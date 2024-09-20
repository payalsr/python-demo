# name = input('Enter Name ')
# zip_code = int(input('Enter zip code '))
# street = input('Enter street name ')
# house_number = int(input('Enter house number '))

# # Display all values separated by hyphen
# print(name, zip_code, street, house_number,sep="-")
# try:
#     a = int(input("Enter value of a:"))
#     b = int(input("Enter value of b:"))
#     c = a/b
#     print("The answer of a divide by b:", c)
# except ValueError:
#     print("Entered value is wrong")
# except ZeroDivisionError:
#     print("Can't divide by zero")
# var = "James" * 2  * 3
# print(var)
# listOne = [20, 40, 60, 80]
# listTwo = [20, 40, 60, 80]

# print(listOne == listTwo)
# print(listOne is listTwo)
# str = "pynative"
# print (str[1:3])
# for x in range(0.5, 5.5, 0.5):
#   print(x)
# x = 36 / 4 * (3 +  2) * 4 + 2
# print(x)
# var1 = '1'
# var2 = "2"
# var3 = "3"

# print(var1 + var2 + var3)
# def calculate (num1, num2=4):
#   res = num1 * num2
#   print(res)

# calculate(5, 6)
# for i in range(1, 5):
#     print(i)
# else:
#     print("this is else block statement" )
# var= "James Bond"
# print(var[9::-1])
# sampleList = ["Jon", "Kelly", "Jessa"]
# sampleList.insert(2,"Scott")
# print(sampleList)
# sampleList = ["Jon", "Kelly", "Jessa"]
# sampleList.append("Scott")
# print(sampleList)
# p, q, r = 10, 20 ,30
# print(p, q, r)
#add and appen takes one arg for added elemnt at the end
# sampleSet = {"Jodi", "Eric", "Garry"}
# sampleSet.add( "Vicki")
# print(sampleSet)
# for i in range(10, 15, 1):
#   print( i, end=', ')
# salary = 8000

# def printSalary():
#   salary = 12000
#   print("Salary:", salary)
  
# printSalary()
# print("Salary:", salary)
# valueOne = 5 ** 2
# valueTwo = 5 ** 3

# print(valueOne)
# print(valueTwo)
# x = 50
# def fun1():
#     x = 25
#     print(x)
    
# fun1()
# print(x)
# x = 75
# def myfunc(x):
   
#     x = x + 1
#     print(x)

# myfunc()
# print(x)
# print(type(10))
# str1 = 'Ault\'Kelly'
# print(str1)
# print(bool(0), bool(3.14159), bool(-3), bool(1.0+1j))
# x = 50
# def fun1():
#      global x
#      x = 20
# fun1()
# print(x) # it should print 20
# print(type(range(5)))
# print(type([]) is list)
# def func1():
#     x = 50
#     return x
# func1()
# print(x)
# aTuple = (1, 'Jhon', 1+3j)
# print(type(aTuple[2:3]))
# print(type(0xFF))
# print(2 * 3 ** 3 * 4)
# a = 4
# b = 11
# print(a | b)
# print(a >> 2)
# y = 10
# x = y += 2
# print(x)
# x = 6
# y = 2
# print(x ** y)
# print(x // y)
# print(bool(0), bool(3.14159), bool(-3), bool(1.0+1j))
# print(-18 // 4)
# x = 100
# y = 50
# print(x and y)
# print(2%6)
# x = 10
# y = 50
# if x ** 2 > 100 and y < 100:
#     print(x, y)
# print('%x, %X' % (15, 15))
# f = open("test.txt", "r")
# print(f.readline(3))
# f.close()
# print('PYnative ', end='//')
# print(' is for ', end='//')
# print(' Python Lovers', end='//')
# print(sep='--', 'Ben', 25, 'California')

# print('[%c]' % 65)
# def display(**kwargs):
#     for i in kwargs:
#         print(i)

# display(emp="Kelly", salary=9000)
# def add(a, b):
#     return a+5, b+5

# result = add(3, 2)
# print(result)
# def fun1(name, age=20):
#     print(name, age)

# fun1('Emma', 25)
# def outer_fun(a, b):
#     def inner_fun(c, d):
#         return c + d

#     return inner_fun(a, b)
#     return a

# result = outer_fun(5, 10)
# print(result)
# x = 0
# while (x < 100):
#   x+=2
# print(x)
# x = 0
# for i in range(10):
#   for j in range(-1, -10, -1):
#     x += 1
#     print(x)
# var = 10
# for i in range(10):
#     for j in range(2, 10, 1):
#         if var % 2 == 0:
#             continue
#             var += 1
#     var+=1
# else:
#     var+=1
# print(var)
# a, b = 12, 5
# if a + b:
#     print('True')
# else:
#   print('False')
# for num in range(2,-5,-1):
#     print(num, end=", ")
# numbers = [10, 20]
# items = ["Chair", "Table"]

# for x,y in zip(numbers,items):
#    print(x,y)
# list1 = [5, 10, 15] 
# list2 = ['apple', 'banana', 'cherry'] 
 
# for i in range(len(list1)): 
#     print(list1[i], list2[i]) 
# print( 3.3 == 3.3 )
# z = complex(1.25)
# print(z)
# import math
# print(math.ceil(252.4))#next value 253
# print(math.floor(252.4))#avrg value 252
# print(abs(-45.300))45.3
# print(0b101)
# print(0o10)
# print(0x1F)
# x = -5j
# print(type(x))
# print(int(2.999))
# str1 = "my isname isisis jameis isis bond"
# sub = "is"
# print(str1.count(sub, 4))#starting from 4 th index
# str1 = 'Welcome'
# print(str1*2)
# l = [None] * 10
# print(len(l))
# sampleList = [10, 20, 30, 40]
# del sampleList[0:6]
# print(sampleList)
# aList = [4, 8, 12, 16]
# aList[1:4] = [20, 24, 28]
# print(aList)
# my_list = ["Hello", "Python"]
# print("-".join(my_list))
# aList = [5, 10, 15, 25]
# print(aList[::-3])
# age = 36
# print( f"My name is John, I am {age}")
import random

# print(random.randint(3, 9))
# print(random.randrange(3, 9))

# mylist = ["apple", "banana", "cherry"]

# print(random.choice(mylist))

# mylist = ["apple", "banana", "cherry"]

# print(random.choices(mylist, weights = [10, 1, 1], k = 14))
import json
# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)C:
# some JSON:
# x = '{ "name":"John", "age":30, "city":"New York"}'

# # parse x:
# y = json.loads(x)

# # the result is a Python dictionary:
# print(y["age"])
# import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password=""
# )

# print(mydb)
# from datetime import datetime

# now = datetime.now()
# print('Current DateTime:', now)
# print('Type:', type(now))