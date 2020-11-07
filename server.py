import socket

ONE_CONNECTION_ONLY = (True)

port = 1218
host = socket.gethostname()
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((host, port))
server.listen(1)
print("File server starting....")

while True:
    conn, addr = server.accept()
    data = conn.recv(1024)

    file_name = 'pic.jpg'
    f = open(file_name, 'rb')
    l = f.read(1024)

    while l:
        conn.send(l)
        print('Sent', repr(l))
        l = f.read(1024)
    
    f.close()
    print("File sent complete!")
    conn.close()
    if ONE_CONNECTION_ONLY:
        break

server.close()

