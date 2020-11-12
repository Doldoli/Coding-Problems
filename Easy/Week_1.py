'''
Week 1 - Coding Problems
@author: André Gilbert
note: every problem should be solved with an algorithm that can be used on a input with N amount of elements!
'''

# Task 1
# Change the given list into a nested list, each list contains 5 elements with index 0 - 4.
#
# [['Python', 'Java', 'R', 'C#', 'Typescript'], ['C++', 'Golang', 'PHP', 'Javscript, 'Kotlin'], ['Swift']]
#
list_task_1 = ['Python', 'Java', 'R', 'C#', 'Typescript', 'C++', 'Golang', 'PHP', 'Javascript', 'Kotlin', 'Swift']
nums_of_elements_per_list = 5

# Task 2
# Find N largest elements from a list.
#
# input = [4, 5, 1, 2, 9]
# n = 2
# output = [9, 5]
#
list_task_2 = [81, 52, 45, 10, 3, 2, 96, 123, 100, 43, 30, 15, 95, 32, 46, 74, 80, 12, 32, 44, 11, 22, 88, 90, 121, 56]
n_largest_elements = 3

# Task 3
# Find cumulative sum of a list.
#
# array = [10, 20, 30, 40, 50]
# func => [10, 10 + 20, 30 + 30, 60 + 40, 100 + 50]
# output = [10, 30, 60, 100, 150]
#
list_task_3 = [4, 10, 15, 18, 20, 1, 23, 534, 6, 23, 1, 66435, 42, 23, 546, 7, 76, 45, 867, 45654, 7657, 254, 6, 5]

# Task 4
# Output the string representation of numbers from 1 to n
# But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”.
# For numbers which are multiples of both three and five output “FizzBuzz”.
#
# n = 15
# output = ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]
#
n = 30

# Task 5
# Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.
#
# array = [0 ,0 ,1 ,1 ,1 ,2 ,2 ,3 ,3 ,4]
# output = 5 (length of array)
#
list_task_5 = [0, 0, 7, 7, 7, 2, 2, 1, 1, 4, 1, 1, 4, 4, 9, 9, 3, 3, 6, 6, 3, 0]
