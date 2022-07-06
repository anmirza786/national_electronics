from django.urls import path

from . import views

urlpatterns = [
    path('',views.veiwProducts,name='view_products'),
    path('search/', views.search, name='search'),
    path('<slug:category_slug>/<slug:product_slug>/', views.product, name='product'),
    path('<slug:category_slug>/', views.category, name='category')
]