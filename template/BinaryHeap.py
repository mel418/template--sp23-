import numpy as np
import math
from Interfaces import Queue
from Interfaces import Tree



def left(i: int) -> int:
    """
    helper method; returns the index of the left child of the element at index i
    """
    # todo
    return (2*i) + 1 



def right(i: int) -> int:
    """
    helper method; returns the index of the right child of the element at index i
    """
    # todo
    return 2 * (i + 1)


def parent(i: int) -> int:
    """
    helper method; returns the index of the parent of the element at index i
    """
    # todo
    return (i-1) // 2


def _new_array(n: int) -> np.array:
    """
    helper method; creates a new numpy array of 0's of size n
    """
    return np.zeros(n, object)


class BinaryHeap(Queue, Tree):
    def __init__(self):
        self.a = _new_array(1)
        self.n = 0

    def add(self, x: object):
        # todo
        if len(self.a) == self.n: self._resize()
        self.a[self.n] = x
        self.n += 1
        self._bubble_up_last()
        return True

    def remove(self):
        # todo
        if self.n == 0: raise IndexError
        x = self.a[0]
        self.a[0] = self.a[self.n-1]
        self.n -= 1
        self._trickle_down_root()
        if (3 * self.n) < len(self.a): self._resize()
        return x

    def depth(self, u) -> int:
        # todo
        if u == None: return -1
        for i in range(self.n):
            if self.a[i] == u:
                d = 0
                while i != 0:
                    i = parent(i)
                    d += 1
                return d
        raise ValueError(f"{u} is not found in the binary heap.")

    def height(self) -> int:
        # todo
        return math.floor(math.log2(self.n))

    def bf_order(self) -> list:
        #todo
        nodes = []
        q = [0]  # Start with the root node
        while q:
            i = q.pop(0)
            nodes.append(self.a[i])
            if left(i) < self.n:
                q.append(left(i))
            if right(i) < self.n:
                q.append(right(i))
        return nodes
        #return self.__str__()

    def in_order(self) -> list:
        def _in_order(i):
            nodes = []
            if i < self.n:
                nodes += _in_order(left(i))
                nodes.append(self.a[i])
                nodes += _in_order(right(i))
            return nodes
        return _in_order(0)

    def post_order(self) -> list:
        def _post_order(i):
            nodes = []
            if i < self.n:
                nodes += _post_order(left(i))
                nodes += _post_order(right(i))
                nodes.append(self.a[i])
            return nodes
        return _post_order(0)


    def pre_order(self) -> list:
        def _pre_order(i):
            nodes = []
            if i < self.n:
                nodes.append(self.a[i])
                nodes += _pre_order(left(i))
                nodes += _pre_order(right(i))
            return nodes
        return _pre_order(0)


    def size(self) -> int:
        return self.n

    def find_min(self):
        if self.n == 0: raise IndexError()
        return self.a[0]

    def _bubble_up_last(self):
        # todo
        i = self.n-1 
        p_idx = parent(i)
        while i > 0 and self.a[i] < self.a[p_idx]:
            self.a[i], self.a[p_idx] = self.a[p_idx], self.a[i]
            i = p_idx
            p_idx = parent(i)

    def _resize(self):
        # todo
        new_array = np.zeros(2 * self.n, object)
        for k in range(self.n):
            new_array[k] = self.a[k]
        self.a = new_array

    def _trickle_down_root(self):
        # todo
        i = 0
        while i < self.n:
            l_idx = left(i)
            r_idx = right(i)
            min_idx = i
            if l_idx < self.n and self.a[l_idx] < self.a[min_idx]:
                min_idx = l_idx
            if r_idx < self.n and self.a[r_idx] < self.a[min_idx]:
                min_idx = r_idx
            if min_idx != i:
                self.a[i], self.a[min_idx] = self.a[min_idx], self.a[i]
                i = min_idx
            else:
                break

    def __str__(self):
        return str(self.a[0:self.n])
    
    
# heap = BinaryHeap() # -19, -26, -25, 3, -30
# heap.add(-19)
# heap.add(-26)
# heap.add(-25)
# heap.add(3)
# heap.add(-30)
# print(heap)


