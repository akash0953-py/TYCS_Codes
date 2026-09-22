import hashlib,time

class Block:
    def __init__(self,i,data,prev_hash="0"):
        self.i = i
        self.time = time.strftime("%H:%M:%S")
        self.data = data
        self.prev_hash = prev_hash
        self.hash = self.create_hash()

    def create_hash(self):
        bs = f"{self.i}{self.time}{self.data}{self.prev_hash}".encode()
        return hashlib.sha256(bs).hexdigest()
    
class Blockchain:
    def __init__(self):
        self.chain = [self.genesis()]
    def genesis(self):
        return Block(1,"")
    def add(self,data):
        last = self.chain[-1]
        ni = last.i +1
        lhash = last.hash
        nb = Block(ni,data,lhash)
        self.chain.append(nb)
    def is_valid(self):
        for i in range(1,len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i-1]
            if current.hash != current.create_hash():
                return False
            if current.prev_hash != previous.hash:
                return False
        return True
        
    def display(self):
        for b in self.chain:
            print("index : " , b.i)
            print("Data : " ,b.data)
            print("Time : " ,b.time)
            print("Hash : " ,b.hash)
            print("prev hash : " ,b.prev_hash)

a = Blockchain()
for i in range(4):
    data = 100 * (i+1)
    a.add(data)

a.display()
a.is_valid()
