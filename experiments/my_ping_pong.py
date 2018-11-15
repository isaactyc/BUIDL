import socketserver, socket, sys


host = "127.0.0.1"
port = 10000
address = (host, port)

class MyTCPServer(socketserver.TCPServer):
    allow_reuse_address = True

class TCPHandler(socketserver.BaseRequestHandler):
    #whenever it gets some data, it will execute function 'handle'
    def handle(self):
        message = self.request.recv(10)
        print(f"got a message: {message}")
        if message == b"ping":
            self.request.sendall(b"pong\n")

def serve():
    #instantiate a server using this handler
    server = MyTCPServer(address, TCPHandler)
    server.serve_forever()

def ping():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(address)
    sock.sendall(b"ping")
    data = sock.recv(10)
    print(f"Received {data.decode()}")

#if the dunder, name is equal to main, that means the file
# is executed on the command line, and the user
#is not importing it from somewhere else
if __name__ == "__main__":
    command = sys.argv[1]
    if command == "serve":
        serve()
    elif command == "ping":
        ping()
    else:
        print("invalid message")
