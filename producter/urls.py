"""
URL configuration for producter project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import re
from django.conf import settings
from django.contrib import admin
from django.core.exceptions import ImproperlyConfigured
from django.urls import path, re_path
from django.views.static import serve

from onsale import views

handler400 = views.bad_request_view

def static(prefix, view=serve, **kwargs):
    """
    Return a URL pattern for serving files both in DEBUG and PRODUCTION mode.
    We redefine from django.conf.urls.static import static, because we want run application without nginx for static
    But when we set DEBUG = False - we have problems with static, core function doesn't handle static in this case

    urlpatterns = [
        # ... the rest of your URLconf goes here ...
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    """
    if not prefix:
        raise ImproperlyConfigured("Empty static prefix not permitted")
    return [
        re_path(
            r"^%s(?P<path>.*)$" % re.escape(prefix.lstrip("/")), view, kwargs=kwargs
        ),
    ]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.product_list, name='product_list'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
