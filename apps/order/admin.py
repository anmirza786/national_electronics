from django.contrib import admin

from .models import Order, OrderItem


class OrderAdmin(admin.ModelAdmin):
    list_display = ('user','total','status','order_at','phone','postalcode')
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product',
                    'quantity','price')

admin.site.register(Order,OrderAdmin)
admin.site.register(OrderItem,OrderItemAdmin)
