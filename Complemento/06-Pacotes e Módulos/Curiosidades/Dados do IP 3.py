import socket

hostname = input("Enter hostname: ")
ip = socket.gethostbyname(hostname)
print(f'IP Address: {ip}')