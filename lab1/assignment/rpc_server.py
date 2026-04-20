from xmlrpc.server import SimpleXMLRPCServer

def multiply(A, B):
    r1 = len(A)
    c1 = len(A[0])
    r2 = len(B)
    c2 = len(B[0])
    if c1 != r2:
        raise ValueError("Incompatible dimensions")
    result = [[0 for j in range(c2)] for i in range(r1)]

    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                result[i][j] += A[i][k] * B[k][j]
    return result

server = SimpleXMLRPCServer(("0.0.0.0", 6000))
print("RPC Server running...")

server.register_function(multiply, "multiply")
server.serve_forever()
