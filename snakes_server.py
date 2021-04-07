import snakes_pb2
import snakes_pb2_grpc


class SnakesServiceServicer(snakes_pb2_grpc.SnakesServiceServicer):
    def GetSnake(self, request, context):
        return snakes_pb2_grpc.GetSnakeResponse(id=3)

    def CreateSnake(self, request, context):
        return snakes_pb2_grpc.CreateSnakeResponse(name="ssss", pattern="dots")
