from typing import Sequence

from django.db.models import QuerySet, Q

from onsale.models import Product, Category, Tag


def get_all_categories() -> QuerySet[Category]:
    return Category.objects.all()

def get_all_tags() ->QuerySet[Tag]:
    return Tag.objects.all()


def find_products(search_val: str, category_id: int | str, tag_ids: Sequence) -> QuerySet[Product]:
    # Get products and categories
    products = Product.objects.select_related('category').prefetch_related('tags').all()

    # Apply search filtering
    if search_val:
        products = products.filter(Q(title__icontains=search_val) | Q(description__icontains=search_val))

    # Apply category filtering
    if category_id:
        products = products.filter(category_id=category_id)

    # Apply tag filtering (show products that have *any* of the selected tags)
    if tag_ids:
        products = products.filter(tags__id__in=tag_ids).distinct()

    return products.order_by('id')
