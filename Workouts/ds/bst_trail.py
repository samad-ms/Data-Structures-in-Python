class BST:
    def __init__(self,data):
        self.lchild=None
        self.rchild=None
        self.key=data
    def insert(self,data):
        if self.key is None:
            self.key=data
        if data<self.key:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild=BST(data)
        if data > self.key:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)

    def search(self,data):
        if self.key == data:
            print("found data")
        if data<self.key:
            if self.lchild:
                self.lchild.search(data)
            else:
                print(" not found data")
        if data > self.key:
            if self.rchild:
                self.rchild.search(data)
            else:
                print(" not found data")


    def min_node(self):
        cur=self
        while cur.lchild:
            cur=cur.lchild
        print("\n min node is ",cur.key)

    def deletion(self,data):
        if data<self.key:
            if self.lchild:
                self.lchild=self.lchild.deletion(data)
        elif data>self.key:
            if self.rchild:
                self.rchild=self.rchild.deletion(data)
        else:
            if not self.lchild:
                return self.rchild
            if not self.rchild:
                return self.lchild
            node=self.rchild
            while node.lchild:
                node=node.lchild
            self.key=node.key
            self.rchild=self.rchild.deletion(node.key)
        return self

    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.key,end=" ")
        if self.rchild:
            self.rchild.inorder()

def isValid(node,left=float("-inf"),right=float("inf")):
    if not node:
        return True
    if not (left<node.key<right):
        return False
    return isValid(node.lchild,left,node.key) and isValid(node.rchild,node.key,right)

def count(root):
    if root is None:
        return 0
    return 1+count(root.lchild)+count(root.rchild)




root=BST(None)
l1=[50,25,20,30,27,26,28,60,55,70]
for n in l1:
    root.insert(n)
root.inorder()
print()
# root.deletion(50)
root.inorder()
root.min_node()
print(count(root))
print(isValid(root))