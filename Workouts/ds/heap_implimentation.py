class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def is_empty(self):
        return len(self.heap) == 0

    def insert(self, data):
        self.heap.append(data)
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, i):
        while i > 0 and self.heap[i] < self.heap[self.parent(i)]:
            parent_idx = self.parent(i)
            self.swap(i, parent_idx)
            i = parent_idx

    def extract_min(self):
        if self.is_empty():
            return None
        min_value = self.heap[0]
        last_value = self.heap.pop()

        if not self.is_empty():
            self.heap[0] = last_value
            self.heapify_down(0)

        return min_value


    def heapify_down(self, i):
        n = len(self.heap)
        left = self.left_child(i)
        right = self.right_child(i)
        smallest = i

        if left < n and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < n and self.heap[right] < self.heap[smallest]:
            smallest = right

        if i != smallest:
            self.swap(i, smallest)
            self.heapify_down(smallest)


# Example usage:
h = MinHeap()
arr = [2, 1, 3, 6, 7, 6, 4, 7]
for i in arr:
    h.insert(i)

print("Min Heap:", h.heap)
h.heap_sort(h.heap)
print()
print("Min Heap:", h.heap)