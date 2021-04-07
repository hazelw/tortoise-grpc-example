import asyncio
import grpc

import snakes_pb2_grpc
from snakes_server import SnakesServiceServicer


async def serve():
    server = grpc.aio.server()
    snakes_pb2_grpc.add_SnakesServiceServicer_to_server(SnakesServiceServicer(), server)
    server.add_insecure_port("[::]:50052")
    await server.start()
    await server.wait_for_termination()


if __name__ == "__main__":
    asyncio.run(serve())
