import socket
import json

# Test matrices
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

client_socket = socket.socket()
client_socket.connect(("localhost", 5000))

data = json.dumps({'A': A, 'B': B})
client_socket.send(data.encode())

result_data = client_socket.recv(4096).decode()
result = json.loads(result_data)

print("Result Matrix:")
for row in result:
    print(row)

client_socket.close()
