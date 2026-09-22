import hashlib,time
class Block:
    def __init__(self, index, timestamp, data, prior_hash="0"):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.prior_hash = prior_hash
        self.hash = self.create_hash()
    def create_hash(self):
        block_string = f"{self.index}{self.timestamp}{self.data}{self.prior_hash}".encode()
        return hashlib.sha256(block_string).hexdigest()
    
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
    def create_genesis_block(self):
        return Block(1, time.strftime("%H:%M:%S", time.localtime()), "", "0")
    def get_last_block(self):
        return self.chain[-1]
    def add_block(self, data):
        last_block = self.get_last_block()
        new_index = last_block.index + 1
        new_timestamp = time.strftime("%H:%M:%S", time.localtime())
        new_block = Block(new_index, new_timestamp, data, last_block.hash)
        self.chain.append(new_block)
        return new_block
    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]
            if current.hash != current.create_hash():
                return False
            if current.prior_hash != previous.hash:
                return False
        return True
    def display_chain(self):
        for block in self.chain:
            print(
                f"Block index {block.index}\n"
                f" Block timestamp {block.timestamp}\n"
                f" Block data {block.data}\n"
                f" Prior hash {block.prior_hash}\n"
                f" Hash {block.hash}\n")
blockchain = Blockchain()
for i in range(3):
    data = f"transactions: Acc.A -> Acc.B = Rs.{1000 * (i + 1)}"
    block = blockchain.add_block(data)
print("Is chain valid?", blockchain.is_chain_valid())



import hashlib, time

class Block:
    def __init__(self, i, data, prev="0"):
        self.i = i
        self.time = time.strftime("%H:%M:%S")
        self.data = data
        self.prev = prev
        self.hash = self.make_hash()

    def make_hash(self):
        bs = f"{self.i}{self.time}{self.data}{self.prev}".encode()
        return hashlib.sha256(bs).hexdigest()


class Blockchain:
    def __init__(self):
        self.chain = [self.genesis()]

    def genesis(self):
        return Block(1, "")

    def add(self, data):
        last = self.chain[-1]
        self.chain.append(Block(last.i + 1, data, last.hash))

    def valid(self):
        for i in range(1, len(self.chain)):
            c, p = self.chain[i], self.chain[i-1]
            if c.hash != c.make_hash() or c.prev != p.hash:
                return False
        return True
    
    def display(self):
        for b in self.chain:
            print("\nBlock:", b.i)
            print("Time:", b.time)
            print("Data:", b.data)
            print("Previous:", b.prev)
            print("Hash:", b.hash)


bc = Blockchain()

for i in range(3):
    bc.add(f"A -> B = Rs.{1000*(i+1)}")

print("Valid:", bc.valid())



