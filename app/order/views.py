import json

from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import viewsets

from order import choices
from order.helpers import UUIDEncoder
from order.models import Order
from order.serializers import OrderSerializer
from order.helpers import redis_cli, order_pubsub


class OrderView(viewsets.ModelViewSet):
    """
    ModelViewset for Order.
    """
    serializer_class = OrderSerializer
    pagination_class = PageNumberPagination
    permission_classes = [AllowAny]
    lookup_field = "status"

    def get_queryset(self) -> 'Queryset[Order]':
        """
        Overridden queryset for filtering with status.
        If query params has status it will filter the Order's with the given status

        :return: Queryset(Order)
        """
        queryset = Order.objects.all()
        status = self.request.query_params.get("status")
        if status:
            queryset = queryset.filter(status=status)

        return queryset

    def create(self, request: Request, *args, **kwargs) -> Response:
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        redis_cli.pubsub()
        redis_cli.publish('orders', json.dumps(serializer.data, cls=UUIDEncoder))

        return Response(serializer.data, status=201)

    @action(detail=True, methods=["POST"], name="process-order")
    def process_order(self, request: Request, *args, **kwargs) -> Response:
        """
        POST API to process orders.

        After getting POST request, it gets the messages from the subscribed PUB/SUB. Ignoring if the
        order["data"] = 1 because it means subscribed message. After finding the Order changing its status to completed.
        :param request: Request
        :param args: args
        :param kwargs: kwargs
        :return: Response
        """
        order = order_pubsub.get_message()
        if order and not order['data'] == 1:
            order = json.loads(order["data"])
            order = Order.objects.get(id=order.get("id"))
            order.status = choices.COMPLETED
            order.save()

            return Response(data=f"{order.id}, {choices.COMPLETED}", status=200)
        return Response(data="No order found in Pub/Sub", status=400)
