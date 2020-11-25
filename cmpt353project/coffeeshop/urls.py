from django.urls import path

from . import views

urlpatterns = [
    path('menu/', views.menu, name='menu'),
    path('order/', views.order, name='order'),
    path('confirm/', views.confirm, name='confirm')
]