import socket

def multiply(A, B, r1, c1, c2):
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

data = conn.recv(4096).decode().split("|")

r1 = int(data[0])
c1 = int(data[1])
A = eval(data[2])

r2 = int(data[3])
c2 = int(data[4])
B = eval(data[5])

result = multiply(A, B, r1, c1, c2)

conn.send(str(result).encode())
conn.close()
