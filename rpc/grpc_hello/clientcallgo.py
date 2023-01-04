import grpc

from grpc_hello.protos import helloworld_pb2,helloworld_pb2_grpc

if __name__ == "__main__":
    with grpc.insecure_channel("localhost:8090") as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        rsp:helloworld_pb2.HelloReply = stub.SayHello(helloworld_pb2.HelloRequest(name="mike"))
        print(rsp.message)