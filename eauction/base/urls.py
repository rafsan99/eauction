from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),
    path('create-product/', views.createProduct, name="create-product"),
    path('product/<str:pk>/', views.product, name="product"),
    path('edit-bid/<str:pk>/', views.editBid, name="edit-bid"),
]
