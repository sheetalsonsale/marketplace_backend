
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('user.urls')),
    # path('products/', include('product.urls')),
    # path('card/', include('card.urls')),
    # path('orders/', include('order.urls')),
    
]
