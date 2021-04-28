from django.urls import path
from . import views

urlpatterns = [
    path('',views.store,name='store'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('login/',views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/',views.user_register, name='register'),

    path('update_item/', views.updateItem, name='update_item'),
    path('process_order/', views.processOrder, name='process_order'),
]