import socket
import threading

print(1)
sock = socket.socket()
sock.connect(('', 9090))


def proc_input():
    msg = ''
    while msg != 'exit':
        msg = input('введите сообщение: ')
        sock.send(msg.encode())


def proc_output():
    while True:
        data = sock.recv(1024)
        print(data.decode())
        if data.decode() == 'exit':
            break


p1 = threading.Thread(target=proc_input, name="input", args=[])
p2 = threading.Thread(target=proc_output, name="input", args=[])

p2.start()
p1.start()
