import socket

def client():
    # Создаем TCP/IP сокет
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Подключаемся к серверу (порт 80 - стандартный HTTP)
    server_address = ('localhost', 80)
    print(f"Подключаемся к HTTP-серверу {server_address[0]}:{server_address[1]}")
    
    try:
        client_socket.connect(server_address)
        
        # Отправляем HTTP-запрос GET /
        http_request = (
            "GET / HTTP/1.1\r\n"
            "Host: localhost\r\n"
            "Connection: close\r\n"
            "\r\n"
        )
        client_socket.sendall(http_request.encode())
        print("HTTP-запрос отправлен")
        
        # Получаем ответ от сервера
        response = b""
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            response += data
        
        # Декодируем ответ (первые 1024 байта для примера)
        decoded_response = response.decode('utf-8', errors='ignore')
        print("\nПолучен ответ от сервера:")
        print(decoded_response[:1024])  # Выводим только начало ответа
        
        # Сохраняем HTML в файл
        with open("received_page.html", "w", encoding="utf-8") as f:
            # Находим начало HTML-кода после заголовков
            html_start = decoded_response.find("\r\n\r\n") + 4
            if html_start > 0:
                f.write(decoded_response[html_start:])
                print("\nHTML-страница сохранена в файл 'received_page.html'")
        
    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        # Закрываем соединение
        client_socket.close()
        print("Соединение с сервером закрыто")

if __name__ == "__main__":
    client()