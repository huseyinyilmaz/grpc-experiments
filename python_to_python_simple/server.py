from concurrent import futures
import logging

import grpc
from grpc_reflection.v1alpha import reflection

import python_to_python_simple_pb2
import python_to_python_simple_pb2_grpc


class SimpleAPI(python_to_python_simple_pb2_grpc.Simple_python_pythonServicer):
    def increase(self, request, context):

        return python_to_python_simple_pb2.IncreaseReply(num=request.num+1)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    python_to_python_simple_pb2_grpc.add_Simple_python_pythonServicer_to_server(SimpleAPI(), server)

    SERVICE_NAMES = (
        python_to_python_simple_pb2.DESCRIPTOR.services_by_name['Simple_python_python'].full_name,
        reflection.SERVICE_NAME,
    )

    reflection.enable_server_reflection(SERVICE_NAMES, server)

    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
