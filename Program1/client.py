import socket

def request_file(host='localhost', port=12345, filename=''):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    client_socket.send(filename.encode())
    response = client_socket.recv(1024).decode()
    
    if response.startswith('EXISTS'):
        file_size = int(response.split()[1])
        print(f"Receiving file: {filename} of size {file_size} bytes")
        
        with open('received_' + filename, 'wb') as f:
            bytes_received = 0
            while bytes_received < file_size:
                bytes_data = client_socket.recv(1024)
                f.write(bytes_data)
                bytes_received += len(bytes_data)

        print(f"File {filename} received successfully.")
        
        # Read and display file contents
        with open('received_' + filename, 'r', encoding='utf-8') as f:
            print("\n--- File Contents ---")
            print(f.read())
    else:
        print("File not found on server.")

    client_socket.close()

if __name__ == "__main__":
    filename_to_request = input("Enter the filename to request: ")
    request_file(filename=filename_to_request)