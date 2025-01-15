import hashlib
import time


class Block:
    def __init__(self, index, timestamp, data, previous_hash=""):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        # Calculate the SHA-256 hash of the block
        block_string = (
            f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}"
        )
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine_block(self, difficulty):
        # Continue to adjust the nonce until the hash has the required number of leading zeros
        target = "0" * difficulty
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()
            print(f"Nonce: {self.nonce}, Hash: {self.hash}")
        print(f"Block mined: {self.hash}")


class Blockchain:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        # Create the first block in the blockchain
        genesis_block = Block(0, time.time(), "Genesis Block", "0")
        genesis_block.mine_block(self.difficulty)
        return genesis_block

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        # Set the previous hash of the new block to the hash of the latest block
        new_block.previous_hash = self.get_latest_block().hash
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)


# Create a blockchain with a difficulty of 4
my_blockchain = Blockchain(difficulty=4)

# Add blocks to the blockchain
print("Mining block 1...")
my_blockchain.add_block(Block(1, time.time(), {"amount": 4}))

print("Mining block 2...")
my_blockchain.add_block(Block(2, time.time(), {"amount": 10}))

# Print the blockchain
for block in my_blockchain.chain:
    print(
        f"Block {block.index} [Previous Hash: {block.previous_hash}, Hash: {block.hash}, Nonce: {block.nonce}, Data: {block.data}]"
    )
