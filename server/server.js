const grpc = require("@grpc/grpc-js");
const protoLoader = require("@grpc/proto-loader");
const PROTO_PATH = "../Message.proto";
const ipAddress = '0.0.0.0'; 
const port = 50051;

const loaderOptions = {
  keepCase: true,
  longs: String,
  enums: String,
  defaults: true,
  oneofs: true,
};

// load the proto file
const packageDefinition = protoLoader.loadSync(PROTO_PATH, loaderOptions);
const echoProto = grpc.loadPackageDefinition(packageDefinition).messagePackage;

// instantiate the server
const server = new grpc.Server();

// Implement the service methods
function echoImplementation(call, callback) {
  const resMessage = `Echo: [${call.request.message}]`;
  callback(null, { message: resMessage  });
}

// add the service to the server
server.addService(echoProto.EchoService.service, {
  echo: echoImplementation,
});

// bind service to port
server.bindAsync(
  `${ipAddress}:${port}`,
  grpc.ServerCredentials.createInsecure(),
  (error, port) => {
    if (error) {
      console.error("Error binding the server:", error);
      return;
    }
    console.log(`Server running. Listening on port ${port}.`);
    server.start();
  }
);
