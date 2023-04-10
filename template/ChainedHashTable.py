from Interfaces import Set
from DLList import DLList
import numpy as np
 
 
class ChainedHashTable(Set):
    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
 
    def __init__(self, dtype=DLList):
        self.dtype = dtype
        self.d = 1
        self.t = self.alloc_table(2 ** self.d)
        self.z = 193759204821
        self.w = 31
        self.n = 0
 
    def alloc_table(self, n: int):
        t = np.zeros(n, dtype=object)
        for i in range(n):
            t[i] = self.dtype()
        return t
 
    def _hash(self, key: int) -> int:
        #return self.z * hash(key) % (2 ** self.w) >> (self.w - self.d)
        return (hash(key))% (2**self.d)
        #return (3*hash(key)) % (2 **self.d)

    def size(self) -> int:
        return self.n
 
    def find(self, key: object) -> object:
        # todo
        bin = self._hash(key)
        #print(f"bin of {key} is {bin}")
        for i in range(self.t[bin].size()):
            if self.t[bin].get(i).key == key:
                return self.t[bin].get(i).value
        return None

    
    
    def add(self, key: object, value: object) -> bool:
        # Check if the key already exists
        if self.find(key) is not None:
            return False
            
        # Check if the table needs resizing
        if self.n == len(self.t):
            self.resize()
            #print(f"resize used after {value}")
        
        # Add the item to the table
        bin = self._hash(key)
        item = self.Node(key, value)
        self.t[bin].add(0, item)
        self.n += 1
        return True
 
 
    def remove(self, key: int) -> object:
        # todo
        bin = self._hash(key)
        for i in range(self.t[bin].size()):
            if self.t[bin].get(i).key == key:
                self.t[bin].remove(i)
                self.n -= 1
                if len(self.t) > 3*self.n: 
                    self.resize()
                    #print(f"resize used after value {key}")
                
                return True
        return None
 
 
    def resize(self):
        #todo
        if self.n == len(self.t):
            self.d += 1
        elif len(self.t) > 3*self.n and self.d > 1:
            self.d -= 1
        else:
            return
        
        temp = self.alloc_table(2**self.d)
        for j in range(len(self.t)):
            for i in range(self.t[j].size()):
                bin = self._hash(self.t[j].get(i).key)
                temp[bin].add(0, self.t[j].get(i))
        self.t = temp
 
    def __str__(self):
        s = "["
        for i in range(len(self.t)):
            for j in range(len(self.t[i])):
                k = self.t[i][j]
                s += str(k.key)
                s += ":"
                s += str(k.value)
                s += ";"
        return s + "]"
 
'''
table = ChainedHashTable()


table.add(23, "A")

table.add(15, "B")

table.add(11, "C")

table.remove(23)

table.remove(15)

table.add(10, "D")

table.add(12, "A")

print(table)
print(table.find(12))
print(table.find(10))
print(table.find(11))
'''