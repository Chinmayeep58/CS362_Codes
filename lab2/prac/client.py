'''
1. create socket
2. bind to ip and port
3. connect to server
4. send and receive data
5. close socket
'''

import socket
import os

host="127.0.0.1"

def main():
    pid=os.getpid()
    port=int(input('enter port number (5000/5001,5002)'))
    socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    with socket as s:
        s.connect((host,port))
        data=s.recv(1024).decode()
        while True:
            msg=input()
            s.sendall((msg+"\n").encode())
            reply=s.recv(4096)
            if not reply:
                break
            print(reply.decode())


if __name__=="__main__":
    main()
