import socket

def client():
    # Создаем TCP/IP сокет
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Подключаемся к серверу
    server_address = ('localhost', 12345)
    print(f"Подключаемся к серверу {server_address[0]}:{server_address[1]}")
    client_socket.connect(server_address)
    
    try:
        # Отправляем сообщение серверу
        message = "Hello, server"
        client_socket.sendall(message.encode())
        print(f"Отправлено серверу: {message}")
        
        # Получаем ответ от сервера
        data = client_socket.recv(1024)
        print(f"Получено от сервера: {data.decode()}")
        
    finally:
        # Закрываем соединение
        client_socket.close()
        print("Соединение с сервером закрыто")

if __name__ == "__main__":
    client()