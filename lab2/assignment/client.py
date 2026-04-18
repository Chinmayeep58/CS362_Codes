import socket
import os

HOST = "127.0.0.1"

def main():
    pid = os.getpid()

    port = int(input("Enter server port (5000 / 5001 / 5002): "))

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, port))
        print(f"Client PID={pid} connected to port {port}\n")

        print(s.recv(1024).decode(), end="")

        while True:
            msg = input("> ")
            s.sendall((msg + "\n").encode())

            reply = s.recv(4096)
            if not reply:
                break
            print(reply.decode(), end="")

if __name__ == "__main__":
    main()
