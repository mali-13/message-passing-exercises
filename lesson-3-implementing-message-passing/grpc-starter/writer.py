import grpc
import orders_pb2
import orders_pb2_grpc


"""
Sample implementation of a writer that can be used to write messages to gRPC.
"""

print("Sending sample payload...")

channel = grpc.insecure_channel("localhost:5005")
stub = orders_pb2_grpc.OrderServiceStub(channel)

# Update this with desired payload
order = orders_pb2.OrderMessage(
    id="15ORD",
    created_by="14USR",
    status=orders_pb2.OrderMessage.Status.QUEUED,
    created_at="2020-03-12",
    equipment=[orders_pb2.OrderMessage.Equipment.KEYBOARD]
)


response = stub.Create(order)
