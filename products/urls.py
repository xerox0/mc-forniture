from django.urls import path


from products import views

from .views import ProdottiList, ProdottiDetail, ProdottiCreate, ProdottiDelete,ProdottiUpdate

app_name = 'prod'

urlpatterns = [
    path('products/<int:pk>/detail', ProdottiDetail.as_view(), name='products-detail'),
    path('products/<int:pk>/list', ProdottiList.as_view(), name='products-list'),
    path('products/create',ProdottiCreate.as_view(), name='products-create'),
    path('products/<int:pk>/delete',ProdottiDelete.as_view(),name = 'products-delete'),
    path('products/<int:pk>/update',ProdottiUpdate.as_view(),name = 'products-update'),
    path('categoria/',views.CategoriaView,name = 'products-category')
]