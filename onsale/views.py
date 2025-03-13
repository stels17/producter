from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from onsale import service


def bad_request_view(request, exception=None, message=None):
    """ For directing an errored request """
    context = {
        "message": message if message else "Invalid request. Please try again."
    }
    return render(request, "400.html", context, status=400)


def validate_id_str(id_str: str):
    try:
        id = int(id_str)
        return id > 0
    except (ValueError, TypeError):
        return False


# Create your views here.
@require_http_methods(['GET'])
def product_list(request):
    """ Accepts user requests and prepares data for rendering the template """
    page_number = request.GET.get("page", 1)
    search_str = request.GET.get('q', "")
    category_id = request.GET.get('category', "")
    tag_ids = request.GET.getlist('tags', [])  # Get selected tag IDs

    # Validate the provided params
    if category_id and not validate_id_str(category_id):
        return bad_request_view(request, message="Invalid category id")

    for id_str in tag_ids:
        if not validate_id_str(id_str):
            # raise SuspiciousOperation("Invalid category or tag id")
            return bad_request_view(request, message="Invalid tag id")

    products_found = service.find_products(search_val=search_str, category_id=category_id, tag_ids=tag_ids)

    # Apply pagination (custom number per page)
    paginator = Paginator(products_found, settings.PRODUCTS_PER_PAGE)
    page_obj = paginator.get_page(page_number)

    return render(request, 'onsale/product_list.html', {
        'products': page_obj,
        'categories': service.get_all_categories(),
        'tags': service.get_all_tags(),
        'selected_tags': tag_ids,  # Ensures checkboxes remain checked
        'total_products': paginator.count,
    })
