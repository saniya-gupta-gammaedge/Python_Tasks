# print("Hello!!,It's day 3")

#lambda function
# x=lambda a:a+10

# print(x(5))

# z=lambda a,b: a // b

# print(z(12,6))

# #with strings
# str1="gamma edge"
# a=lambda string: string.upper()

#print(a(str1))

#finding the cube
# def cube(y):
#     return y*y*y

# lamb_cube=lambda a: a*a*a

# print("using def function the cube is",cube(5))
# print("using lambda function t he cube is",lamb_cube(5))

#lamda function with list comprehension

# is_even_list = [lambda arg=x: arg * 10 for x in range(1, 5)]
# for item in is_even_list:
#     print(item())

#filter function
# t1=(1,2,3,4,5,6,7,8,9,10)
# a=list(filter(lambda x:(x % 2 != 0), t1))
# print(a)

# age=[21,25,10,60,20,14,11,10,6,26]
# a=list(filter(lambda age:(age >18),age))
# print(a)

#map function
l1=[1,2,3,4,5,6,7,8,9]
b=list(map(lambda x:(x*2),l1))
print(b)

z=list(map(lambda x: (x*2) ,range(1,11)))
print(z)

#iterator

cities = ["Berlin", "Vienna", "Zurich"]

iterator_obj = iter(cities)

print(next(iterator_obj))
print(next(iterator_obj))
print(next(iterator_obj))
