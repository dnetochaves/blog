from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostIndex.as_view(), name='index'),
    path('categoria/', views.PostCategoria.as_view(), name='index'),
    path('busca/', views.PostBusca.as_view(), name='index'),
    path('posts_detalhes/<int:pk>/', views.PostDetalhes.as_view(), name='posts_detalhes'),
] 