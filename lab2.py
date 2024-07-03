# Lab 2 Solution

# While loop

count = 5
while(count<5):
    count = count + 1
    print(f"Count number: {count}")


# Single Statement While Loop
count = 0
while(count == 10): print("Hello")


# For Loop
list = ["Apex Legends", "Resident Evil 4", "God of War"]
for i in list:
    print(i)

# Tuple
tuple = ("Apex Legends", "Resident Evil 4", "God of War")
for i in tuple:
    print(i)

# String
string = "Umar"
for i in string:
    print(i)

# Loop Control
# Break

string = "Umar"
for letter in string:
    if letter == "a":
        break

print(f"Current letter is: {letter}")

# Continue

string = "Umar"
for letter in string:
    if letter == "a":
        continue

print(f"Current letter is: {letter}")


# Functions

def my_function(a):
    print(a)
    print(type(a))


my_function(1.00)


def function(country):
    for i in country:
        print(i)

country = ["Pakistan", "China", "Spain"]

function(country)

def func(number):
    return 5*number

print(func(5))

# Keyword Arguments

def my_func(anime1, anime2, anime3):
    print("The most popular is: " + anime1)

my_func("Naruto", "Bleech", "One Piece")


# Classes and Objects

# Classes

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myFunction(self):
        print(f"My name is {self.name} & age is {self.age}")


p1 = Person("Umar", "22")
p1.myFunction()




