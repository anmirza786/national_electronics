from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include('apps.cart.urls')),
    path('', include('apps.buyer.urls')),
    path('', include('apps.core.urls')),
    path('products/', include('apps.product.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)