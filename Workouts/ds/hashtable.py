class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr=[None for i in range(self.MAX)]

    def get_hash(self,key):
        h=0
        for c in key:
            h=h+ord(c)
        return h%self.MAX

    def add_element(self,key,val):
        h=self.get_hash(key)
        self.arr[h]=val

    def del_element(self,key):
        h=self.get_hash(key)
        self.arr[h]=None

t1=HashTable()
t1.add_element('march 1',320)
print(t1.arr)

