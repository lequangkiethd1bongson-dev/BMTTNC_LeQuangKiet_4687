from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os

# Import các lớp Cipher từ folder cipher của bạn
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.playfair import PlayFairCipher
from cipher.railfence import RailFenceCipher
from cipher.transposition.transposition_cipher import TranspositionCipher

base_dir = os.path.abspath(os.path.dirname(__file__))
# Kết nối đến thư mục cipher/temple
template_path = os.path.join(base_dir, 'cipher', 'temple')
app = Flask(__name__, template_folder=template_path)
CORS(app)
# Khởi tạo các đối tượng cipher
caesar_cipher = CaesarCipher()
vigenere_cipher = VigenereCipher() 
playfair_cipher = PlayFairCipher()
transposition_cipher = TranspositionCipher()
railfence_cipher = RailFenceCipher()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<page>.html')
def serve_html(page):
    return render_template(f'{page}.html')

# --- ROUTES API XỬ LÝ MÃ HÓA ---

# Caesar API
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

# Vigenere API
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

# Playfair API
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

# Transposition API
@app.route('/api/transposition/encrypt', methods=['POST'])
def transposition_encrypt():
    data = request.get_json() or {}
    plain_text = data.get('plain_text', "")
    key = int(data.get('key', 0))
    encrypted_text = transposition_cipher.encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/transposition/decrypt', methods=['POST'])
def transposition_decrypt():
    data = request.get_json() or {}
    cipher_text = data.get('cipher_text', "")
    key = int(data.get('key', 0))
    decrypted_text = transposition_cipher.decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

# Rail Fence API
@app.route('/api/railfence/encrypt', methods=['POST'])
def railfence_encrypt():
    data = request.get_json() or {}
    plain_text = data.get('plain_text', "")
    key = int(data.get('key', 0))
    encrypted_text = railfence_cipher.rail_fence_encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/railfence/decrypt', methods=['POST'])
def railfence_decrypt():
    data = request.get_json() or {}
    cipher_text = data.get('cipher_text', "")
    key = int(data.get('key', 0))
    decrypted_text = railfence_cipher.rail_fence_decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

if __name__ == "__main__":
    # Chạy server tại port 1234
    app.run(host="0.0.0.0", port=1234, debug=True)