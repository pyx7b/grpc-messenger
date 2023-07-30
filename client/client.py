import grpc
import Message_pb2 as pb2
import Message_pb2_grpc as pb2_grpc
import datetime
import app_logger

# Set up the logger
logger = app_logger.setup_logger()

def run_grpc_client():
    server = '0.0.0.0'
    port = '50051'
    try:
        channel = grpc.insecure_channel(f'{server}:{port}')
        stub = pb2_grpc.EchoServiceStub(channel)
        logger.info(f'Connected to server at {server}:{port}')
    except Exception as e:
        logger.error(f'Error connecting to server: {e}')
        return

    # Make a request to the server
    message = "This is a test"
    request = pb2.EchoRequest(message=message)
    response = stub.echo(request)

    # Handle the response
    logger.info(f'Server response: {message}')

    # Close the gRPC channel when you are done
    channel.close()
    logger.info('gRPC channel closed')


if __name__ == "__main__":
    run_grpc_client()
