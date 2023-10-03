class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            data = self.front.data
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            return data

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            current = self.front
            while current is not None:
                print(current.data, end=" ")
                current = current.next
            print()

# Example usage:
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.display()  # Output: 10 20 30

queue.dequeue()
queue.display()  # Output: 20 30
