from django.urls import path


from products import views

from .views import ProdottiList, ProdottiDetail

app_name = 'prod'

urlpatterns = [
    path('products/<int:pk>/detail', ProdottiDetail.as_view(), name='products-detail'),
    path('list', ProdottiList.as_view(), name='products-list')
]