import socket

r1 = int(input("Enter rows of Matrix A: "))
c1 = int(input("Enter columns of Matrix A: "))

A = []
print("Enter Matrix A:")
for i in range(r1):
    A.append(list(map(int, input().split())))

r2 = int(input("Enter rows of Matrix B: "))
c2 = int(input("Enter columns of Matrix B: "))

B = []
print("Enter Matrix B:")
for i in range(r2):
    B.append(list(map(int, input().split())))

client_socket = socket.socket()
client_socket.connect(("localhost", 5000))

data = str(r1) + "|" + str(c1) + "|" + str(A) + "|" + str(r2) + "|" + str(c2) + "|" + str(B)
client_socket.send(data.encode())

result = client_socket.recv(4096).decode()

print("Result Matrix:")
print(result)

client_socket.close()
