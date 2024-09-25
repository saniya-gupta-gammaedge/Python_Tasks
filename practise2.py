#print("Day 2 begins")

#exception handling

#try and except error handling
# a=5
# try:
#     print(a/0)
# except:
#     print("Zero division error occur")

#type error
# a=10
# b="Gamma"
# try:
#     print(z=a+b)
# except:
#     print("Error:two different data types cannot be added")


# # #Index Error
# a = [1, 2, 3]
# try: 
#     print ("Second element = %d",(a[1]))

#     print ("Fourth element = %d",(a[3]))

# except:
#     print ("An error occurred")

    
# #give more than one except clause

# def func(a):
#     if a<=10:
#         b=a/(a-10)
#         print("Value of b is",b)
# try:
#     func(10)
#     func(11)
# except ZeroDivisionError:
#     print("Zero division error occur")
# except NameError:
#     print("Name error occured")

    
# #use of finally keyword
# a=3
# b=a-a
# try:
#     c=a-b
#     print("Value of c is",c)
# except ZeroDivisionError:
#     print("A zero division error occured")
# finally:
#     print("This is always executed")

# #raising the error
# try:
#     raise NameError("Hii there")
# except:
#     print("This is the error")
#     raise

# print("This is it from exception")

# import regex as re
# import re

# text = "The cat is on the roof."
# pattern = "cat"

# # Search for the pattern
# match = re.search(pattern, text)

# if match:
#     print("Match found:",match.group())
# else:
#     print("No match found.")

# #match function

# text = "Hello, world!"
# # ^ indicates the start of the string
# pattern = "^Hello"  

# if re.match(pattern, text):
#     print("The text starts with 'Hello'")
# else:
#     print("The text does not start with 'Hello'.")

    #decorator


# my_deco()

# def my_d(abc):
#         def start(fun):
#                 print("initial step")
#                 abc(fun)
#                 print("Final step")
#         return start

# @my_d
# def my_deco(fun):
#         print("Understand Decorator")

# my_deco(1)

#another decorator function

def my_decorator(z):
#this is the wrap function
        def my_first():
                print("Hello Gamma")
                z()
                print("See  u tomorrow")
        return my_first


@my_decorator
def my_func():
        print("Hello Friends")

my_func()

