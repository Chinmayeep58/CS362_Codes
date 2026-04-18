# socket steps
''' 
1. create socket (open)
2. bind to the port and ip
3. listen for clients
4. receive data
5. complete function
6. send to client and close the socket
'''

import socket
import threading

host="127.0.0.1"
ports=[5000, 5001, 5002]

def handle_clients(conn, addr, port):
    print(f"connected to {addr} on port {port}")
    with conn:
        conn.sendall(b"choose task:\n1. arithmetic\n2. string analysis")
        while True:
            data=conn.recv(1024)
            if not data:
                break
            msg=data.decode("utf-8",errors="ignore").strip()
            parts=msg.split()
            op=parts[0]

            if op=="1":
                return


def start_server(port):
    socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    socket.bind((host,port))
    socket.listen()
    while True:
        conn, addr=socket.accept()
        threading.Thread(target=handle_clients,args=(conn, addr, port),daemon=True).start()


def main():
    for port in ports:
        threading.Thread(target=start_server,args=(port,), daemon=True).start()
    while True:
        pass

if __name__=="__main__":
    main()