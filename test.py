import hashlib,time

class Block:
    def __init__(self,i,d,ts,ph="0"):
        self.i = i
        self.d = d
        self.ts = ts
        self.ph = ph
        self.hash = self.create_hash()
    def create_hash(self):
        bs = f"{self.i}{self.d}{self.ts}{self.ph}".encode()
        return hashlib.sha256(bs).hexdigest()
    
class Blockchain:
    def __init__(self):
        self.chain = [self.cgb()]
    def cgb(self):
        return Block(1," ",time.strftime("%H:%M:%S",time.localtime()),"0")
    def glb(self):
        return self.chain[-1]
    def ab(self,data):
        lb = self.glb()
        ni = lb.i +1
        nt = time.strftime("%H:%M:%S",time.localtime())
        ph = lb.hash
        nb = Block(ni,data,nt,ph)
        self.chain.append(nb)
        return nb
    def is_chain_valid(self):
        for i in range(1,len(self.chain)):
            c = self.chain[i]
            p = self.chain[i-1]
            if c.hash != c.create_hash():
                return False
            if c.ph != p.hash:
                return False
        return True
    def ds(self):
        for b in self.chain:
            print(
                f"index {b.i} \n"
                f"data {b.d} \n"
                f"time {b.ts} \n"
                f"hash {b.hash} \n"
                f"prior_hash {b.ph} \n"
            )
bc = Blockchain()
for i in range(3):
    data = f"abcd {10 * (i+1)}"
    bc.ab(data)
bc.ds()
        