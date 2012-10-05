import SocketServer

import sys
sys.path.append("../")
sys.path.append("../batch/")
sys.path.append("../../")
sys.path.append("../../test/")
sys.path.append("../../test/evaluation")

import json

from batch import Service
from evaluation import BasicObj

class BatchHandler(SocketServer.BaseRequestHandler) :
    
    def handle(self) :
        self.data = self.request.recv(10240).strip()
        print "{0} wrote:".format(self.client_address[0])
        print self.data
        service = Service.Service(BasicObj.BasicObj(1000))
        print service.serve(self.data)
        #print BasicObj.BasicObj(1000).foo(1)
        #self.request.send("Batch 1.0 JSON 1.0\n")   # Header required
        self.request.send(json.dumps(service.serve(self.data)))

if __name__ == "__main__" :
    HOST, PORT = "localhost", 9825

    server = SocketServer.TCPServer((HOST, PORT), BatchHandler)
    print "Server start..."
    server.serve_forever()

