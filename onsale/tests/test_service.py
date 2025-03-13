import pytest
from django.db.models import QuerySet
from onsale.models import Product, Category, Tag
from onsale.service import get_all_categories, get_all_tags, find_products


@pytest.fixture
def setup_db(db):
    # Load the test data using Django's loaddata
    from django.core.management import call_command
    call_command("loaddata", "small_test_data.json")


def test_get_all_categories(setup_db):
    categories = get_all_categories()
    assert isinstance(categories, QuerySet)
    assert categories.count() == 4  # Expecting 4 categories (Furniture, Electronics, Clothing, Books)
    assert categories.filter(title="Books").exists()


def test_get_all_tags(setup_db):
    tags = get_all_tags()
    assert isinstance(tags, QuerySet)
    assert tags.count() == 4  # Expecting 4 tags, including the unused one
    assert Tag.objects.filter(title="Exclusive Offer").exists()  # Ensure unused tag exists


@pytest.mark.parametrize(
    ('search_val', 'expected_number'),
    [
        ("Laptop", 1),
        ("modern", 3),
        ("Blablanla", 0),
    ]
)
def test_find_products_search(setup_db, search_val, expected_number):
    products = find_products(search_val, "", [])
    assert isinstance(products, QuerySet)
    assert products.count() == expected_number


def test_search_is_case_insensitive(setup_db):
    result1 = find_products('laptop', "", [])
    result2 = find_products('LaptoP', "", [])
    assert result1.count() == result2.count()


# Test find_products() filtering by category
def test_find_products_by_category(setup_db):
    category = Category.objects.get(title="Electronics")
    products = find_products("", category.id, [])
    assert isinstance(products, QuerySet)
    assert products.count() == 2  # Electronics category should have products


def test_existing_product_shadowed_by_category(setup_db):
    other_category = Category.objects.get(title="Electronics")
    products = find_products("dining chair", other_category.id, [])
    assert not products


def test_existing_product_shadowed_by_tags(setup_db):
    chair_absent_tags = Tag.objects.exclude(products__title__icontains="dining chair").values_list("pk", flat=True)
    no_chair = find_products("dining chair", "", list(chair_absent_tags))
    assert no_chair.count() == 0


# Test find_products() filtering by tags
def test_find_products_by_tag(setup_db):
    tag = Tag.objects.get(title="Best Seller")
    products = find_products("", "", [tag.id])
    assert products.count() == 4  # Some products should have this tag


def test_find_by_tags_no_duplication(setup_db):
    """ If there is product A has tag2 and tag3 we shouldn't see it twice """
    products = find_products("", "", [2, 3])
    assert products.count() == 6


def test_find_products_empty_category(setup_db):
    category = Category.objects.get(title="Books")
    products = find_products("", category.id, [])
    assert products.count() == 0  # No products should belong to 'Books'


# Test find_products() returns empty for an unused tag
def test_find_products_unused_tag(setup_db):
    tag = Tag.objects.get(title="Exclusive Offer")
    products = find_products("", "", [tag.id])
    assert products.count() == 0  # No products should have this tag


def test_find_by_category_and_tags(setup_db):
    products = find_products("", 3, [1])
    assert products.count() == 1

@pytest.mark.parametrize(
    ('search_val', 'category_id', 'tags', 'expected_number'),
    [
        ("", 1, [], 3 ),
        ("wooden", 1, [], 1),
        ("wooden", 1, [2], 1),  # with existing tag
        ("wooden", 1, [3], 0),  # with non-existent tag
        ("wooden!", 1, [], 0),
    ]
)
def test_find_by_search_and_category_and_tags(setup_db, search_val, category_id, tags, expected_number):
    products = find_products(search_val, category_id, tags)
    assert products.count() == expected_number
