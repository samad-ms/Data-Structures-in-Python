class BST:
    def __init__(self,data):
        self.key=data
        self.lchild=None
        self.rchild=None
    def insert(self,data):
        if self.key is None:
            self.key=data
            return
        if self.key==data:
            return
        if self.key>data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild=BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild=BST(data)

    def search(self,data):
        if self.key==data:
            print("found the value")
        if self.key > data:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("data is not present")
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("data is not present")

    def preorder(self):
        print(self.key,end=" ")
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()

    def postorder(self):
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.key, end=" ")

    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.key,end=" ")
        if self.rchild:
            self.rchild.inorder()

    def delete(self,data):
        if self.key is None:
            print("empty tree")
            return
        if data<self.key:   #l= [10,6,3,1,6,98,3,7]
            if self.lchild:
                self.lchild=self.lchild.delete(data)
                print(self.key)
            else:
                print("not present")
        elif data>self.key:
            if self.rchild:
                self.rchild = self.rchild.delete(data)
            else:
                print("not present")
        else:
            if self.lchild is None:
                temp=self.rchild
                self=None
                return temp
            if self.rchild is None:
                temp = self.lchild
                self = None
                return temp

            node=self.rchild
            while self.lchild:
                node=self.lchild
            self.key=node.key
            self.rchild=self.rchild.delete(node.key)
        return self


root=BST(None)
l=[10,6,3,1,6,98,3,7]
for i in l:
    root.insert(i)
root.inorder()
root.delete(1)
print("<<<<<<<<<")
root.inorder()

