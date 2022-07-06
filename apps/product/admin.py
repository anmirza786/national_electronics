from itertools import product
from pyexpat import model
from django.contrib import admin

from .models import Category, Product, ProductImage

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','slug')

class ProductImageAdmin(admin.TabularInline):
    model = ProductImage
    extra = 1
    max_num = 5
    min_num = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductImageAdmin,
    ]
    list_display = ('title','category','price','date_added')
    list_display_links = ('title', )
    list_filter = ('category', )
    exclude = ('slug',)
    def save(self, request):
        self.image = ProductImage.objects.all().first()
        return super().save(request)
    class Meta:
        model=Product


admin.site.register(Category,CategoryAdmin)
# admin.site.register(Product,ProductAdmin)
# admin.site.register(ProductImage)