# Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.
class EvenOdd:
    def __init__(self, arr):
        self.arr = arr
    def sortEvenOdd(self):
        start = 0
        for i in range(0, len(self.arr)):
            if i % 2:
                self.arr[start], self.arr[i] = self.arr[i], self.arr[start]
                start+=1
        print(self.arr)

if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8,9]
    sol = EvenOdd(arr)
    sol.sortEvenOdd()
