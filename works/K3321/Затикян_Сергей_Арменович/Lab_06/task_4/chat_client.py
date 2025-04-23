import socket
import threading

def receive_messages(client):
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'NICK':
                nickname = input("Введите ваш никнейм: ")
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            print("Ошибка соединения с сервером!")
            client.close()
            break

def write_messages(client, nickname):
    while True:
        message = input('')
        if message.startswith('/nick'):
            # Команда для смены ника
            client.send(f'/nick {message[6:]}'.encode('utf-8'))
        else:
            full_message = f'{nickname}: {message}'
            client.send(full_message.encode('utf-8'))

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 5555))

    # Получаем никнейм
    nickname = None
    while nickname is None:
        message = client.recv(1024).decode('utf-8')
        if message == 'NICK':
            nickname = input("Введите ваш никнейм: ")
            client.send(nickname.encode('utf-8'))
        else:
            print(message)

    # Запускаем потоки для приема и отправки сообщений
    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    receive_thread.start()

    write_thread = threading.Thread(target=write_messages, args=(client, nickname))
    write_thread.start()

if __name__ == "__main__":
    print("Подключение к чату...")
    start_client()