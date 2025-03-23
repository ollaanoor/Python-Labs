#Q1
# name = input("Enter your first and last name: ").split()
# print(name[0] + " " + name[1])

#Q2
# n = input("Enter a number: ")
# num1, num2, num3 = n, n*2, n*3
# result = int(num1) + int(num2) + int(num3)
# print(result)

#Q3
# text = """ 
# This 
# is a ..... multi-line
# heredoc string
# """
# print(text)

#Q4
# import math
# radius = int(input("Enter radius: "))
# print((4/3) * math.pi * (radius ** 3))

#Q5
# import math
# base = int(input("Enter base: "))
# height = int(input("Enter height: "))
# area = (1/2) * base * height
# print(f"Area is: {area}")

#Q6
# for i in range(9):
#     if(i >= 5):
#         count = 9 - i
#     else:
#         count = i + 1
#     for j in range(count):
#         print("*", end="")
#     print()

#Q7
# word = input("Enter a word: ")
# print(word[::-1])

#Q8
# for i in range(6):
#     if(i==3 or i==6):
#         pass
#     else:
#         print(i)

#Q9
# fib = []
# i = 0
# while(len(fib) == 0 or fib[-1] < 50):
#     if(i==0 or i==1):
#         fib.append(i)
#     else:
#         fib.append(fib[i-1]+fib[i-2])
#     i += 1
# print(fib[1:-1])

#Q10
# string = input("Enter a string: ")
# letter = digit = 0
# for i in range(len(string)):
#     if(string[i].isalpha()):
#         letter +=1
#     else:
#         digit +=1
# print(f"{letter} letters and {digit} digits")