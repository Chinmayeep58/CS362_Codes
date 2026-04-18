import socket

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

server=socket.socket()
server.bind(("localhost",5000))
server.listen(1)

print("Server waiting for client")
conn, addr=server.accept()
print("client connected")

data=conn.recv(4096).decode().split("|")
a=eval(data[0])
b=eval(data[1])
ans=mul(a,b)
conn.send(str(ans).encode())
conn.close()