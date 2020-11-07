import socket
import cv2

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 1218
sock.connect((host, port))
sock.send(b"Hello from client")

# img = cv2.imread("Received File") 
with open("Received _File.png", "wb") as file:
    print("File open")
    print("receiving data...")
    while True:
        data = sock.recv(1024)
        print(f"data={data}")
        if not data:
            break
        file.write(data)
        # cv2.imwrite("file_anh.jpg", img)

print("Got the file")
sock.close()
print("Connection is close!")