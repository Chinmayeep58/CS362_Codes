import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://127.0.0.1:6000/")

# Test matrices
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

result = proxy.multiply(A, B)

print("Result Matrix:")
for row in result:
    print(row)
