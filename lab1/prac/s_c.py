import socket

r1=int(input("Enter number of rows: "))
c1=int(input("Enter number of columns: "))

a=[]
print("Enter matrix A:")
for i in range(r1):
    a.append(list(map(int,input().split())))

r2=int(input("Enter number of rows: "))
c2=int(input("Enter number of columns: "))

b=[]
print("Enter matrix A:")
for i in range(r2):
    b.append(list(map(int,input().split())))

client=socket.socket()
client.connect(("localhost",5000))

data=str(a)+"|"+str(b)
ans=client.recv(4096).decode()
print("result matrix")
print(ans)
client.close()