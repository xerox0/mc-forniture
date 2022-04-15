import views
from django.urls import path



from .views import ThreadCreate, ThreadList, RispostaList,add_comment

app_name ='forum'

urlpatterns = [
    path('create',ThreadCreate.as_view(), name='thread-create'),
    path('list/',ThreadList.as_view(),name='thread-list'),
    path('forum/<int:pk>/discussione/', RispostaList.as_view(),name='discussione'),
    path('forum/<int:pk>/creacommento/',add_comment,name='crea-commento')
    ]