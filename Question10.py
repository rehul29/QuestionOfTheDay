# Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. Array can contain duplicated. The time complexity must be in O(n).
import math
class ThirdLargest:
    def __init__(self, arr):
        self.arr = arr
    def findThirdLargest(self):
        first = second = third = float('-inf')
        for i in range(0, len(self.arr)):
            if self.arr[i] > first:
                third = second
                second = first
                first = self.arr[i]
        if math.isinf(third):
            return first
        return third

if __name__ == "__main__":
    arr = [1,3,3,3,4]
    print(ThirdLargest(arr).findThirdLargest())
