import socket
import threading

clients = []
nicknames = []

def broadcast(message, sender=None):
    for client in clients:
        if client != sender:  # Не отправляем сообщение отправителю
            try:
                client.send(message.encode('utf-8'))
            except:
                # Если отправка не удалась, удаляем клиента
                index = clients.index(client)
                clients.remove(client)
                client.close()
                nickname = nicknames[index]
                broadcast(f'{nickname} покинул чат!'.encode('utf-8'))
                nicknames.remove(nickname)

def handle_client(client):
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message.startswith('/nick'):
                # Обработка смены ника
                new_nick = message.split(' ', 1)[1]
                index = clients.index(client)
                old_nick = nicknames[index]
                nicknames[index] = new_nick
                broadcast(f'{old_nick} сменил ник на {new_nick}')
            else:
                broadcast(message, sender=client)
        except:
            # Удаляем клиента при ошибке
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} покинул чат!')
            nicknames.remove(nickname)
            break

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 5555))
    server.listen()
    print("Сервер чата запущен на localhost:5555")

    while True:
        client, address = server.accept()
        print(f"Подключение от {str(address)}")

        # Запрашиваем никнейм
        client.send('NICK'.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        
        nicknames.append(nickname)
        clients.append(client)

        print(f"Никнейм клиента: {nickname}")
        broadcast(f"{nickname} присоединился к чату!")
        client.send('Подключение к серверу успешно!'.encode('utf-8'))

        # Запускаем поток для обработки клиента
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

if __name__ == "__main__":
    start_server()