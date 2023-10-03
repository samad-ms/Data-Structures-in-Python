import queue
import queue
stack = queue.LifoQueue(2)

def display():
    elements = list(stack.queue)
    if not elements:
        print("Stack is empty")
    else:
        print("Stack elements:", end=" ")
        for e in elements:
            print(e, end=" ")
        print()


def push():
    if stack.qsize==2:
        e = int(input("enter element to insert"))
        stack.put(e,timeout=1)
        display()
    else:
        e=int(input("enter element to insert"))
        stack.put(e)
        display()

def pop():
    if not stack:
        print("stack is empty.>>>")
    else:
        e=stack.get()
        print("deleted element is ",e)
        display()


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

