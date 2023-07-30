# Introduction


# Server

1. Install package
```
npm install
```

2. Start server
```
npm start

```
Note that we are using `nodemon` for development purpose.

# Client

1. Installation:

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

3. Run
```
python3 
```