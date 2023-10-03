import collections
class Stack:
    def __init__(self):
        self.container=collections.deque()

    def push(self,data):
        self.container.append(data)
        print(self.container)
    def pop(self):
        if len(self.container)==0:
            print("rmpty cant delete>>>>")
        else:
            self.container.pop()
            print(self.container)

st1=Stack()
while True:
    choice=int(input("enter choice: 1)push 2)pop 3)quit"))
    if choice == 1:
        data=input("enter data: ")
        st1.push(data)
    elif choice==2:
        st1.pop()
    elif choice ==3:
        break
    else:
        print("enter right option>>>>")