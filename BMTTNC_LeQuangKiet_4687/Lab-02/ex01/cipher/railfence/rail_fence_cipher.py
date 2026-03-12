class RailFenceCipher:
    def __init__(self):
        pass

    def rail_fence_encrypt(self, plain_text, num_rails):
        if num_rails <= 1: return plain_text
        
        rails = [[] for _ in range(num_rails)]
        rail_index = 0
        direction = 1
        
        for char in plain_text:
            rails[rail_index].append(char)
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction
            
        # SỬA: Đưa dòng này ra ngoài vòng lặp for
        cipher_text = ''.join(''.join(rail) for rail in rails)
        return cipher_text

    def rail_fence_decrypt(self, cipher_text, num_rails):
        if num_rails <= 1 or not cipher_text:
            return cipher_text
        
        # Bước 1: Xác định cấu trúc zigzag để biết mỗi hàng có bao nhiêu chữ
        rail_lengths = [0] * num_rails
        rail_index = 0
        direction = 1
        for _ in cipher_text:
            rail_lengths[rail_index] += 1
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction # Lệnh này phải nằm ngoài if/elif
            
        # Bước 2: Chia chuỗi cipher_text vào các hàng dựa trên độ dài đã tính
        rails = []
        start = 0
        for length in rail_lengths:
            # Chuyển thành list để có thể pop(0) lấy ký tự ra
            rails.append(list(cipher_text[start:start + length]))
            start += length
            
        # Bước 3: Thu hoạch ký tự theo hình zigzag để tái tạo bản rõ
        plain_text = ""
        rail_index = 0
        direction = 1
        
        for _ in range(len(cipher_text)):
            if rails[rail_index]:
                plain_text += rails[rail_index].pop(0)
            
            # Cập nhật hướng đi cho vòng lặp kế tiếp
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction # Luôn cập nhật chỉ số hàng
            
        return plain_text