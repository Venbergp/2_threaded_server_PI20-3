import socket
import threading

sock = socket.socket()
sock.bind(('', 9090))

sock.listen(1)

conn, addr = sock.accept()

msg = ''

while True:
    data = conn.recv(1024)
    if not data:
        break
    msg += data.decode()
    conn.send(data)


print(msg)

conn.close()
