from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.single_post_page),
    path('', views.index),
    path('bulletin-board/', views.bulletin_board),

]
