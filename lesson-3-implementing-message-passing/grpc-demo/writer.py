import grpc
import order_pb2
import order_pb2_grpc

"""
Sample implementation of a writer that can be used to write messages to gRPC.
"""

print("Sending sample payload...")

channel = grpc.insecure_channel("localhost:5005")
stub = order_pb2_grpc.OrderServiceStub(channel)

# Update this with desired payload
order = order_pb2.OrderMessage(
    id="123456",
    created_by="Lucas",
    created_at="9am",
    status=order_pb2.OrderMessage.Status.QUEUED,
    equipment=[order_pb2.OrderMessage.Equipment.MOUSE]
)


response = stub.Create(order)
