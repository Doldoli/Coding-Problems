'''
Week 6 - Problem Self-dividing Number 
@author: André Gilbert, andre.gilbert.77110@gmail.com

A self-dividing number is a number that is divisible by every digit it contains.
Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.
The boundaries of each input argument are 1 <= left <= right <= 1000.
'''

# input: left = 1, right = 15
# output = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15]
# for example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, 128 % 8 == 0

left, right = 1, 100