'''
Week 6 - Problem Minimum Time Visiting All Points
@author: André Gilbert, andre.gilbert.77110@gmail.com

On a plane there are n points with integer coordinates points[i] = [xi, yi]. 
Your task is to find the minimum time in seconds to visit all points.

You can move according to the next rules:
In one second always you can either move vertically, horizontally by one unit or diagonally (it means to move one unit vertically and one unit horizontally in one second).
You have to visit the points in the same order as they appear in the array.
'''

from typing import List


# O(n) time complexity, O(1) space complexity
def solution(points: List[List[int]]) -> int:
    seconds = 0
    for i in range(len(points) - 1):
        seconds += max(abs(points[i][0] - points[i + 1][0]), abs(points[i][1] - points[i + 1][1]))
    return seconds


# Example usage
if __name__ == "__main__":
    points = [[1, 1], [3, 4], [-1, 0]]
    result = solution(points)
    print(result)