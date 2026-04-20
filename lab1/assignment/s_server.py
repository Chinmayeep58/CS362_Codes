import socket
import json

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

server_socket = socket.socket()
server_socket.bind(("localhost", 5000))
server_socket.listen(1)

print("Server waiting for client...")

conn, addr = server_socket.accept()
print("Client connected")

data = conn.recv(4096).decode()
matrices = json.loads(data)
A = matrices['A']
B = matrices['B']

result = multiply(A, B)

conn.send(json.dumps(result).encode())
conn.close()
