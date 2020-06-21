# Remove Duplicated from sorted array. Time O[N]. Space O[1]
class RemoveDuplicatesFromSortedArray:
    def __init__(self, arr):
        self.arr = arr
    def remove_duplicates(self):
        i=0
        j=0
        while j<len(self.arr):
            if self.arr[j]==self.arr[i]:
                j+=1
                continue
            i+=1
            self.arr[i] = self.arr[j]
        self.arr = self.arr[0:i+1]
        print("final arr:{}".format(self.arr))

if __name__ == "__main__":
    arr = [1,1,1,1,2,2,2,3]
    sol = RemoveDuplicatesFromSortedArray(arr)
    sol.remove_duplicates()
