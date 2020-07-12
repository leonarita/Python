from socket import *
import threading
import sys
from playsound import playsound

FLAG = False


def send_to_server(clsock):
    global FLAG

    while True:
        if FLAG:
            break
        send_msg = input('')
        clsock.sendall(send_msg.encode())


def recv_from_server(clsock):
    global FLAG

    while True:
        data = clsock.recv(1024).decode()

        if data == 'q':
            print('Closing connection')
            FLAG = True
            break

        print('Server: ' + data)
        playsound('alert.wav')


def main():
    threads = []

    HOST = '192.168.56.1'
    PORT = 6789

    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.bind((HOST, PORT))

    print('Client is connected to a chat server!\n')

    t_rcv = threading.Thread(target=recv_from_server, args=(clientSocket,))
    t_send = threading.Thread(target=send_to_server, args=(clientSocket,))

    threads.append(t_rcv)
    threads.append(t_send)

    t_rcv.start()
    t_send.start()

    t_rcv.join()
    t_send.join()

    print('EXITING')
    sys.exit()


if __name__ == '__main__':
    main()