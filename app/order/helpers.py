import json
from uuid import UUID

import redis


class UUIDEncoder(json.JSONEncoder):
    """
    Encodes UUID fields by converting them to hex
    """
    def default(self, obj: object) -> json:
        if isinstance(obj, UUID):
            return obj.hex
        return json.JSONEncoder.default(self, obj)


# very bad implementation of redis pub/sub

redis_cli = redis.Redis(host='redis', port=6379, db=0)
order_pubsub = redis_cli.pubsub()
order_pubsub.subscribe('orders')
