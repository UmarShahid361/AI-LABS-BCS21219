# Program to find numbers divisible by 7 and multiple of 5

for i  in range(1500,2701):
    if(i%7==0) and (i%5==0):
        print(i)


# Converter for temperature

def convert_celsius_to_fahrenheit(celsius):
  """Converts Celsius to Fahrenheit."""
  fahrenheit = (9/5) * celsius + 32
  return fahrenheit

def convert_fahrenheit_to_celsius(fahrenheit):
  """Converts Fahrenheit to Celsius."""
  celsius = (5/9) * (fahrenheit - 32)
  return celsius

# Get user input
temperature_value = float(input("Enter the temperature value: "))
temperature_unit = input("Enter the unit (C for Celsius, F for Fahrenheit): ").upper()

# Perform conversion and print result
if temperature_unit == 'C':
  converted_temperature = convert_celsius_to_fahrenheit(temperature_value)
  print(f"{temperature_value} degrees Celsius is equal to {converted_temperature} degrees Fahrenheit.")
elif temperature_unit == 'F':
  converted_temperature = convert_fahrenheit_to_celsius(temperature_value)
  print(f"{temperature_value} degrees Fahrenheit is equal to {converted_temperature} degrees Celsius.")
else:
  print("Invalid unit. Please enter C or F.")




# Program to guess a number between 0 and 9

x = 5
while True:
  guess = int(input("guess a number between 1 to 9:  "))
  if guess == x :
    print("Congratulations! you guessed a number prcisely")
    break
  else:
    print("plz try again !")



# Design a pattern using nested loop

# Increasing pattern
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()

# Decreasing pattern
for i in range(4, 0, -1):
    for j in range(i):
        print("*", end="")
    print()


# Reverse the accepted words from the user

x = input("plz enter a word:  ")
reversed_word = reversed(x)
print(''.join(reversed_word))



# Program to count even and odd numbers

numbers = (1,2,3,4,5,6,7,8,9)
count_even = 0
count_odd =0
for i in numbers:
  if i%2==0:
    count_even =count_even+1
  else:
    count_odd = count_odd+1

print(f'"count_even : "{count_even}    "count_odd : "{count_odd}')


#A program which prints the item and its type from a list

list = [1452,11.23,1+2j,True,'w3resource',(0,-1),[5,12],{"class":'V', "section":'A'}]
print(list[2])
print(type(list[2]))


#A program whhich prints all numbers from 0 to 6 except 3 and 6

for i in range(0,7):
  if i == 3 or i == 6:
    continue
  else:
   print(i)

list = []
for i in range(0,50):
  list.append(i)


number_previous =list[0]
number_current_previous = list[1]

fibonacci_list = [0,1]
for i in range(3,11):
  fib_num = number_previous+number_current_previous
  fibonacci_list.append(fib_num)
  number_previous = number_current_previous
  number_current_previous = fib_num


print(fibonacci_list)


#A program to get the Fibonacci series between 0 to 50

list = []
for i in range(0,50):
  list.append(i)


number_previous =list[0]
number_current_previous = list[1]

fibonacci_list = [0,1]
for i in range(3,11):
  fib_num = number_previous+number_current_previous
  fibonacci_list.append(fib_num)
  number_previous = number_current_previous
  number_current_previous = fib_num


print(fibonacci_list)


#A program which prints "Fizz" for numbers of multiple of 3 and print "buzz" for multipule of 5 and print "FizzBuzz" for both

for i in range(1,51):
  if i%3==0 :
    print("Fizz")
  elif(i%5==0):
    print("Buzz")
  elif(i%3==0 and i%5==0):
    print("FizzBuzz")
  else:
    print(i)


#A program that accepts sequence of charachter lines  and prints in lower case

string =  '''I AM UMAR SHAHID A SOFTWARE DEVELOPER'''
print(string.lower())


# A program which accepts a binary number of 4 digits and print that  which is divisible of 5

list = []
for i in range(1,5):
  x = int(input("plz enter 4 digits binary numbers : "))
  list.append(x)

print(list)
for i in range(len(list)):
  if int(list[i])%5==0:
    print(list[i])

#A progarm which accepts a tring and count alphabets and digit in it

string = "Python 3.2 "
count_alpha = 0
count_digit = 0
for char in string:
  if char.isalpha():
    count_alpha += 1
  elif char.isdigit():
    count_digit += 1

print("Letters: ", count_alpha)
print("Digits: ", count_digit)


#A program takes row(m) and column(n) as input and generates two_dimentional array and the elenments should be i*j


# Get input for number of rows and columns
m = int(input("Enter the number of rows: "))
n = int(input("Enter the number of columns: "))

# Create a 2D array filled with zeros
array_2d = [[0 for j in range(n)] for i in range(m)]

# Fill the array with i*j
for i in range(m):
  for j in range(n):
    array_2d[i][j] = i * j

# Print the 2D array
print(array_2d)