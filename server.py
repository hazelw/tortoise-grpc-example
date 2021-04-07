from concurrent import futures

import grpc

import snakes_pb2_grpc
from snakes_server import SnakesServiceServicer


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    snakes_pb2_grpc.add_SnakesServiceServicer_to_server(SnakesServiceServicer(), server)
    server.add_insecure_port("[::]:50052")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
