import socket
import threading

HOST='0.0.0.0'
PORT=int(input("Enter your server port: "))

PEER_IP='127.0.0.1'
PEER_PORT=int(input("Enter peer server port: "))

local_clients=[]

def handle_connection(conn):
    while True:
        try:
            msg=conn.recv(1024).decode()
            if not msg:
                break

            #if message is coming from local client
            if msg.startswith("CLIENT:"):
                clean_msg=msg.replace("CLIENT:", "", 1)
                #Forward to peer server 
                forward=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                forward.connect((PEER_IP, PEER_PORT))
                forward.send(f"SERVER:{clean_msg}".encode())
                forward.close()

            #if message is coming from peer server
            elif msg.startswith("SERVER:"):
                clean_msg=msg.replace("SERVER:", "", 1)

                # Deliver to local clients ONLY (no forwarding again)
                for client in local_clients:
                    try:
                        client.send(clean_msg.encode())
                    except:
                        pass

        except:
            break

    if conn in local_clients:
        local_clients.remove(conn)
    conn.close()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("Server running...")

while True:
    conn, addr=server.accept()
    local_clients.append(conn)
    threading.Thread(target=handle_connection, args=(conn,)).start()
