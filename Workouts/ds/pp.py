def preoreder(root):
    print(root.key)
    if root.lchild:
        root.lchild.preorder()
    if root.rchild:
        root.rchild.preorder()