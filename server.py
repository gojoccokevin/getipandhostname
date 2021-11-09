import socket
##ginamit para maimport ang socket module.
##Socket API magagamit pag nag online imbes na local lang

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
##used AF_INET for IPv4
##used SOCK_STREAM kasi streaming socket siya

s.bind((socket.gethostname(), 1234))
## binds a tuple containing an ip and a port number to the server socket

s.listen(5);
## listens to connections 

while True:
    client, ip = s.accept()
    print(f"Connection from {ip} has been established")
    client.send(bytes("Welcome to the server!", "utf-8"))
##whenever a client connects to the server it will send a message in utf-8 format to the client while displaying
##in the server the ip address of the client