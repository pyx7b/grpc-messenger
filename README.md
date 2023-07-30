# Introduction
This is gRPC client in python talking to a gRPC server on nodeJS.

# Server
Assume you have git clone the code.

1. Go to server directory and install the npm packages:
```
cd server
npm install
```

2. Start the node server locally. It runs on port `50051`, change it to something else if thre is a conflicts.
```
npm start
```
Note that we are using `nodemon` for development purpose.

# Client
Obviously, a server needs a client to talk to:
1. Setup the ypthog

```
cd client
python3 -m venv venv
source venv/bin/activate
pip install grpcio grpcio-tools
```

2. Use the protoc compiler with the grpcio-tools plugin to generate the Python files in the current directory directory for `Message.proto` in the parent directoy `-I..`:
```
python -m grpc_tools.protoc -I.. --python_out=. --grpc_python_out=. ../Message.proto
```

3. Client sends test message to server via gRPC:
```
python3 client.py
```