from django.urls import path
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
path('', views.productList.as_view(), name='product_list'),
path('new', views.productCreate.as_view(), name='product_new'),
path('view/<int:pk>', views.productView.as_view(), name='product_view'),
path('edit/<int:pk>', views.productUpdate.as_view(), name='product_edit'),
path('delete/<int:pk>', views.productDelete.as_view(), name='product_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

