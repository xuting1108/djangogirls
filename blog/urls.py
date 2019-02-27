from django.urls import path
from . import views

#Aqui, estamos importando do Django
# a função url e todas as nossas views do aplicativo blog

urlpatterns = [
    path('', views.post_list, name='post_list'),
#Como você pode ver, estamos agora atribuindo uma view
#chamada post_list à URL raiz.
#A última parte, name='post_list', é o nome da URL que será usado para identificar a view.

    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]