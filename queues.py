# a  list, first in first out FIFO
#enqueue = add 
#dequeue = remove
#queue with list
from collections import deque
from queue import Queue


queue1 = []
queue1.append(3)
queue1.append(5)
queue1.append(7)
print(f"queue1 : {queue1}")
queue1.pop(0)
print(f"popped queue1: {queue1}")
#queue with deqeue
q2 = deque()
q2.append(2)
q2.append(5)
q2.append(8)
print(f"queue 2: {q2}")
q2.popleft()
print(f"popped queue 2: {q2}")

q3 = Queue(maxsize=3)
print(q3.qsize())
q3.put(4)
q3.put(8)
q3.put(12)
print(q3.full())
print("elements in queue 3")
print(q3.get())
print(q3.get())
print(q3.get())
#empty queue
print("\nEmpty:",q3.empty())
q3.put(5)
q3.put(8)
print("elements in queue 3")
print(q3.get())
print(q3.get())
print("\nFull", q3.full())
#element as stack using queues
class Q:
    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)
    #pop
    def pop(self) -> int:
        pass
    #top
    def top(self):
        return self.q[-1]
    #check if empty
    def isEmpty(self):
        return len(self.q) == 0
