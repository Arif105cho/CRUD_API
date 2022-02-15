from django.urls import path,include
from .views import *

urlpatterns = [
    path('create/',CreateUser.as_view(),name='createuser'),
    path('single/<int:pk>',SingleUser.as_view(),name='single'),

    #Category
    path('category/', CreateCategory.as_view(), name='category'),
    path('singlecategory/<int:pk>', SingleCategory.as_view(), name='singlecategory'),

    #Subcategory
    path('subcategory/', CreateSubCategory.as_view(), name='subcategory'),
    path('singlesubcategory/<int:pk>', SingleSubCategory.as_view(), name='singlesubcategory'),

    #Product
    path('product/', createProduct.as_view(), name='product'),
    path('singleproduct/<int:pk>', SingleProduct.as_view(), name='singleproduct'),

    # Add_cart
    path('addcart/', createAddCart.as_view(), name='product'),
    path('singleaddcart/<int:pk>', SingleAddCart.as_view(), name='singleproduct'),

    # DilveryOrder
    path('delivery/', createOrder.as_view(), name='dilvery'),
    path('singledelivery/<int:pk>', SingleOrder.as_view(), name='singledilvery'),

    #Payment Details
    path('payment/',createPayment.as_view(),name='payment'),

    path('login/',LoginApiView.as_view(),name='login')

]
