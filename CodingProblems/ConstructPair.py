'''
Iner function - Closure()_ nested function
The main idea: Owing to cons() return a function and this function also return another function really processing arg
(3-function will be call).
The target function also needs a func as a argument and continue returning another function that return true value

car(cons(a,b)) : cons(a,b) ~ func --> func(left) --> left(a,b) --> a
'''
def cons(a,b):
    def pair(f):
        return f(a,b)
    return pair

def car(func):
    def left(a,b):
        return a
    return func(left)

def cdr(func):
    def right(a,b):
        return b
    return func(right)


#For test
print(car(cons(1,2)))