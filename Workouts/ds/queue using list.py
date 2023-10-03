queue = []
def enque():
    e=int(input("enter the element to insert:"))
    queue.append(e)
    print("appented element is ",e)
    print(queue)

def deque():
    if not queue:
        print("queue is empty")
    else:
        e = queue.pop(0)
        print("deleted element is ", e)
        print(queue)


while True:
    choice=int(input("enter your choice : 1)add 2)delete 3)quit"))
    if choice == 1:
        enque()
    elif choice==2:
        deque()
    elif choice==3:
        break
    else:
        print("appropriate choice>>>>>>")
