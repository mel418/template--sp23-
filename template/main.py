import Calculator
import BookStore
import DLList

def menu_calculator():
    calculator = Calculator.Calculator()
    option = ""
    while option != '0':
        print("""
        1 Check mathematical expression
        2 Store variable values
        3 Print expression with values 
        4 Evaluate expression
        0 Return to main menu
        """)
        option = input()
        if option == "1":
            expression = input("Introduce the mathematical expression: ")
            if calculator.matched_expression(expression):
                print(f"{expression} is a valid expression")
            else:
                print(f"{expression} is invalid expression")
        
        elif option == "2":
            while True:
                var = input("Enter a variable: ")
                val = input("Enter its value: ")
                calculator.set_variable(var, val)
                choice = input("Enter another variable? Y/N: ")
                if choice.lower() != "y":
                    break

        elif option == "3":
            expression = input("Introduce the mathematical expression: ")
            if not calculator.matched_expression(expression):
                print("Invalid expression")
                continue
            print(calculator.print_expression(expression))
        
        elif option == '4':
            exp = input('Enter the expression: ')
            expression = calculator.print_expression(exp)
            for el in expression:
                if el.isalpha():    
                    print("Result: Error - Not all variable values are defined.")
                    return
            print(f'Evaluating expression: {expression}\n\
                  Result: {calculator.evaluate(exp)}')

        ''' 
        Add the menu options when needed
        '''


def menu_bookstore_system():
    bookStore = BookStore.BookStore()
    option = ""
    while option != '0':
        print("""
        s FIFO shopping cart
        r Random shopping cart
        1 Load book catalog
        2 Remove a book by index from catalog
        3 Add a book by index to shopping cart
        4 Remove from the shopping cart
        5 Search book by infix
        6 Get cart best-seller
        7 Add a book by key to shopping cart
        8 Add a book by title prefix to shopping cart
        9 Search best-sellers with infix
        0 Return to main menu
        """)
        option = input()
        if option == "r":
            bookStore.setRandomShoppingCart()
        elif option == "s":
            bookStore.setShoppingCart()
        elif option == "1":
            file_name = input("Introduce the name of the file: ")
            bookStore.loadCatalog(file_name)
            # bookStore.pathLength(0, 159811)
        elif option == "2":
            i = int(input("Introduce the index to remove from catalog: "))
            bookStore.removeFromCatalog(i)
        elif option == "3":
            i = int(input("Introduce the index to add to shopping cart: "))
            bookStore.addBookByIndex(i)
        elif option == "4":
            bookStore.removeFromShoppingCart()
        elif option == "5":
            infix = input("Introduce the query to search: ")
            cnt = int(input("Enter max number of results: "))
            bookStore.searchBookByInfix(infix, cnt)
        elif option == "6":
            bookStore.getCartBestSeller()
        elif option == "7":
            book_key = input("Enter book key: ")
            bookStore.addBookByKey(book_key)
        elif option == '8':
            prefix = input('Introduce the prefix:')
            bookStore.addBookByPrefix(prefix)
        elif option=='9':
            infix = input('Enter infix: ')
            structure = int(input('Enter structure (1 or 2): '))
            max_titles = int(input('Enter max number of titles: '))
            bookStore. bestsellers_with(infix, structure, max_titles)
            

        ''' 
        Add the menu options when needed
        '''

def palindrome_test():
    list = DLList.DLList()
    phrase = input('Enter a word/phrase: ')
    for k in phrase:
        if k.isalnum() == True:
            list.append(k.lower())
    if list.isPalindrome():
        print('Result: Palindrome')
    else:
        print('Result: Not a palindrome')


# main: Create the main menu
def main():
    option = ""
    while option != '0':
        print("""
        1 Calculator
        2 Bookstore System
        3 Palindrome Test
        0 Exit/Quit
        """)
        option = input()

        if option == "1":
            menu_calculator()
        elif option == "2":
            menu_bookstore_system()
        elif option == "3":
            palindrome_test()
       


if __name__ == "__main__":
    main()
