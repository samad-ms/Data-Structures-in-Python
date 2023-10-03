class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None

class Stack:
    def __init__(self):
        self.top=None
        self.size=0

    def push(self,data):
        newnode=Node(data)
        newnode.ref=self.top
        self.top=newnode
        self.size+=1

    def pop_element(self):
        if self.top is None:
            print("cant inset,stack is empty")
        else:
            e=self.top.data
            self.top=self.top.ref
            self.size-=1

    def is_empty(self):
        return self.top == None
    def print_stack(self):
        if self.top is None:
            print("stack is empty")
        else:
            temp=self.top
            while temp:
                print(temp.data,end=" ")
                temp=temp.ref
            print()

    def peek(self):
        if self.top == None:
            print("no peak element,empty stack")
        else:
            return self.top.data

st1=Stack()
st1.push(10)
st1.push(20)
st1.push(30)

st1.print_stack()
print(st1.is_empty())
print(st1.peek())