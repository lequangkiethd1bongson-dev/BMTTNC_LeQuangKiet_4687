from block import Block
import hashlib
import time

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        # Tạo khối sơ khai (Genesis Block)
        self.create_block(proof=1, previous_hash='0')

    def create_block(self, proof, previous_hash):
        block = Block(
            len(self.chain) + 1,
            previous_hash,
            time.time(),
            self.current_transactions,
            proof
        )
        self.current_transactions = [] # Reset danh sách giao dịch sau khi đóng khối
        self.chain.append(block)
        return block

    def get_previous_block(self):
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        while not check_proof:
            # Giải bài toán hash: tìm giá trị sao cho 4 chữ số đầu của hash là '0000'
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1
        return new_proof

    def add_transaction(self, sender, receiver, amount):
        self.current_transactions.append({
            'sender': sender,
            'receiver': receiver,
            'amount': amount
        })
        return self.get_previous_block().index + 1

    def is_chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]
            # Kiểm tra tính liên kết: hash khối trước có khớp với previous_hash khối này không
            if block.previous_hash != previous_block.hash:
                return False
            
            previous_proof = previous_block.proof
            proof = block.proof
            hash_operation = hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest()
            
            # Kiểm tra xem hash có hợp lệ (bắt đầu bằng '0000') không
            if hash_operation[:4] != '0000':
                return False
            
            previous_block = block
            block_index += 1
        return True