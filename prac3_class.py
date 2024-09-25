#Class
class Dog:
    atr1="mammal"
    atr2="dog"

#sample methods
    def fun(self):
        print("I m a",self.atr1)
        print("I m a",self.atr2)
    def greet(self):
        print("I hope ur doing well")

# #object instantiation

Rodger= Dog()
print(Rodger.atr1)
print(Rodger.atr2)
Rodger.greet()
Rodger.fun()


class Dog:
    def __init__(self, name, age):  #constructor
        self.name = name            # Attribute 
        self.age = age              # Attribute

    def bark(self):                 # Method
        return "Woof!"
    
dog1 = Dog("Buddy", 3)  # Creating an object of Dog 
dog2 = Dog("Max", 5)    # Another object 

print(dog1.name)  
print(dog1.age)  
print(dog1.bark())  

print(dog2.name)  
print(dog2.age)   
print(dog2.bark()) 



class Animal:
    def __init__(self,name):
        self.name=name

    def speak(self):
        return "Woof!!!"


class Dog(Animal):
    def speak(self):
        return "Wooof!! My name is " + self.name()
    
class Cat(Animal):
    def speak(self):
        return "Meoww!! My name is "+ 
        self.name()
    

#creating objects
dog1=Dog("Tiger")
cat1=Cat("Pluto")

print(dog1.speak())
print(cat1.speak())




#Generator
def cont():
    for i in range(0,5):
        yield i
a=cont()
print(next(a))
print(next(a))

print("BREAKK")

for val in a:
    print(val)  
#Provide an example of a lambda function that sorts a list of tuples by the second value.

l1=[(1,2),(6,3),(4,1)]
a=sorted(l1,key=lambda x:x[1])
print(a)
print(l1)

#Write a Python expression using generator expressions that generates even numbers up to 100.
def even(n):
    for i in range(n+1):
        if i%2==0:
            yield i

a=even(101)
print(next(a))
print(next(a))

for x in a:
    print(x)