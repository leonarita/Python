import socket

s = socket.socket()
port = 12345
s.bind(('', port))
print('Socket binded to ', port)

s.listen(5)
print("Socket is listening")

while True:
    c, addr = s.accept()
    print('Got connection from', addr)
    c.send('Connected')
    c.close()