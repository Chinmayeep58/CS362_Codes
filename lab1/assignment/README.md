# 2D Matrix Multiplication Service

This project implements a 2D matrix multiplication service using Python, comparing Socket-based communication and Remote Procedure Call (RPC).

## Components

### Socket-based Implementation
- **s_server.py**: Socket server that listens for client connections, receives two matrices, performs multiplication, and sends back the result.
- **s_client.py**: Socket client that sends two test matrices to the server and prints the result.

### RPC-based Implementation
- **rpc_server.py**: XML-RPC server that registers a `multiply` function for matrix multiplication.
- **rpc_client.py**: XML-RPC client that calls the remote `multiply` function and prints the result.

## Test Matrices
- Matrix A: [[1, 2], [3, 4]]
- Matrix B: [[5, 6], [7, 8]]
- Expected Result: [[19, 22], [43, 50]]

## How to Run

### Socket Version
1. Run the server: `python s_server.py`
2. In another terminal, run the client: `python s_client.py`

### RPC Version
1. Run the server: `python rpc_server.py`
2. In another terminal, run the client: `python rpc_client.py`

## Comparison

- **Socket-based**: Low-level, requires manual serialization (using JSON), handles connection management.
- **RPC-based**: Higher-level abstraction, automatic serialization, easier to use, built-in error handling.

Both approaches achieve the same result but RPC is simpler for this use case.