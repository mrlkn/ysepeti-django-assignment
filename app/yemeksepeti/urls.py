from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("user.urls")),
    path('api/', include("food.urls")),
    path('api/', include("restaurant.urls")),
    path('api/', include("order.urls"))
]
