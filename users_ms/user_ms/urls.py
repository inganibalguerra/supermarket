from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from user_ms.views.user_view import UserList
from user_ms.views.user_view import UserDetail

urlpatterns = [
    path('users/', UserList.as_view()),
    path('users/<int:pk>', UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)