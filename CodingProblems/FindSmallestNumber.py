'''
The main idea find the min number not sun of sub_array - special case, return result 1
Find the sum of first i elements assuming s and expected result s+1 if s+1 less than i+1-th element and break
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

#Test with a simple list
a_list = [1,2,3,4]

my_class = Myarray(a_list)
result = my_class.FindMinElement()
print(result)


