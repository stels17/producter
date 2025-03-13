from unittest.mock import patch

import pytest
from django.urls import reverse
from django.utils.http import urlencode


@patch('onsale.views.service.get_all_categories', return_value=[])
@patch('onsale.views.service.get_all_tags', return_value=[])
@patch('onsale.views.service.find_products', return_value=[])
def test_wants_ut_to_see_categories_and_tags(mock_find_products, mock_get_all_tags, mock_get_all_categories, client):
    response = client.get(reverse('product_list'))
    mock_get_all_categories.assert_called_once()
    mock_get_all_tags.assert_called_once()
    mock_find_products.assert_called_once()
    assert response.status_code == 200


@pytest.mark.parametrize(
    ('category', 'tags', 'expected_status_code'),
    [
        ('', '', 200),
        ('fff', '', 400),
        ('1', '2,3', 200),
        ('1', 'fffff', 400),
    ]
)
def test_validates_input(client, db, category, tags, expected_status_code):
    params = {
        'category': category,
        'tags': tags.split(',') if tags else [],
    }
    response = client.get(f'/?{urlencode(params, doseq=True)}')
    assert response.status_code == expected_status_code
