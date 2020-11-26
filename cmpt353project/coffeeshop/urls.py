from django.urls import path

from . import views

# all the urls that are used in the application
urlpatterns = [
    path('menu/', views.menu, name='menu'),
    path('order/', views.order, name='order'),
    path('complete/', views.complete, name='complete'),
    path('cancel/', views.cancel, name='cancel')
]