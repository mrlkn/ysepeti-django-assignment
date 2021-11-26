from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from app.order import views

urlpatterns = [
    path('order/', views.OrderView.as_view({
        "post": "create",
        "get": "list",
    }),
        name="order-orders"
    ),
    path('order/<int:pk>', views.OrderView.as_view({
        "get": "retrieve",
        "put": "update",
        "delete": "destroy"
    }),
         name="order-order"
    ),
    path('order/process_order', views.OrderView.as_view({
        "post": "process_order"
    }),
         name="process-order"
    )
]


urlpatterns = format_suffix_patterns(urlpatterns)
