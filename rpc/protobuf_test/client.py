from protobuf_test.proto import hello_pb2

request = hello_pb2.HelloRequest()

request.name="alice"
res=request.SerializeToString()
print(res)
print(len(res))


request2 = hello_pb2.HelloRequest()

res2=request2.ParseFromString(res)
print(res2)