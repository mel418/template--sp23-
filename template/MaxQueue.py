from SLLQueue import SLLQueue
from DLLDeque import DLLDeque


class MaxQueue(SLLQueue):
    def __init__(self):
        SLLQueue.__init__(self)
        self.max_deque = DLLDeque()  # NOTE: DLLDeque implements the Deque interface but also inherits all methods from DLList 

    def add(self, x : object):
        """
    adds an element to the end of this max queue
    INPUT: x the element to add
    """
        SLLQueue.add(self, x)
        while self.max_deque.size() > 0 and x > self.max_deque.dummy.prev.x:
            self.max_deque.remove_last()
        self.max_deque.add_last(x) 

    def remove(self) -> object:
        """
    removes and returns the element at the head of the max queue
    """
        x = SLLQueue.remove(self)
        if x == self.max_deque[0]:
            self.max_deque.remove_first()
        return x

    def max(self):
        """
    returns the maximum element stored in the queue
        """
        return self.max_deque.get(0)


# mq = MaxQueue()
# mq.add(3)
# mq.add(4)
# mq.add(1)
# print("Added:", 3)
# print("MaxQueue contents:", mq)
# print("Max Dequeu contents", mq.max_deque)
# print("Max element", mq.max(), "\n\n")

"""
# TESTER
mq = MaxQueue()
mq.add(3)
print("Added:", 3)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

mq.add(2)
print("Added:", 2)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

mq.add(1)
print("Added:", 1)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

mq.add(4)
print("Added:", 4)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

r = mq.remove()
print("Removed element:", r)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

r = mq.remove()
print("Removed element:", r)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

r = mq.remove()
print("Removed element:", r)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

mq.add(8)
print("Added:", 8)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

mq.add(3)
print("Added:", 3)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

mq.add(5)
print("Added:", 5)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

mq.add(4)
print("Added:", 4)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

mq.add(1)
print("Added:", 1)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")

mq.add(6)
print("Added:", 6)
print("MaxQueue contents:", mq)
print("Max Dequeu contents", mq.max_deque)
print("Max element", mq.max(), "\n\n")


while mq.size() > 0:
    r = mq.remove()
    print("Removed element:", r)
    print("MaxQueue contents:", mq)
    print("Max Dequeu contents", mq.max_deque)
    if mq.size() > 0:
        print("Max element", mq.max(), "\n\n")
        
"""