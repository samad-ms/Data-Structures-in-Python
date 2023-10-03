import queue

stack = queue.LifoQueue(3)

# Push elements onto the stack
stack.put(1)
stack.put(2)
stack.put(3)
stack.get()

# Convert the stack to a list
liststack = list(stack.queue)

print(stack.full())
print(stack.empty())
print(liststack)
print(liststack[-1])