import django.db.models
from django.conf import settings
from django.contrib import admin
from django.forms.widgets import TextInput

from onsale import models
from onsale.admin_filters import MultiSelectRelatedFieldListFilter

# Register your models here.
admin.site.site_header = settings.ADMIN_PANEL_TITLE
admin.site.site_title = "Producter Admin Portal"
admin.site.index_title = "Welcome to Producter Portal"

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ['created_at']

@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    readonly_fields = ['created_at']


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):

    readonly_fields = ['price_display', 'created_at', 'updated_at']
    filter_horizontal = ['tags']
    list_display = ['title', 'price_display', 'category', 'updated_at', 'tags_list']
    list_filter = ['category', ('tags', MultiSelectRelatedFieldListFilter)]
    # list_filter = ['category', ('tags', admin.RelatedFieldListFilter)]

    formfield_overrides = {
        django.db.models.PositiveIntegerField : {'widget': TextInput(attrs={'size': 20, 'style': 'width: 150px;'})},
    }

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('category').prefetch_related('tags')
