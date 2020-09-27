import logging
import grpc

import python_to_python_two_way_stream_pb2
import python_to_python_two_way_stream_pb2_grpc

from datetime import datetime


REQUEST_COUNT = 10000


def run():
    with grpc.insecure_channel(
        "localhost:50051", compression=grpc.Compression.Gzip
    ) as channel:

        stub = python_to_python_two_way_stream_pb2_grpc.Two_way_stream_python_to_pythonStub(channel)
        start = datetime.now()
        response_iterator = stub.increase(python_to_python_two_way_stream_pb2.IncreaseRequest(num=i) for i in range(REQUEST_COUNT))
        # This is is actually little problematic. We create a request stream but we do not know request/response matching. I am able to check it the way I am doing because order of responses are guaranteed.
        assert all(map(lambda tp: tp[0]+1 == tp[1].num , zip(range(REQUEST_COUNT), response_iterator)))
        print(f"{REQUEST_COUNT} requests is completed in {datetime.now() - start}")


if __name__ == "__main__":
    logging.basicConfig()
    run()
