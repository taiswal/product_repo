from django.urls import path
from .views import index_p,create_product, product_list, update_product, delete_product
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # path('product_list/', product_list, name='product_list'),
    path('product_list', product_list, name='product_list'),
    path('create/', create_product, name='create_product'),
    path('update/<int:pk>/', update_product, name='update_product'),
    path('delete/<int:pk>/', delete_product, name='delete_product'),
    path('index_p/',index_p,name='index_p')
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


