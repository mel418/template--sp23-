import numpy as np
import random
from ArrayQueue import ArrayQueue


class RandomQueue(ArrayQueue):
    def __init__(self):
        ArrayQueue.__init__(self)

    def remove(self) -> object:
        '''
            remove a random element
            You can call the method of the parent class using super(). e.g.
            super().remove()
        '''
        # todo
        if self.n <= 0: raise IndexError
        random_index = random.randint(0, self.n - 1)
        x = self.a[(random_index + self.j) % len(self.a)]
        for i in range(random_index, self.n-1):
            self.a[(self.j+i) % len(self.a)] = self.a[(self.j+i+1) % len(self.a)]
        #self.a[random_index], self.a[(self.n - 1 + self.j) % len(self.a)] = self.a[(self.n - 1 + self.j) % len(self.a)], self.a[random_index]
        self.n -= 1
        if len(self.a) > 3 * self.n:
            self.resize()
        return x