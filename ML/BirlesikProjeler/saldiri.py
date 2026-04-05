import socket
import time
hedef = "127.0.0.1"
port = 9999

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Saldırı başladı... Durdurmak için Ctrl+C")
while True:
    sock.sendto(b"x" * 10, (hedef, port))
    time.sleep(0.060)