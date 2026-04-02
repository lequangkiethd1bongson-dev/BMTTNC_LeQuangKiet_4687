import sys
from PIL import Image

def encode_image(image_path, message):
    # Mở hình ảnh
    img = Image.open(image_path)
    width, height = img.size
    
    # Chuyển đổi thông điệp sang dạng nhị phân (8-bit cho mỗi ký tự)
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    # Thêm một chuỗi bit đặc biệt để đánh dấu kết thúc thông điệp
    binary_message += '1111111111111110' 
    
    data_index = 0
    
    # Duyệt qua từng pixel của ảnh theo hàng và cột
    for row in range(height):
        for col in range(width):
            # Lấy giá trị màu của pixel (R, G, B)
            pixel = list(img.getpixel((col, row)))
            
            # Duyệt qua 3 kênh màu: Đỏ, Xanh lá, Xanh dương
            for color_channel in range(3):
                if data_index < len(binary_message):
                    # Thay đổi bit cuối cùng của giá trị màu thành bit của thông điệp
                    pixel[color_channel] = int(format(pixel[color_channel], '08b')[:-1] + binary_message[data_index], 2)
                    data_index += 1
            
            # Cập nhật lại pixel đã được giấu tin vào ảnh
            img.putpixel((col, row), tuple(pixel))
            
            # Nếu đã giấu hết thông điệp thì dừng lại
            if data_index >= len(binary_message):
                break
        if data_index >= len(binary_message):
            break

    # Lưu ảnh mới đã được chèn tin
    encoded_image_path = 'encoded_image.png'
    img.save(encoded_image_path)
    print("Steganography complete. Encoded image saved as", encoded_image_path)

def main():
    # Kiểm tra xem người dùng có nhập đủ tham số (đường dẫn ảnh và thông điệp) không
    if len(sys.argv) != 3:
        print("Usage: python encrypt.py <image_path> <message>")
        return

    image_path = sys.argv[1]
    message = sys.argv[2]
    encode_image(image_path, message)

if __name__ == "__main__":
    main()