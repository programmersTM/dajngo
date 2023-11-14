from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new_blog/', views.new_blog, name='new_blog'),
    path('<str:title>/', views.detail_blog, name='detail_blog'),
    path('<int:pk>/edit', views.edit_blog, name='edit_blog'),
    path('<int:pk>/delete', views.delete_blog, name='delete_blog'),
]