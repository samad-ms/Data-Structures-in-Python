import collections
stack = collections.deque()
def push():
    if len(stack) == n:
        print("stack is full ")
    else:
        e=int(input("enter element to insert"))
        stack.append(e)
        print(stack)

def pop():
    if not stack:
        print("stack is empty.>>>")
    else:
        e=stack.pop()
        print("deleted element is ",e)
        print(stack)

n=int(input("enter the elements:"))
while True:
    choice=int(input("enter your choice: 1>push  2.pop 3.quit"))
    if choice==1:
        push()
    elif choice==2:
        pop()
    elif choice==3:
        break
    else:
        print("enter properly>>")

