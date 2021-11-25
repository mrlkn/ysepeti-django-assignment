from django.urls import path

from app.restaurant import views

urlpatterns = [
    path('restaurant/', views.RestaurantViewSet.as_view({
        "post": "create",
        "get": "list"
    }),
         name="restaurant-restaurants"
    ),
    path('restaurant/<int:pk>', views.RestaurantViewSet.as_view({
        "get": "retrieve",
        "put": "update",
        "delete": "destroy"
    }),
         name="restaurant-restaurant"
    )
]
