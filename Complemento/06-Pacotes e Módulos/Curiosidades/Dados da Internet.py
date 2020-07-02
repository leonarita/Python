import os
import socket

hostname = socket.gethostname()
ip_adress = socket.gethostbyname(hostname)

print(f"\n\nHostname: {hostname}")
print(f"IP Adress: {ip_adress}")

os.system('cmd /k "ping localhost"')