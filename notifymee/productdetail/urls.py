from django.urls import path
from productdetail import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('addnewproducts/',views.AddnewProducts,name="AddnewProducts"),
    path('productlist/',views.productlist,name = "productlist"),
]