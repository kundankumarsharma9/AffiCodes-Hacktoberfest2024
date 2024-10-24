class Queue:
    def __init__(self):
        self.queue = []  # Initialize an empty list to represent the queue

    # Function to add an element to the rear of the queue (enqueue)
    def enqueue(self, data):
        self.queue.append(data)
        print(f"Enqueued {data}")

    # Function to remove an element from the front of the queue (dequeue)
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty!")
            return None
        else:
            data = self.queue.pop(0)
            print(f"Dequeued {data}")
            return data

    # Function to check if the queue is empty
    def is_empty(self):
        return len(self.queue) == 0

    # Function to get the size of the queue
    def size(self):
        return len(self.queue)

    # Function to view the front element of the queue
    def front(self):
        if self.is_empty():
            print("Queue is empty!")
            return None
        else:
            return self.queue[0]

    # Function to display the elements of the queue
    def display(self):
        if self.is_empty():
            print("Queue is empty!")
        else:
            print("Queue elements:", self.queue)

# Example usage:
q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.display()  # Output: Queue elements: [10, 20, 30]

q.dequeue()  # Output: Dequeued 10
q.display()  # Output: Queue elements: [20, 30]

print("Front element:", q.front())  # Output: Front element: 20
print("Queue size:", q.size())      # Output: Queue size: 2
