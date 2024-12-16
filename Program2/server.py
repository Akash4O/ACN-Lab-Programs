import socket

def start_server(host='localhost', port=12345):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
        server_socket.bind((host,port))
        print(f"Server listening on {host}:{port}")

        while True:
            message,client_address = server_socket.recvfrom(1024)
            decoded_message = message.decode()
            print(f"Received message from {client_address}:{decoded_message}")

            response_length = len(decoded_message)
            response_message = decoded_message.upper()
            response  = f"Length: {response_length}, Message: {response_message}"

            server_socket.sendto(response.encode(),client_address)

if __name__ == "__main__":
    start_server()