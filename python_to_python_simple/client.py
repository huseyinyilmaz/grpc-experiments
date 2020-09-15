import logging
import grpc

import python_to_python_simple_pb2
import python_to_python_simple_pb2_grpc
from datetime import datetime


REQUEST_COUNT = 10000


def run():
    with grpc.insecure_channel(
        "localhost:50051", compression=grpc.Compression.Gzip
    ) as channel:

        stub = python_to_python_simple_pb2_grpc.Simple_python_pythonStub(channel)
        start = datetime.now()
        for i in range(REQUEST_COUNT):
            response = stub.increase(python_to_python_simple_pb2.IncreaseRequest(num=i))
            assert response.num == i + 1
        print(f"{REQUEST_COUNT} requests is completed in {datetime.now() - start}")


if __name__ == "__main__":
    logging.basicConfig()
    run()
