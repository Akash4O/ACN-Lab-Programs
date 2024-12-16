# File Transfer System

## Overview

This is a simple client-server file transfer application implemented in both Python and Java. The system allows a client to request and receive files from a server running on localhost.

## Features

- Supports file transfer over a socket connection
- Checks file existence before transfer
- Sends file size information
- Transfers files in chunks
- Works with text and binary files

## Requirements

### Python Version
- Python 3.x
- `socket` module (built-in)
- `os` module (built-in)

### Java Version
- Java 8 or later
- No external libraries required

## Python Usage

### Server
1. Save the server script as `server.py`
2. Run the server:
   ```
   python server.py
   ```
3. The server will start listening on `localhost:12345`

### Client
1. Save the client script as `client.py`
2. Run the client:
   ```
   python client.py
   ```
3. Enter the filename when prompted

## Java Usage

### Compilation
```bash
javac FileServer.java
javac FileClient.java
```

### Running
1. Start the server:
   ```
   java FileServer
   ```
2. In another terminal, run the client:
   ```
   java FileClient
   ```
3. Enter the filename when prompted

## Example Workflow

1. Ensure the server is running
2. In the client, enter a filename that exists in the server's directory
3. The file will be transferred and saved as `received_[filename]`
4. The file contents will be displayed in the console

## Limitations

- Only works on localhost
- No authentication or encryption
- Limited error handling
- Transfers files synchronously

## Potential Improvements

- Add support for remote hosts
- Implement file transfer resume functionality
- Add progress bar for large file transfers
- Implement authentication
- Add support for multiple simultaneous transfers

## License

[Choose an appropriate license, e.g., MIT, Apache 2.0]

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.