'''
Problem: Dind the min number NOT sum  of sub_array
Solution: with special case, return result 1 when beginning array bigger than  1 
Find the sum of first (i-th) elements S and expected result s+1 if s+1 less than (i+1-th) element, then break

Here is trick for find solution
'''
class Myarray: 
    def __init__(self, dlist): #similar to constructor in C++ to assign value from initialization class
        self.dlist = dlist
        
    def FindMinElement(self):
        a = 1 
        self.dlist.sort()
        for i in range(0, len(self.dlist), 1):
            if (self.dlist[i] <= a):
                a += self.dlist[i]
            else:
                break
        return a

    # Another way to solve which be more closer with the idea of solution
    '''
    def FindMinElement(self):
        a = 1
        self.dlist.sort()
        for i in range(0, len(self.dlist), 1):
            if (a < self.dlist[i]):
                break
            else:
                a += self.dlist[i]
        return a
    '''

#Test with a simple list
a_list = [1,2,3,4]
b=[2,4,5]

my_class = Myarray(a_list)
result = my_class.FindMinElement()
print(result)

class2 = Myarray(b)
result2 = class2.FindMinElement()
print(result2)


