import snakes_pb2
import snakes_pb2_grpc

from app.models import Snake


class SnakesServiceServicer(snakes_pb2_grpc.SnakesServiceServicer):
    def __init__(self):
        pass

    def GetSnake(self, request, context):
        snake = Snake.get(id=request.id)

        if not snake:
            return snakes_pb2.GetSnakeResponse(error_message="no snake")
        return snakes_pb2.GetSnakeResponse(name=snake.name, pattern=snake.pattern)

    def CreateSnake(self, request, context):
        snake = Snake.create(name=request.name, pattern=request.pattern)

        return snakes_pb2.CreateSnakeResponse(id=snake.id)
