from uuid import getnode
from Interfaces import List
import numpy as np


class DLList(List):
    class Node:
        def __init__(self, x: object):
            self.next = None
            self.prev = None
            self.x = x

    def __init__(self):
        self.dummy = DLList.Node("")
        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy
        self.n = 0

    def get_node(self, i: int) -> Node:
        # todo
        if i < 0 or i > self.n: return None
        if i < self.n/2: 
            p = self.dummy.next
            for k in range(i):
                p = p.next
        else:  
            p = self.dummy
            for k in range(self.n - i):
                p = p.prev
        return p


    def get(self, i) -> object:
        # todo
        if i < 0 or i >= self.n: return None
        return self.get_node(i).x

    def set(self, i: int, x: object) -> object:
        # todo
        if i < 0 or i>= self.n: raise IndexError
        u = self.get_node(i)
        y = u.x
        u.x = x
        return y

    def add_before(self, w: Node, x: object) -> Node:
        # todo
        if w is None: raise IndexError
        u = self.Node(x)
        u.prev = w.prev
        u.next = w
        w.prev = u
        u.prev.next = u
        self.n += 1  # always increment the size of the list
        return u

    def add(self, i: int, x: object):
        # todo
        if i < 0 or i > self.n:
            raise IndexError()
        return self.add_before(self.get_node(i), x)
    
    def _remove(self, w: Node):
        # todo
        w.prev.next = w.next
        w.next.prev = w.prev
        if w is self.dummy.next:
            self.dummy.next = w.next
        if w is self.dummy.prev:
            self.dummy.prev = w.prev
        self.n -= 1
        return w.x

    def remove(self, i: int):
        if i < 0 or i >= self.n: raise IndexError()
        w = self.get_node(i)
        return self._remove(w)
        

    def size(self) -> int:
        return self.n

    def append(self, x: object):
        self.add(self.n, x)

    def reverse(self):
        curr = self.dummy.next
        while curr != self.dummy:
            # swap prev and next attributes of the current node
            temp = curr.next
            curr.next = curr.prev
            curr.prev = temp

            # move to the next node
            curr = temp

        # swap prev and next attributes of the dummy node
        temp = self.dummy.next
        self.dummy.next = self.dummy.prev
        self.dummy.prev = temp

        return self

    def isPalindrome(self) -> bool:
        # todo
        if self.n < 2: return True
        left = self.dummy.next
        right = self.dummy.prev
        while left != right and left.prev != right:
            if left.x != right.x:
                return False
            left = left.next
            right = right.prev
        return True

    def swap_ends(self):
        if self.n < 2:  # list is empty or has only one node
            return self
        head = self.dummy.next
        tail = self.dummy.prev
        # swap prev and next attributes of the head node
        temp = head.prev
        head.prev = tail.prev
        tail.prev = temp
        temp = head.next
        head.next = tail.next
        tail.next = temp
        # update references of adjacent nodes
        head.prev.next = head
        head.next.prev = head
        tail.prev.next = tail
        tail.next.prev = tail
        return self



    def contains(self, x: object):
        if self.n == 0:
            return False
        current = self.dummy.next
        while current != self.dummy:
            if current.x == x:
                return True
            current = current.next
        return False


    def __str__(self):
        s = "["
        u = self.dummy.next
        while u is not self.dummy:
            s += "%r" % u.x
            u = u.next
            if u is not None:
                s += ","
        return s + "]"

    def __iter__(self):
        self.iterator = self.dummy.next
        return self

    def __next__(self):
        if self.iterator != self.dummy:
            x = self.iterator.x
            self.iterator = self.iterator.next
        else:
            raise StopIteration()
        return x

# q = DLList()
# q.append('D')
# q.append('B')
# q.append('F')
# q.append('A')
# q.append('G')
# q.append('E')
# q.append('C')
# q.remove(0)
# q.remove(5)
# q.append('X')
# q.set(3,'B')
# q.add(2,'A')
# print(q,q.dummy.next.x,q.dummy.prev.x)
# q.swap_ends()
# print(q,q.dummy.next.x,q.dummy.prev.x)
#print(f'head: {q.get_node} and tail: {q.get(q.n-1)}')
# # print(q.reverse())
# # print(q.isPalindrome())