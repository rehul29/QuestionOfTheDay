# Median of two sorted array (Frequently asked in interviews). 
class Median:
    def __init__(self, arr1, arr2):
        self.arr1 = arr1
        self.arr2 = arr2
    
    def findMedian(self):
        length = len(self.arr1) + len(self.arr2)
        n = length//2
        i1 = 0
        i2 = 0
        median = 0
        for i in range(0,n+2):
            if i == n or (i == n-1 and length % 2 == 0):
                if arr1[i1] < arr2[i2]:
                    median += arr1[i1]
                    i1 += 1
                else:
                    median +=arr2[i2]
                    i2 += 1
            else:
                if arr1[i1] < arr2[i2]:
                    i1 += 1
                else:
                    i2 += 1
        if length % 2 == 0:
            median = median/2.0
        print("Median: {}".format(median))

if __name__ == "__main__":
    arr1 = [0,1,3,5,6,7,9]
    arr2 = [3,5,5,6,7,7,8,9]
    # 0, 1, 3, 3, 5, 5, 5, *6, 6, 7, 7, 7, 8, 9, 9 = 6
    sol = Median(arr1, arr2)
    sol.findMedian()
    arr1 = [0,1,3,5,6,7,9]
    arr2 = [3,5,5,6,7,7,8]
    # 0, 1, 3, 3, 5, 5, *5, *6, 6, 7, 7, 7, 8, 9 = 5.5
    sol = Median(arr1, arr2)
    sol.findMedian()

