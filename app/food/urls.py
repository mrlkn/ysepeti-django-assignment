from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from food import views

urlpatterns = [
    path('food/', views.FoodViewSet.as_view({
        "post": "create",
        "get": "list"
    }),
         name="food-foods"
    ),
    path('food/<int:pk>', views.FoodViewSet.as_view({
        "get": "retrieve",
        "put": "update",
        "delete": "destroy"
    }),
         name="food-food"
    ),
    path('category/', views.CategoryViewSet.as_view({
        "post": "create",
        "get": "list"
    }),
         name="category-categories"
    ),
    path('category/<int:pk>', views.CategoryViewSet.as_view({
        "get": "retrieve",
        "put": "update",
        "delete": "destroy"
    }),
         name="category-category"
    )
]

urlpatterns = format_suffix_patterns(urlpatterns)
