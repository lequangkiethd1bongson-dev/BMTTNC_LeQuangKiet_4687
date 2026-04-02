from flask import Flask, request, jsonify 
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.playfair import PlayFairCipher
from cipher.railfence import RailFenceCipher
from cipher.transposition.transposition_cipher import TranspositionCipher

app = Flask(__name__)

# Khởi tạo các đối tượng cipher
caesar_cipher = CaesarCipher()
vigenere_cipher = VigenereCipher() 
playfair_cipher = PlayFairCipher()
transposition_cipher = TranspositionCipher()
railfence_cipher = RailFenceCipher()

# --- CAESAR ---
@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    data = request.json or {}
    plain_text = data.get('plain_text', "")
    key = int(data.get('key', 0))
    encrypted_text = caesar_cipher.encrypt_text(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})

@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    data = request.json or {}
    cipher_text = data.get('cipher_text', "")
    key = int(data.get('key', 0))
    decrypted_text = caesar_cipher.decrypt_text(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})

# --- VIGENERE ---
@app.route("/api/vigenere/encrypt", methods=["POST"])
def vigenere_encrypt():
    data = request.json or {}
    plain_text = data.get('plain_text', "")
    key = data.get('key', "") 
    encrypted_text = vigenere_cipher.encrypt_text(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route("/api/vigenere/decrypt", methods=["POST"])
def vigenere_decrypt():
    data = request.json or {}
    cipher_text = data.get('cipher_text', "")
    key = data.get('key', "") 
    decrypted_text = vigenere_cipher.decrypt_text(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

# --- PLAYFAIR ---
@app.route("/api/playfair/creatematrix", methods=['POST'])
def playfair_creatematrix():
    data = request.json or {}
    key = data.get('key', "") 
    result_matrix = playfair_cipher.create_matrix_key(key) 
    return jsonify({'playfair_matrix': result_matrix})

@app.route("/api/playfair/encrypt", methods=["POST"]) 
def playfair_encrypt():
    data = request.json or {}
    plain_text = data.get('plain_text', "") 
    key = data.get('key', "")
    matrix = playfair_cipher.create_matrix_key(key) 
    encrypted_text = playfair_cipher.playfair_encrypt(plain_text, matrix) 
    return jsonify({'encrypted_text': encrypted_text})

@app.route("/api/playfair/decrypt", methods=["POST"])
def playfair_decrypt():
    data = request.json or {}
    cipher_text = data.get('cipher_text', "")
    key = data.get('key', "")
    matrix = playfair_cipher.create_matrix_key(key) 
    decrypted_text = playfair_cipher.playfair_decrypt(cipher_text, matrix) 
    return jsonify({'decrypted_text': decrypted_text})

@app.route('/api/transposition/encrypt', methods=['POST'])
def transposition_encrypt():
    data = request.get_json() or {}
    # Kiểm tra kỹ: Bạn dùng 'plain_text' hay 'plaintext'?
    text = data.get('plain_text', "") 
    key_raw = data.get('key')
    
    # Nếu key không tồn tại hoặc không phải số, hàm sẽ bị lỗi hoặc trả về rỗng
    if text == "" or key_raw is None:
        return jsonify({'error': 'Missing text or key', 'received': data}), 400
    
    key = int(key_raw)
    encrypted_text = transposition_cipher.encrypt(text, key)
    return jsonify({'encrypted_text': encrypted_text})
@app.route('/api/transposition/decrypt', methods=['POST'])
def transposition_decrypt():
    data = request.get_json() or {}
    cipher_text = data.get('cipher_text', "")
    key = int(data.get('key', 0))
    decrypted_text = transposition_cipher.decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

# --- RAIL FENCE ---
@app.route('/api/railfence/encrypt', methods=['POST'])
def railfence_encrypt(): 
    data = request.get_json() or {}
    plain_text = data.get('plain_text', "")
    key = int(data.get('key', 0))
    encrypted_text = railfence_cipher.rail_fence_encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/railfence/decrypt', methods=['POST'])
def railfence_decrypt(): # Đã đổi tên hàm và sửa logic gọi hàm decrypt
    data = request.get_json() or {}
    cipher_text = data.get('cipher_text', "")
    key = int(data.get('key', 0))
    # SỬA LỖI: Gọi đúng hàm rail_fence_decrypt
    decrypted_text = railfence_cipher.rail_fence_decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1234, debug=True)