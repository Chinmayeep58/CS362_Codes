import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://127.0.0.1:6000/")

r1 = int(input("Enter rows of Matrix A: "))
c1 = int(input("Enter columns of Matrix A: "))

A = []
print("Enter Matrix A:")
for i in range(r1):
    A.append(list(map(int, input().split())))

r2 = int(input("Enter rows of Matrix B: "))
c2 = int(input("Enter columns of Matrix B: "))

B = []
print("Enter Matrix B:")
for i in range(r2):
    B.append(list(map(int, input().split())))

result = proxy.multiply(A, B)

print("Result Matrix:")
for row in result:
    print(row)
