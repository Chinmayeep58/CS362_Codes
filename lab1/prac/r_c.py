import xmlrpc.client

proxy=xmlrpc.client.ServerProxy("http://127.0.0.1:6000/")
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

ans=proxy.mul(a,b)

print("result matrix: ")
for i in ans:
    print(i)