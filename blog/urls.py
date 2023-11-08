from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new_blog/', views.new_blog, name='new_blog'),
]