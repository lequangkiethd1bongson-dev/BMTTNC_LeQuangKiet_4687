from blockchain import Blockchain

# 1. Khởi tạo một Blockchain mới
my_blockchain = Blockchain()

# 2. Thêm các giao dịch vào danh sách chờ
my_blockchain.add_transaction('Alice', 'Bob', 10)
my_blockchain.add_transaction('Bob', 'Charlie', 5)
my_blockchain.add_transaction('Charlie', 'Alice', 3)

# 3. Quá trình đào (Mining) một khối mới
# Lấy thông tin khối trước đó để làm cơ sở
previous_block = my_blockchain.get_previous_block()
previous_proof = previous_block.proof

# Tìm proof mới (Proof of Work)
new_proof = my_blockchain.proof_of_work(previous_proof)
previous_hash = previous_block.hash

# Thêm giao dịch thưởng cho người đào (Miner)
my_blockchain.add_transaction('Genesis', 'Miner', 1)

# Tạo khối mới và thêm vào chuỗi
new_block = my_blockchain.create_block(new_proof, previous_hash)

# 4. Hiển thị thông tin toàn bộ Blockchain
for block in my_blockchain.chain:
    print(f"Block #{block.index}")
    print("Timestamp:", block.timestamp)
    print("Transactions:", block.transactions)
    print("Proof:", block.proof)
    print("Previous Hash:", block.previous_hash)
    print("Hash:", block.hash)
    print("-" * 40)

# 5. Kiểm tra xem chuỗi Blockchain có hợp lệ không
print("Is Blockchain Valid:", my_blockchain.is_chain_valid(my_blockchain.chain))