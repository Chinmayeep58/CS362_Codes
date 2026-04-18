from xmlrpc.server import SimpleXMLRPCServer

def mul(a, b):
    r1 = len(a)
    c1 = len(a[0])
    r2 = len(b)
    c2 = len(b[0])

    if c1 != r2:
        return "Matrix multiplication not possible"

    ans = [[0 for _ in range(c2)] for _ in range(r1)]

    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                ans[i][j] += a[i][k] * b[k][j]

    return ans

server = SimpleXMLRPCServer(("0.0.0.0", 6000))
print("server running")
server.register_function(mul, "mul")
server.serve_forever()