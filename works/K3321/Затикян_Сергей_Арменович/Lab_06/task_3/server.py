import socket

def load_html_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return "<html><body><h1>Error: File not found</h1></body></html>"

def server():
    # Создаем TCP/IP сокет
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Привязываем сокет к порту 80 (стандартный HTTP-порт)
    server_address = ('localhost', 80)
    print(f"HTTP-сервер запущен на {server_address[0]}:{server_address[1]}")
    server_socket.bind(server_address)
    
    # Слушаем входящие соединения
    server_socket.listen(1)
    
    while True:
        print("Ожидание подключения клиента...")
        connection, client_address = server_socket.accept()
        
        try:
            print(f"Подключен клиент: {client_address}")
            
            # Получаем HTTP-запрос (но в этом примере мы его не обрабатываем)
            data = connection.recv(1024)
            print(f"Получен запрос:\n{data.decode()}")
            
            # Загружаем HTML-страницу из файла
            html_content = load_html_file("index.html")
            
            # Формируем HTTP-ответ
            http_response = (
                "HTTP/1.1 200 OK\r\n"
                "Content-Type: text/html; charset=utf-8\r\n"
                f"Content-Length: {len(html_content)}\r\n"
                "\r\n"
                f"{html_content}"
            )
            
            # Отправляем ответ клиенту
            connection.sendall(http_response.encode('utf-8'))
            print("HTML-страница отправлена клиенту")
            
        finally:
            # Закрываем соединение
            connection.close()
            print("Соединение с клиентом закрыто")

if __name__ == "__main__":
    server()