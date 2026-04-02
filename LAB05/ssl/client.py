import socket
import ssl
import threading

# Thông tin server
server_address = ('localhost', 12345)

def receive_data(ssl_socket):
    try:
        while True:
            data = ssl_socket.recv(1024)
            if not data:
                break
            # Sử dụng \r để ghi đè lên dòng "Nhập tin nhắn" đang chờ
            print(f"\nNhận: {data.decode('utf-8')}")
            print("Nhập tin nhắn: ", end="", flush=True)
    except:
        pass
    finally:
        print("\nKết nối từ server đã bị ngắt.")

# 1. Tạo socket client thông thường
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. Thiết lập SSL Context
context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)

# --- PHẦN SỬA LỖI QUAN TRỌNG ---
context.check_hostname = False       # Tắt kiểm tra hostname trước
context.verify_mode = ssl.CERT_NONE  # Sau đó mới có thể đặt CERT_NONE mà không bị lỗi
# ------------------------------

try:
    # 3. Bọc socket và kết nối
    ssl_socket = context.wrap_socket(client_socket, server_hostname='localhost')
    ssl_socket.connect(server_address)
    print("--- Đã kết nối bảo mật tới Server ---")

    # 4. Tạo luồng nhận dữ liệu
    receive_thread = threading.Thread(target=receive_data, args=(ssl_socket,), daemon=True)
    receive_thread.start()

    # 5. Vòng lặp gửi tin nhắn
    while True:
        message = input("Nhập tin nhắn: ")
        if message.lower() == 'exit':
            break
        if message.strip(): # Chỉ gửi nếu có nội dung
            ssl_socket.send(message.encode('utf-8'))

except Exception as e:
    print(f"Lỗi kết nối: {e}")

finally:
    ssl_socket.close()
    print("Đã đóng kết nối.")