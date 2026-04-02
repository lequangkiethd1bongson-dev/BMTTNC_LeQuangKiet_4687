import socket
import ssl
import threading

# Thông tin server
server_address = ('localhost', 12345)

# Danh sách các client đã kết nối
clients = []

def handle_client(client_socket):
    # Thêm client vào danh sách
    clients.append(client_socket)
    
    try:
        print("Đã kết nối với:", client_socket.getpeername())
        
        # Nhận và gửi dữ liệu
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            print("Nhận:", data.decode('utf-8'))
            
            # Gửi dữ liệu đến tất cả các client khác (Broadcast)
            # Dùng list(clients) để tránh lỗi khi danh sách thay đổi trong lúc lặp
            for client in list(clients):
                if client != client_socket:
                    try:
                        client.send(data)
                    except:
                        if client in clients:
                            clients.remove(client)
    except Exception as e:
        print(f"Lỗi khi xử lý client: {e}")
    finally:
        print("Đã ngắt kết nối với một client.")
        if client_socket in clients:
            clients.remove(client_socket)
        client_socket.close()

# 1. Tạo SSL context TRƯỚC khi vào vòng lặp để tối ưu
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
try:
    context.load_cert_chain(certfile="./certificates/server-cert.crt", 
                           keyfile="./certificates/server-key.key")
except FileNotFoundError:
    print("Lỗi: Không tìm thấy file chứng chỉ trong thư mục ./certificates/")
    exit()

# 2. Tạo socket server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Cho phép chạy lại server nhanh
server_socket.bind(server_address)
server_socket.listen(5)

print("Server đang chờ kết nối bảo mật...")

# 3. Lắng nghe các kết nối
while True:
    try:
        client_socket, client_address = server_socket.accept()
        
        # Thiết lập kết nối SSL (Bọc socket)
        ssl_socket = context.wrap_socket(client_socket, server_side=True)
        
        # --- PHẦN SỬA LỖI ---
        # Sử dụng threading.Thread (thay vì threading.threading.Thread)
        client_thread = threading.Thread(target=handle_client, args=(ssl_socket,))
        # --------------------
        
        client_thread.daemon = True # Đảm bảo luồng tắt khi server tắt
        client_thread.start()
        
    except ssl.SSLError as e:
        print(f"Lỗi SSL (có thể do client không dùng SSL): {e}")
    except Exception as e:
        print(f"Lỗi kết nối: {e}")