class BST:
    def __init__(self,data):
        self.lchild=None
        self.key=data
        self.rchild=None
    def insertion(self,data):
        if self.key is None:
            self.key = data
            return
        if data<self.key:
            if self.lchild:
                self.lchild.insertion(data)
            else:
                self.lchild=BST(data)
        else:
            if self.rchild:
                self.rchild.insertion(data)
            else:
                self.rchild=BST(data)

    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.key,end=" ")
        if self.rchild:
            self.rchild.inorder()
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
    def search(self,data):
        if self.key == data:
            print("data found")
            return
        if data<self.key:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("data not found")
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("data not found")

    def min_node(self):
        node=self
        while node.lchild:
            node=node.lchild
        print(node.key)

    def max_node(self):
        node = self
        while node.rchild:
            node = node.rchild
        print(node.key)

    def deletion(self, data):
        if not self:
            return self
        if data < self.key:
            self.lchild = self.lchild.deletion(data)
        elif data > self.key:
            self.rchild = self.rchild.deletion(data)
        else:
            if not self.lchild:
                return self.rchild
            elif not self.rchild:
                return self.lchild

            cur = self.rchild
            while cur.lchild:
                cur = cur.lchild
            self.key = cur.key
            self.rchild = self.rchild.deletion(cur.key)
        return self
    def valid(self,root,left=float("-inf"),right=float("inf")):
        if not root:
            return True
        if not(left<root.key<right):
            return False
        return self.valid(root.lchild,left,root.key) and self.valid(root.rchild,root.key,right)

    def tree_height(self,root):
        if not root:
            return -1  # Height of an empty tree is -1 (considering edges)

        left_height = self.tree_height(root.lchild)
        right_height = self.tree_height(root.rchild)

        return max(left_height, right_height) + 1


root=BST(None)
l1=[50,25,75,43,34]

for i in l1:
    root.insertion(i)
# root.inorder()
# print()
# root.preorder()
# print()
# root.search(2)
# print()
# root.postorder()
root.inorder()
print()
root.deletion(75)
root.inorder()
print()
root.min_node()
root.max_node()
print(root.valid(root))
print(root.tree_height(root))