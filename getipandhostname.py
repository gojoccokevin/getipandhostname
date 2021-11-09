import socket
##ginamit para maimport ang socket module.
##Socket API magagamit pag nag online imbes na local lang

hn = socket.gethostname()
##socket.gethostname() function ng socket na kinukuha ang computer name or
##website name depende kung nirun mo sa online compiler o sa terminal

ip = socket.gethostbyname(hn)
##socket.gethostbyname() function sa socket na kinukuha ang ipv4 address ng
##computer or website depende kung nirun mo sa online compiler o sa terminal

print("Hostname without format: {hn}") ##No formatting, displays as is
print("IPv4 Address without format: {ip}") ##No formatting, displays as is
print(f"Hostname: {hn}") ##With formatting, displays the value of hn
print(f"IPv4 Address: {ip}") ##With formatting, displays the value of ip