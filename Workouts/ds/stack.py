stack=[]
def push():
    if len(stack)==n:
        print("full..")
        print(stack)
    else:
        e=int(input("enter elements:"))
        stack.append(e)
        print(stack)
def pop():
    if not stack:
        print("emptyy....")
        print(stack)
    else:
        e=stack.pop()
        print("deleted elements:",e)
        print(stack)

n=int(input("enter the size of stack:"))
while True:
    choice = int(input("enter your choice :- 1:push  2:pop 3:quit"))
    if choice == 1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        break
    else:
        print("enter approprieate option")
