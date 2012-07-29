import SocketServer

class TCPHandler(SocketServer.BaseRequestHandler) :
    
    def handle(self) :
        self.data = self.request.recv(1024).strip()
        print "{0} wrote:".format(self.client_address[0])
        print self.data
        self.request.send(self.data.upper())

if __name__ == "__main__" :
    HOST, PORT = "localhost", 9999

    server = SocketServer.TCPServer((HOST, PORT), TCPHandler)
    server.serve_forever()

