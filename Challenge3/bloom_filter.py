import hashlib

class BloomFilter:
    def __init__(self, size, hash_count):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = [0] * size
    
    def hash_i(self, i, x):
        return int(hashlib.sha256((str(i) + x).encode('utf-8')).hexdigest(), 16) % self.size
    
    def add(self, item):
        for i in range(self.hash_count):
            index = self.hash_i(i, item)
            self.bit_array[index] = 1
    
    def check(self, item):
        for i in range(self.hash_count):
            index = self.hash_i(i, item)
            if self.bit_array[index] == 0:
                return False
        return True
