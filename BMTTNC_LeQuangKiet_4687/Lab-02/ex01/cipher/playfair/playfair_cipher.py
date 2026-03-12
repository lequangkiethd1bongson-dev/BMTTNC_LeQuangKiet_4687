class PlayFairCipher:
    def __init__(self):
        pass
    
    def create_matrix_key(self, key):
        key = key.upper().replace("J", "I")
        key = "".join(dict.fromkeys(key))
        
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        matrix = list(key)
        
        for letter in alphabet:
            if letter not in matrix:
                matrix.append(letter)
                
        playfair_matrix = [matrix[i:i+5] for i in range(0, 25, 5)]
        return playfair_matrix
    
    def tachcap_plaintext(self, text):
        text = text.upper().replace("J", "I").replace(" ", "")
        pairs = []
        i = 0
        
        while i < len(text):
            a = text[i]
            if i + 1 < len(text):
                b = text[i + 1]
                if a == b:
                    pairs.append(a + "X")
                    i += 1
                else:
                    pairs.append(a + b)
                    i += 2
            else:
                pairs.append(a + "X")
                i += 1
        return pairs
    
    def vitri_letter(self, matrix, letter):
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == letter:
                    return row, col
        return None, None 
                
    def playfair_encrypt(self, plain_text, matrix):
        pairs = self.tachcap_plaintext(plain_text)
        encrypted_text = ""
        
        for pair in pairs:
            row1, col1 = self.vitri_letter(matrix, pair[0])
            row2, col2 = self.vitri_letter(matrix, pair[1])
            
            if row1 == row2:
                encrypted_text += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:
                encrypted_text += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
            else:
                encrypted_text += matrix[row1][col2] + matrix[row2][col1]
        return encrypted_text
    
    def playfair_decrypt(self, cipher_text, matrix):
        cipher_text = cipher_text.upper().replace(" ", "")
        decrypted_text = ""
        
        for i in range(0, len(cipher_text), 2):
            pair = cipher_text[i:i+2]
            row1, col1 = self.vitri_letter(matrix, pair[0])
            row2, col2 = self.vitri_letter(matrix, pair[1])
            
            if row1 == row2:
                decrypted_text += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
            elif col1 == col2:
                decrypted_text += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
            else:
                decrypted_text += matrix[row1][col2] + matrix[row2][col1]
       
        final_text = ""
        i = 0
        while i < len(decrypted_text):
           
            if i + 2 < len(decrypted_text) and decrypted_text[i] == decrypted_text[i+2] and decrypted_text[i+1] == 'X':
                final_text += decrypted_text[i] + decrypted_text[i+2]
                i += 3 
            else:
                final_text += decrypted_text[i]
                i += 1
        
        if final_text.endswith("X"):
            final_text = final_text[:-1]
            
        return final_text