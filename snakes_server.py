import snakes_pb2
import snakes_pb2_grpc


class SnakesServiceServicer(snakes_pb2_grpc.SnakesServiceServicer):
    def __init__(self):
        pass

    def GetSnake(self, request, context):
        return snakes_pb2.GetSnakeResponse(name="snakey", pattern="dots")

    def CreateSnake(self, request, context):
        return snakes_pb2.CreateSnakeResponse(id=3)
