class BST:
    def __init__(self,data):
        self.key=data
        self.lchild=None
        self.rchild=None
    def insertion(self,data):
        if self.key is None:
            self.key=data
            return
        if  self.key == data:
            return
        if data<self.key:
            if self.lchild:
                self.lchild.insertion(data)
            else:
                self.lchild=BST(data)
        if data > self.key:
            if self.rchild:
                self.rchild.insertion(data)
            else:
                self.rchild = BST(data)

    def search(self,data):
        if self.key is None:
            print("empty ,cant search")
            return
        if  self.key == data:
            print("item fount")
            return
        if data<self.key:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("item not fount")
        if data > self.key:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("item not fount")

    def deletion(self,data):
        if self.key is None:
            print("empty ,cant search")
            return
        if data<self.key:
            if self.lchild:
                self.lchild=self.lchild.deletion(data)
            else:
                print("item not fount")
        elif data > self.key:
            if self.rchild:
                self.rchild=self.rchild.deletion(data)
            else:
                print("item not fount")
        else:
            if self.lchild:
                temp = self.rchild
                self = None
                return temp
            if self.rchild:
                temp = self.lchild
                self = None
                return temp

            node = self.rchild
            while node.lchild:
                node = node.lchild
            self.key = node.key
            self.rchild = self.rchild.deletion(node.key)
        return self

    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.key,end=' ')
        if self.rchild:
            self.rchild.inorder()


root=BST(None)
l=[1,2,3,4,5,6]
for n in l:
    root.insertion(n)


root.inorder()
print()
root.deletion(2)
root.inorder()
print()
root.search(1)


