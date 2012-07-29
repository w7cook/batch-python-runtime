import socket

HOST, PORT = "localhost", 9999

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

f = open('../batch/test')

try :
    sock.connect((HOST, PORT))
    sock.send(f.read() + '\n')

    received = sock.recv(4096)
finally :
    sock.close()

    print "Result is " + str(received)

