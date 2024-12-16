import socket

def start_client(host='localhost', port=12345):
    with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as client_socket:    
        while True:
            message = input("Enter a message (or 'exit' to quit):")
            if message.lower() == 'exit':
                print("Exiting...")
                break

            client_socket.sendto(message.encode(), (host,port))
            print(f"Sent message to {host} : {port}")

            response, server_address = client_socket.recvfrom(1024)
            print(f"Received response from {server_address} : {response.decode()}")

if __name__ == "__main__":
    start_client()