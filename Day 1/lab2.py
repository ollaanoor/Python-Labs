#Q1
# def reducedList(nums):
#     for i in range(len(nums)-1):
#         if(nums[i] == nums[i+1]):
#             nums.pop(i+1)
#     return nums

# print(reducedList([1,2,3,3]))

#Q2
# def halvingStr(string):
#     if(len(string)%2 == 0):
#         front = string[0:len(string)//2]
#         back = string[len(string)//2:]
#     else:
#         front = string[0:(len(string)//2)+1]
#         back = string[(len(string)//2)+1:]
#     return front,back

# a_front, a_back = halvingStr("abced")
# b_front, b_back = halvingStr("fghi")
# print((a_front + b_front) + (a_back + b_back))


#Q3
# def distinctVals(nums):
#     if len(set(nums)) == len(nums):
#         return True
#     else:
#         return False

# print(distinctVals([1,5,7,9]))
# print(distinctVals([2,4,5,5,7,9]))

#Q4 - Bubble Sort
# def bubbleSort(nums):
#     for i in range(len(nums)):
#         for j in range(0, len(nums)-i-1):
#             if (nums[j] > nums[j + 1]):
#                 temp = nums[j]
#                 nums[j] = nums[j + 1]
#                 nums[j + 1] = temp
#     return nums

# print(bubbleSort([1,5,3,9,22,55,12,2]))

#Q5 - Guess Game
# import random

# random_number = random.randint(1,100)
# tries = 10
# guesses = []

# while True:
#     if tries > 0:
#         guess = int(input("Enter your guess in range 1-100: "))
#         if(guess == random_number):
#             print("Congratulations!")
#             random_number = random.randint(1,100)
#             guesses.clear()
#         elif not(guess in range(101)):
#             print("Make sure to enter a number between 1 and 100")
#             continue
#         elif guess < random_number:
#             print("The number you entered is smaller than the random number")
#         elif guess > random_number:
#             print("The number you entered is greater than the random number")
#         elif guess in guesses:
#             print("You have entered this number before")
#             continue
        
#         tries -= 1
#         guesses.append(guess)
#     else:
#         res = input("Game Over.\nDo you want to play again? y or n: ")
#         if res == 'y':
#             random_number = random.randint(1,100)
#             tries = 10
#             guesses.clear()
#         elif res == 'n':
#             break
#         else:
#             print("Enter a valid option")

#Q6 - HackerRank: Diagonal Difference Problem
# arr = [[1, 2, 3],
#        [4, 5, 6],
#        [9, 8, 9]]

# def diagonalDifference(arr):
#     LRdiag = 0 
#     RLdiag = 0  
#     for i in range(len(arr)):
#         LRdiag += arr[i][i]
#         RLdiag += arr[i][len(arr)-1-i]
#     return abs(LRdiag - RLdiag)

# print(diagonalDifference(arr))
