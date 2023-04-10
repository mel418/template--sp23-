import numpy as np
import ArrayStack
import ChainedHashTable
import DLList
import re
import BinaryTree
import operator
 
 
class Calculator:
    def __init__(self):
        self.dict = ChainedHashTable.ChainedHashTable(DLList.DLList)
 
    def set_variable(self, k: str, v: float):
        self.dict.add(k, v)
 
    def matched_expression(self, s: str) -> bool:
        stack = ArrayStack.ArrayStack()  
        for el in s:
            if el == '(':
                stack.push(s)
            elif el == ')':
                try:
                    stack.pop()
                except:
                    return False
        if stack.size() == 0:
            return True
        return False 
 
    def _build_parse_tree(self, exp: str) -> str:
        if not self.matched_expression(exp):
            raise ValueError
        variables = [x for x in re.split('\W+', exp) if x.isalnum()]
        exp = re.findall('[-+*/()]|\w+', exp)                      # https://docs.python.org/3/library/re.html
        tree = BinaryTree.BinaryTree()
        tree.r = tree.Node()
        currentNode = tree.r
        for el in exp:
            node = tree.Node()
            if el == '(':
                currentNode = currentNode.insert_left(node)
            elif el in '+-/*':
                currentNode.set_val(el)
                currentNode.set_key(el)
                currentNode = currentNode.insert_right(node)
            elif el in variables:
                currentNode.set_key(el)
                currentNode.set_val(self.dict.find(el))
                currentNode = currentNode.parent
            elif el == ')':
                currentNode = currentNode.parent
        return tree
 
    def _evaluate(self, root):
        op = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
        if root.left != None and root.right != None:
            fn  = op[root.k]
            return fn(self._evaluate(root.left), self._evaluate(root.right))
        elif root.left == None and root.right == None:
            if root.v != None:
                return float(root.v)
            raise ValueError(f"Missing value for variable {root.k}")
        elif root.left != None:
            return self._evalulate(root.left)
        else:
            return self._evaluate(root.right)
    '''
    def _evaluate(self, u):
        op = None # {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
        if u.left != None and u.right != None: # u is an operator 
            op = u.k
            left_val = self._evaluate(u.left)
            right_val = self._evaluate(u.right)

            if not isinstance(right_val, (int, float)):
                right_val = self.dict.find(right_val)
                
            if not isinstance(left_val, (int, float)):
                left_val = self.dict.find(left_val)
                
            # check if left or right val is string, replace w approrpiate variable value
            if op == '+':       
                return float(left_val) + float(right_val)
            if op == '-':
                return float(left_val) - float(right_val)
            if op == '*':
                return float(left_val) * float(right_val)
            if op == '/':
                return float(left_val) / float(right_val)
        elif u.left is not None and u.right is None:
            raise ValueError("Missing right operand")
        elif u.right is not None and u.left is None:
            raise ValueError("Missing left operand")
        elif u.left == None and u.right == None: # u is var (leaf node) or does not exist
            if u.k == None:
                raise ValueError("missing right operand")
            elif u.k != None: # u is leaf node representing var 
                return u.k
            else:
                raise ValueError(f"Missing definition for variable {u.k}")
    '''
    def evaluate(self, exp):
        parseTree = self._build_parse_tree(exp)
        return self._evaluate(parseTree.r)
    
    def print_expression(self, exp: str) -> str:
        var_regex = r'[a-zA-Z]\w*'
        for var in re.findall(var_regex, exp):
            if self.dict.find(var) is None:
                exp = exp
            else:
                exp = exp.replace(var, str(self.dict.find(var)))
        return exp
        
# calculator = Calculator()

# calculator.set_variable('eta2', 200)
# calculator.set_variable('beta6', 9.69)


# exp = "(eta2/beta6)"
# calculator.print_expression(exp)
# print(calculator._build_parse_tree(exp))
# result = calculator.evaluate(exp)
# print(result)