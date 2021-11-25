from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from app.user import views

urlpatterns = [
    path('users/', views.UserViewSet.as_view({
        "post": "create",
        "get": "list"
    }),
         name="user-users"
    ),
    path('users/<int:pk>', views.UserViewSet.as_view({
        "get": "retrieve",
        "put": "update",
        "delete": "destroy"
    }),
         name="user-user"
    )
]

urlpatterns = format_suffix_patterns(urlpatterns)
