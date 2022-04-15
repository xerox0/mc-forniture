from django.urls import path


from products import views
from .views import ThreadCreate, ThreadList, RispostaList, RispostaCreate

app_name ='forum'

urlpatterns = [
    path('create',ThreadCreate.as_view(), name='thread-create'),
    path('list/',ThreadList.as_view(),name='thread-list'),
    path('list/<int:pk>/discussione/', RispostaList.as_view(),name='discussione'),
    path('creacommento',RispostaCreate.as_view(),name='crea-commento')
    ]