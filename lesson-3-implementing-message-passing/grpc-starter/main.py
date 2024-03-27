import time
from concurrent import futures

import grpc
import orders_pb2
import orders_pb2_grpc


class OrderServicer(orders_pb2_grpc.OrderServiceServicer):
    def Get(self, request, context):
        first_order = orders_pb2.OrderMessage(
            id="2222",
            created_by="USER123",
            status=orders_pb2.OrderMessage.Status.QUEUED,
            created_at='2020-03-12',
            equipment=[orders_pb2.OrderMessage.Equipment.KEYBOARD]
        )

        second_order = orders_pb2.OrderMessage(
            id="3333",
            created_by="USER123",
            status=orders_pb2.OrderMessage.Status.QUEUED,
            created_at='2020-03-11',
            equipment=[orders_pb2.OrderMessage.Equipment.MOUSE]
        )

        result = orders_pb2.OrderMessageList()
        result.orders.extend([first_order, second_order])
        return result

    def Create(self, request, context):
        print("Received a message!")

        request_value = {
            "id": request.id,
            "created_by": request.created_by,
            "status": request.status,
            "created_at": request.created_at,
            "equipment": ["KEYBOARD"]
        }
        print(request_value)

        return orders_pb2.OrderMessage(**request_value)


# Initialize gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
orders_pb2_grpc.add_OrderServiceServicer_to_server(OrderServicer(), server)


print("Server starting on port 5005...")
server.add_insecure_port("[::]:5005")
server.start()
# Keep thread alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
