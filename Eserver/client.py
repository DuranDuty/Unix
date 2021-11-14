import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 2000))

print(client.recv(2048).decode('utf-8'))
try:
        while True:
            client.send(input('Сообщение на сервер:\n').encode('utf-8'))
            data = client.recv(2048).decode('utf-8')


            if data.lower() == 'exit':
                print('Выход')
                client.send('Пользователь отключен\n'.encode('utf-8'))
                client.shutdown(socket.SHUT_WR)
                exit()

            if data:
                print('\nДанные от сервера:')
                print(data, end='\n\n')
except KeyboardInterrupt:
    client.shutdown(socket.SHUT_WR)