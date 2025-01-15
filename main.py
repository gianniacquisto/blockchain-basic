import hashlib
import time


class Block:
    def __init__(self, index, timestamp, data, previous_hash=""):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        # Calculate the SHA-256 hash of the block
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}"
        return hashlib.sha256(block_string.encode()).hexdigest()


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        # Create the first block in the blockchain
        return Block(0, time.time(), "Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        # Set the previous hash of the new block to the hash of the latest block
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)


# Create a blockchain
my_blockchain = Blockchain()

# Add blocks to the blockchain
my_blockchain.add_block(Block(1, time.time(), {"amount": 4}))
my_blockchain.add_block(Block(2, time.time(), {"amount": 10}))

# Print the blockchain
for block in my_blockchain.chain:
    print(
        f"Block {block.index} [Previous Hash: {block.previous_hash}, Hash: {block.hash}, Data: {block.data}]"
    )
