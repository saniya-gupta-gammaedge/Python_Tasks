#pytesting

# import pytest

# def add(a,b):
#     return a+b

# def test_add():
#     assert add(3,4)==7
#     # assert add(4,9)==13
#     # assert add(5,5)==10



# import math

# def test_sqr():
#     num=16
#     assert math.sqrt(num)==4

# def test_case():
#     num=7
#     assert num*7==49

# import unittest
# def add(a,b):
#     return a+b

# class TestMath(unittest.TestCase):
    
#     def test_add(self):
#         self.assertEqual(add(1, 2), 3)

#     def test_subtract(self):
#         self.assertEqual(add(2, -1), 1)

# # Create a test suite using TestLoader
# def suite():
#     loader = unittest.TestLoader()
#     return loader.loadTestsFromTestCase(TestMath)

# # Run the test suite
# if __name__ == '__main__':
#     runner = unittest.TextTestRunner()
#     runner.run(suite())



import pytest

def add(a,b):
    return a+b

@pytest.mark.parametrize("a,b,expected",[
(1,2,3),
(3,4,7)])

def test_add(a,b,expected):
    assert add(a,b)==expected