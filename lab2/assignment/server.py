import socket
import threading

HOST="127.0.0.1"
PORTS=[5000, 5001, 5002]


def handle_client(conn, addr, port):
    print(f"[+] Connected {addr} on port {port}")

    with conn:
        conn.sendall(b"Choose task:\n1. Arithmetic\n2. String Analysis\n")

        while True:
            data = conn.recv(1024)
            if not data:
                break

            msg=data.decode("utf-8", errors="ignore").strip()
            parts=msg.split()
            op=parts[0]

            if op=="1":
                conn.sendall(b"Enter operation (add/sub/mul/div) followed by two numbers:\n")
                req = conn.recv(1024).decode().strip().split()
                try:
                    op=req[0]
                    a=float(req[1])
                    b=float(req[2])
                    if op=="add":
                        res=a+b
                    elif op=="sub":
                        res=a - b
                    elif op=="mul":
                        res=a * b
                    elif op=="div":
                        if b == 0:
                            conn.sendall(b"Division by zero error\n")
                            continue
                        res=a/b
                    else:
                        conn.sendall(b"Invalid operation\n")
                        continue
                    conn.sendall(f"Result: {res}\n".encode())
                except:
                    conn.sendall(b"Invalid arithmetic input\n")

            elif op=="2":
                conn.sendall(b"Enter string to analyze:\n")
                text=conn.recv(1024).decode().strip()

                upper=text.upper()
                chars=len(text)
                words=len(text.split())

                reply = (f"Uppercase: {upper}\n" f"Characters: {chars}\n" f"Words: {words}\n")
                conn.sendall(reply.encode())

            elif op=="exit":
                break
            
    print(f"[-] Disconnected {addr} from port {port}")


def start_server(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, port))
    s.listen()
    print(f"Server started on {HOST}:{port}")
    while True:
        conn, addr=s.accept()
        threading.Thread(target=handle_client,args=(conn, addr, port),daemon=True).start()


def main():
    for port in PORTS:
        threading.Thread(target=start_server,args=(port,),daemon=True).start()
    while True:
        pass

if __name__=="__main__":
    main()
