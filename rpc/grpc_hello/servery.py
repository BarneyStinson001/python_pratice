from concurrent import futures

import grpc
from grpc_hello.protos import helloworld_pb2,helloworld_pb2_grpc

class Greeter(helloworld_pb2_grpc.GreeterServicer):
    def SayHello(self,request,context):
        return helloworld_pb2.HelloReply(message=f"你好，{request.name}")

if __name__ =='__main__':
    #实例化
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(),server)
    server.add_insecure_port('[::]:10053')
    server.start()
    print("hello")
    server.wait_for_termination()