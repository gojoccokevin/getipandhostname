import socket
##ginamit para maimport ang socket module.
##Socket API magagamit pag nag online imbes na local lang

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
##used AF_INET for IPv4
##used SOCK_STREAM kasi streaming socket siya

s.connect((socket.gethostname(), 1234))
##gets the address of the client and connects to the server

while True:
    msg = s.recv(1024)
    print(msg.decode("utf-8"))
##when client connects successfully to the server, it receives the message encrypted in utf-8
##it then decrypts and displays it