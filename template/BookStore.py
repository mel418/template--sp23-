import Book
import ArrayList
import ArrayQueue
import RandomQueue
import DLList
import SLLQueue
import ChainedHashTable
import BinarySearchTree
# import BinaryHeap
# import AdjacencyList
import time
import MaxQueue

class BookStore:
    '''
    BookStore: It simulates a book system such as Amazon. It allows  searching,
    removing and adding in a shopping cart. 
    '''

    def __init__(self):
        self.bookCatalog = None
        self.shoppingCart = ArrayQueue.ArrayQueue()
        #self.shoppingCart = MaxQueue.MaxQueue()
        self.bookIndices = ChainedHashTable.ChainedHashTable()
        self.sortedTitleIndices = BinarySearchTree.BinarySearchTree()


    def loadCatalog(self, fileName: str):
        '''
            loadCatalog: Read the file filenName and creates the array list with all books.
                book records are separated by  ^. The order is key, 
                title, group, rank (number of copies sold) and similar books
        '''
        self.bookCatalog = ArrayList.ArrayList()
        with open(fileName, encoding="utf8") as f:
            # The following line is the time that the computation starts
            start_time = time.time()
            for line in f:
                (key, title, group, rank, similar) = line.split("^")
                s = Book.Book(key, title, group, rank, similar)
                self.bookCatalog.append(s)
                self.sortedTitleIndices.add(title, self.bookCatalog.size()-1)
            # The following line is used to calculate the total time 
            # of execution
            elapsed_time = time.time() - start_time
            print(f"Loading {self.bookCatalog.size()} books in {elapsed_time} seconds")

    def setRandomShoppingCart(self):
        q = self.shoppingCart
        start_time = time.time()
        self.shoppingCart = RandomQueue.RandomQueue()
        while q.size() > 0:
            self.shoppingCart.add(q.remove())
        elapsed_time = time.time() - start_time
        print(f"Setting radomShoppingCart in {elapsed_time} seconds")

    def setShoppingCart(self):
        q = self.shoppingCart
        start_time = time.time()
        self.shoppingCart = ArrayQueue.ArrayQueue()
        while q.size() > 0:
            self.shoppingCart.add(q.remove())
        elapsed_time = time.time() - start_time
        print(f"Setting radomShoppingCart in {elapsed_time} seconds")

    def removeFromCatalog(self, i: int):
        '''
        removeFromCatalog: Remove from the bookCatalog the book with the index i
        input: 
            i: positive integer    
        '''
        # The following line is the time that the computation starts
        start_time = time.time()
        self.bookCatalog.remove(i)
        # The following line is used to calculate the total time 
        # of execution
        elapsed_time = time.time() - start_time
        print(f"Remove book {i} from books in {elapsed_time} seconds")

    def addBookByIndex(self, i: int):
        '''
        addBookByIndex: Inserts into the playlist the song of the list at index i 
        input: 
            i: positive integer    
        '''
        # Validating the index. Otherwise it  crashes
        if i >= 0 and i < self.bookCatalog.size():
            start_time = time.time()
            s = self.bookCatalog.get(i)
            self.shoppingCart.add(s)
            elapsed_time = time.time() - start_time
            print(f"Added to shopping cart {s}) \n{elapsed_time} seconds")

    def searchBookByInfix(self, infix: str, cnt : int):
        '''
        searchBookByInfix: Search all the books that contains infix
        input: 
            infix: A string    
        '''
        start_time = time.time()
        cookieMonster123 = 0
        for penguin in self.bookCatalog:
            if infix in str(penguin.title):
                print(penguin)
                cookieMonster123 += 1
            if cookieMonster123 >= cnt:
                break
        elapsed_time = time.time() - start_time
        print(f"searchBookByInfix Completed in {elapsed_time} seconds")

    def removeFromShoppingCart(self):
        '''
        removeFromShoppingCart: remove one book from the shoppung cart  
        '''
        start_time = time.time()
        if self.shoppingCart.size() > 0:
            u = self.shoppingCart.remove()
            elapsed_time = time.time() - start_time
            print(f"removeFromShoppingCart {u} Completed in {elapsed_time} seconds")

    def getCartBestSeller(self):
        '''
        getCartBestSeller: returns best-seller amongst the rest of the books in the cart
        '''
        print(f'getCartBestSeller returned')
        print(self.shoppingCart.max().title)

        return self.shoppingCart.max().title
    
    def addBookByKey(self, key: str):
        '''
        addBookByKey: Adds the book with the given key to the shopping cart.
        '''
        start_time = time.time()
        index = self.bookIndices.find(key)
        if index == None:
            print("Book not found.")
        else:
            book = self.bookCatalog.get(index)
            self.shoppingCart.add(book)
            print(f'Added title: {book.title}')
        elapsed_time = time.time() - start_time
        print(f"addBookByKey Completed in {elapsed_time} seconds")

    def addBookByPrefix(self, prefix: str):
        ''' 
        adds the book with the given title prefix to the shopping cart and returns True. 
        If no title contains that prefix or if the prefix is an empty string, then the method must return False and add nothing to the cart.
        HINT: First search the binary search tree for the index corresponding to the title with the given prefix. 
        If the index is not None, add the Book at the given index in the bookCatalogue to the cart
        '''
        
        #todo
        start_time = time.time()

        bookWPrefix = self.sortedTitleIndices.find_or_successor(prefix).v 
        #print(f'bookwPrefix: {bookWPrefix}')

        if bookWPrefix is not None:
            if len(prefix) > 1:
                book = self.bookCatalog.get(bookWPrefix)
                n = len(prefix)
                #print(f'n: {n}')
                if book.title[0:n] == prefix:
                    self.shoppingCart.add(book)
                    #print(f'book: {book}')
                    print("Added first matched title:", book.title)
            
        else:
            print("Error: Prefix was not found.")
            return None

        elapsed_time = time.time() - start_time
        print(f"addBookByPrefix Completed in {elapsed_time} seconds") 