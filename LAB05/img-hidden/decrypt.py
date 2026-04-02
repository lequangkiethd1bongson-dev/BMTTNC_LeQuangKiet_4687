import sys
from PIL import Image

def decode_image(encoded_image_path):
    # Mở hình ảnh đã được mã hóa
    img = Image.open(encoded_image_path)
    width, height = img.size
    binary_message = ""

    # Duyệt qua từng pixel để trích xuất bit cuối cùng (LSB)
    for row in range(height):
        for col in range(width):
            pixel = img.getpixel((col, row))
            
            # Trích xuất bit từ 3 kênh màu R, G, B
            for color_channel in range(3):
                # format(..., '08b')[-1] lấy bit cuối cùng của giá trị màu
                binary_message += format(pixel[color_channel], '08b')[-1]

    # Chuyển đổi chuỗi nhị phân thành ký tự văn bản
    message = ""
    for i in range(0, len(binary_message), 8):
        # Lấy từng cụm 8 bit
        byte = binary_message[i:i+8]
        # Chuyển từ nhị phân sang số nguyên rồi sang ký tự ASCII
        char = chr(int(byte, 2))
        
        # Kết thúc thông điệp khi gặp dấu hiệu dừng (ký tự null hoặc theo logic code là '\0')
        # Lưu ý: Code trong ảnh dùng '\0' làm điểm dừng
        if char == '\0': 
            break
        message += char

    return message

def main():
    # Kiểm tra tham số dòng lệnh
    if len(sys.argv) != 2:
        print("Usage: python decrypt.py <encoded_image_path>")
        return

    encoded_image_path = sys.argv[1]
    decoded_message = decode_image(encoded_image_path)
    print("Decoded message:", decoded_message)

if __name__ == "__main__":
    main()