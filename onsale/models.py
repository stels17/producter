from django.db import models


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['title']


class Tag(models.Model):
    title = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class Product(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag, related_name="products", blank=True)
    description = models.TextField()
    price = models.PositiveIntegerField(verbose_name="Price, cents", help_text="Price in CENTS")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def price_real(self):
        return (self.price or 0) / 100

    @property
    def price_display(self):
        return f'${self.price_real:,.2f}'

    def __str__(self):
        return f"{self.title} {self.price_display}"

    def tags_list(self):
        return ",".join(self.tags.values_list('title', flat=True))[:100]
