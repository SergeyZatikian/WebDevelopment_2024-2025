import socket

def server():
    # Создаем TCP/IP сокет
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Привязываем сокет к порту
    server_address = ('localhost', 12345)
    print(f"Сервер запущен на {server_address[0]}:{server_address[1]}")
    server_socket.bind(server_address)
    
    # Слушаем входящие соединения
    server_socket.listen(1)
    
    while True:
        print("Ожидание подключения клиента...")
        connection, client_address = server_socket.accept()
        
        try:
            print(f"Подключен клиент: {client_address}")
            
            # Получаем данные от клиента
            data = connection.recv(1024)
            print(f"Получено от клиента: {data.decode()}")
            
            # Отправляем ответ клиенту
            response = "Hello, client"
            connection.sendall(response.encode())
            print(f"Отправлено клиенту: {response}")
            
        finally:
            # Закрываем соединение
            connection.close()
            print("Соединение с клиентом закрыто")

if __name__ == "__main__":
    server()