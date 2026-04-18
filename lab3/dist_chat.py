import socket
import threading

HOST = '0.0.0.0'
PORT = int(input("Enter your server port: "))

PEER_IP = input("Enter peer IP: ")
PEER_PORT = int(input("Enter peer port: "))

#server
def handle_connection(conn):
    while True:
        try:
            msg = conn.recv(1024).decode()
            if not msg:
                break
            print(msg)
        except:
            break

    conn.close()


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    while True:
        conn, addr = server.accept()

        threading.Thread(
            target=handle_connection,
            args=(conn,)
        ).start()


#client
def send_message():
    name = input("Enter name: ")

    while True:
        msg = input()
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((PEER_IP, PEER_PORT))
        client.send(f"{name}: {msg}".encode())
        client.close()

threading.Thread(
    target=start_server
).start()

send_message()
