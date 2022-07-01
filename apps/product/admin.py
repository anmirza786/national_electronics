from django.contrib import admin

from .models import Category, Product, ProductImage

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','slug')
class ProductAdmin(admin.ModelAdmin):
    list_display = ('category','title','price','date_added','image')
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product','image')

admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(ProductImage,ProductImageAdmin)