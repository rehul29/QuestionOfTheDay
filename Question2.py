#Print all the triplet in the array whose sum is equal to a given sum. Please try to solve in minium complexity.
from random import random
from random import shuffle
import datetime

class Triplet:
    def __init__(self, sum, arr):
        print("sum: {}".format(sum))
        print("arr: {}".format(arr))
        self.sum = sum
        self.arr = arr
    def brute_force(self):
        for i in range(0,len(self.arr)):
            for j in range(i+1, len(self.arr)):
                for k in range(j+1, len(self.arr)):
                    if arr[i]+arr[j]+arr[k] == self.sum:
                        print("{}+{}+{}".format(arr[i],arr[j],arr[k]))
                        continue
    
    def sorted_arr(self):
        self.arr.sort()
        for i in range(0, len(self.arr)-2):
            left = i+1
            right = len(self.arr) - 1
            while right > left:
                temp_sum = arr[i] + arr[left] + arr[right]
                if temp_sum == self.sum:
                    print("{}+{}+{}".format(arr[i],arr[left],arr[right]))
                    left = left + 1
                    right = right - 1
                elif temp_sum < sum:
                    left = left + 1
                elif temp_sum > sum:
                    right = right - 1

    def hash_set(self):
        for i in range(0, len(self.arr)-1):
            hash_set_ds = set()
            for j in range(i+1, len(self.arr)):
                if (self.sum - (arr[i] + arr[j])) in hash_set_ds:
                    print("{}+{}+{}".format(arr[i],arr[j],self.sum - (arr[i] + arr[j])))
                else:
                    hash_set_ds.add(arr[j])
    
if __name__ == "__main__":
    #testcases
    sum = 25
    arr = [22,1,2,3,0,21,4,5]
    sol = Triplet(sum, arr)
    sol.brute_force()
    sol = Triplet(sum, arr)
    sol.sorted_arr()
    sol = Triplet(sum, arr)
    sol.hash_set()    

    sum = int(random()*1000 + 6)
    arr = []
    for i in range(0, int(random()*1000)):
        arr.append(int(random()*1000))
    arr = list(set(arr))
    shuffle(arr)
    start = datetime.datetime.now()
    sol = Triplet(sum, arr)
    sol.brute_force()
    end = datetime.datetime.now()
    brute_force_time = end-start
    
    start = datetime.datetime.now()
    sol = Triplet(sum, arr)
    sol.sorted_arr()
    end = datetime.datetime.now()
    sorted_arr_time = end-start

    start = datetime.datetime.now()
    sol = Triplet(sum, arr)
    sol.hash_set()
    end = datetime.datetime.now()
    hash_set_time = end-start
    
    print("Brute Force Method Duration: {}".format(str(brute_force_time)))
    print("Sorted Array Method Duration: {}".format(str(sorted_arr_time)))
    print("Hash Set Method Duration: {}".format(str(hash_set_time)))
