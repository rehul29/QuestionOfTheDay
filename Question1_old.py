import unittest
import random
class Question1(object):

    def __init__(self, array):
        self.array = array
    
    def bin_search(self, key, min_index, max_index):
        if max_index >= min_index:
            pivot = (min_index + max_index) //2
            if self.array[pivot] == key:
                return pivot
            if self.array[min_index] <= key and key <= self.array[pivot]:
                return self.bin_search(key, min_index, pivot-1)
            else:
                return self.bin_search(key, pivot+1, max_index)
        else:
            return -1
    
    def search(self, key):
        return self.bin_search(key, 0, len(self.array)-1)
        
class TestCases(unittest.TestCase):
    def test1(self):
        array = [5,7,8,10,1,3]
        key = 3
        q = Question1(array)
        ans = q.search(key)
        print("=========== TestCase 1 =============")
        print("array : {}".format(array))
        print("key : {}".format(key))
        assert array[ans] == key
    def test2(self):
        array = []
        for i in range (1,10000):
            array.append(random.randint(1,100000))
        array = list(set(array))
        array.sort()
        rotation_index = random.randint(0,len(array)-1)
        array = array[rotation_index:] + array[0:rotation_index]
        index = random.randint(0,len(array)-1)
        key = array[index]
        q = Question1(array)
        ans = q.search(key)
        print("=========== TestCase 2 =============")
        print("array : {}".format(array))
        print("key : {}".format(key))
        assert array[ans] == key

if __name__=="__main__":
    unittest.main()
