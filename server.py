import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('127.0.0.1', 2000))
while True:
    server.listen(1)

    client_socket, address = server.accept()
    print(f'Пользователь подключен')

    client_socket.send('Вы подключены к серверу!'.encode('utf-8'))
    while True:
        try:
            data = client_socket.recv(2048).decode('utf-8')
        except OSError:
            data = None

        if data:
            print('\nПолученные данные от пользователя:')
            print(data)
        msg = input('\nCообщение клиенту:\n').encode('utf-8')
        client_socket.send(msg)
        if msg.lower() == 'exit'.encode('utf-8'):

            server.shutdown(socket.SHUT_WR)
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            server.bind(('127.0.0.1', 2000))
            break


