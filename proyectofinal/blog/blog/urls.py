from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('<int:pk>/', views.blog_detail, name='blog_detail'),
    path('create/', views.create_blog, name='create_blog'),
    path('about/', views.about, name='about'),  # Ruta para "Acerca de mí"
]
urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('<int:pk>/', views.blog_detail, name='blog_detail'),
    path('create/', views.create_blog, name='create_blog'),
    path('<int:pk>/edit/', views.update_blog, name='update_blog'),
    path('<int:pk>/delete/', views.delete_blog, name='delete_blog'),
    path('about/', views.about, name='about'),
]
