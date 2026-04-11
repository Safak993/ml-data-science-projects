import socket, time                                                  #buradayım ahahahahah
while 1 < 2:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     #cıliyent oluşturur
    client.connect(('127.0.0.1', 65432))                           #clinet ip
    client.send("TcpSaldiriOmg".encode('utf-8'))                   #sunucuyu selamlar
    client.close()                                                 #cılienti kapatır
    time.sleep(0.1)