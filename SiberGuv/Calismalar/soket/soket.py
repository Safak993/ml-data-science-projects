from rich import print, panel, table                          #kütüpaneler
import socket                                                 #soket imporutlar

                                                                #socket nesnesi oluşturma (ipv4 ve tcp)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    #serverı tanımlar
                                                                #ip ve port bağlama
server.bind(('127.0.0.1', 12345))                             #server ip ve port
server.listen(1)                                              #server çalıştırma
print("[bold yellow][!] [/][bold blue]Sunucu Dinlemede...[/]") #sunucuyu anlatır hiakye gibi
# Bağlantı olduğu anda server.accept 2 şey döndürür
#1: client_socket: İstemciyle konuşmak için kullanacağın özel, yeni bir kanal.
#2: address: Bağlanan kişinin IP adresi ve portu.
client_socket, address = server.accept()                      #bağlantıyı kabul etme
print(f"[bold green][*] Bağlantı sağlandı: {address} [/]")    #bağlantıyı söyler
                                                                #veriyi alma
data = client_socket.recv(1024).decode('utf-8')               #serverda utf8 kullanılcakmış
print(f"[bold yellow][!] Gelen mesaj: {data} [/]")            #gelen mesajı gösterirMİŞ
                                                                #kapama
client_socket.close()                                         #bunu yazarken uykum geldi :P
server.close()                                                #serverı kapatıyo
