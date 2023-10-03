stack=[]
def push(e):
    stack.append(e)
def pop_element():
    if not stack:
        print("empty stack , deletion not possible")
    else:
        e=stack.pop()
        # print("poped elements is",e)
        # print(stack)
        return e
def is_empty():
    return  len(stack) == 0
def peek():
    return stack[-1]
def del_mid(st,n,curr=0):
    if is_empty() or curr ==n:
        return
    x=pop_element()
    del_mid(st,n,curr+1)
    if curr!=(n//2):
        push(x)

push(1)
push(2)
push(3)
push(4)
push(5)
push(6)

print(stack)
del_mid(stack,len(stack))
print(stack)


