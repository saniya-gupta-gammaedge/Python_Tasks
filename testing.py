print("Helooo!!! It's Day 4")


#factorial function

# from doctest import testmod

# def fact(n):

#     '''
#     This function returns the factorial
#     of any number...
    
#     Input and expected output
#     >>> fact(2)
#     2
#     >>> fact(3)
#     6
    
#     '''
#     fact=1
#     for i in range(1,n+1):
#          fact=fact*i
#     print(fact)




# #call the testmod function
# if __name__=="__main__":
#     testmod(name="fact()",verbose=True)


# def add(a, b):
#     """
#     Adds two numbers together.

#     >>> add(2, 3)
#     5
#     >>> add(-1, 1)
#     0
#     >>> add(0, 0)
#     0
#     """
#     return a + b

# if __name__ == "__main__":
#     import doctest
#     doctest.testmod(verbose=True)


#division function
# def divide(a,b):
#     '''
#     This function divides the 
#     numbers provided by the user

#     >>> divide(10,5)
#     2
#     >>> divide(100,2)
#     50
#     '''

#     return a//b
# if __name__=="__main__":
#         import doctest
        # doctest.testmod(name="divide()",verbose=True)


# #complex docstring
# def l1(my_list):
#     '''this function add up 3 in the elements 
#     of the list
#     >>> l1([2, 4, 6])
#     [5, 7, 9]
#     >>> l1([2, 2, 3])
#     [5, 5, 6] 
#     '''
#     return [x+3 for x in my_list]

# if __name__ == "__main__":
#     import doctest
#     doctest.testmod(verbose=True)



 #unit testing
import unittest

def add(a,b):
    return a+b

class Case(unittest.TestCase):

    #cretaing different test cases with the help of methods
    def test_add_positive_number(self):
        self.assertEqual(add(3,2),5)

    def test_subtract_number(self):
        self.assertEqual(add(6,-4),2)

if __name__=="__main__":
    unittest.main()






