class HashTable:
    def __init__(self):
        self.MAX=10
        self.arr=[[] for i in range(self.MAX)]
    def get_hash(self,key):
        h=0
        for char in key:
            h=h+ord(char)
        return h%self.MAX

    def __setitem__(self, key, value):
        h=self.get_hash(key)
        found=False
        for idx,element in enumerate(self.arr[h]):
            if len(element)==2 and element[0]==key:
                self.arr[h]=(key,value)
                found=True
        if found == False:
            self.arr[h].append((key, value))

    def __getitem__(self, item):
        h=self.get_hash(item)
        for element in self.arr[h]:
            if element[0] == item:
                return element[1]

    def __delitem__(self, item):
        h = self.get_hash(item)
        for idx,kv in enumerate(self.arr[h]):
            if kv[0]==item:
                del self.arr[h][idx]

t=HashTable()
t['march 6']=130
t['march 17']=230
t['march 8']=420
print(t['march 6'])
del t['march 6']
del t['march 17']
print(t.arr)