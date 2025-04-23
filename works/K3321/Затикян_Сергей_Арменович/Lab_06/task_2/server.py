import socket

def calculate_parallelogram_area(base, height):
    try:
        return float(base) * float(height)
    except ValueError:
        return None

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
            data = connection.recv(1024).decode()
            print(f"Получено от клиента: {data}")
            
            # Обрабатываем запрос
            params = data.split(',')
            if len(params) == 2:
                base, height = params
                area = calculate_parallelogram_area(base, height)
                if area is not None:
                    response = f"Площадь параллелограмма: {area}"
                else:
                    response = "Ошибка: неверные параметры"
            else:
                response = "Ошибка: требуется два параметра (основание и высота)"
            
            # Отправляем ответ клиенту
            connection.sendall(response.encode())
            print(f"Отправлено клиенту: {response}")
            
        finally:
            # Закрываем соединение
            connection.close()
            print("Соединение с клиентом закрыто")

if __name__ == "__main__":
    server()