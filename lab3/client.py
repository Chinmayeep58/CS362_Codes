import socket
import threading

SERVER_IP='127.0.0.1'
PORT=int(input("Enter your own server port: "))

def receive(sock):
    while True:
        try:
            msg=sock.recv(1024).decode()
            if not msg:
                break
            print("\nReceived:", msg)
        except:
            break

client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_IP, PORT))

name=input("Enter name: ")

threading.Thread(target=receive, args=(client,)).start()

while True:
    msg=input()
    client.send(f"CLIENT:{name}: {msg}".encode())
