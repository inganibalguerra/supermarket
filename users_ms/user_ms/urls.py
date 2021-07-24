from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from user_ms.views.category_view import CategoryList
from user_ms.views.category_view import CategoryDetail
from user_ms.views.product_view import ProductList
from user_ms.views.product_view import ProductDetail
from user_ms.views.user_view import UserList
from user_ms.views.user_view import UserDetail

urlpatterns = [
    path('categories/', CategoryList.as_view()),
    path('categories/<int:pk>', CategoryDetail.as_view()),
    path('products/', ProductList.as_view()),
    path('products/<int:pk>', ProductDetail.as_view()),
    path('users/', UserList.as_view()),
    path('users/<int:pk>', UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)