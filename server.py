import socket
TCP_IP = '192.168.1.126'
TCP_PORT = 5005
BUFFER_SIZE = 20  # Normally 1024, but we want fast response
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
conn, addr = s.accept()
print 'Connection address:', addr
while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    print "Got a message!"
#    conn.send("Message")  # echo
conn.close()
