# Replace Elements with Greatest Element on Right Side. Details in Q2 tab
class Greatest_Right:
    def __init__(self, arr):
        self.arr = arr
    def replace_with_greatest_right(self):
        g_indices = []
        max = 1
        g_indices.append(len(self.arr)-1) 
        max = self.arr[len(self.arr)-1]
        for i in range(len(self.arr)-1,0,-1):
            if self.arr[i] > max:
                g_indices.append(i)
                max = self.arr[i]
        temp = g_indices.pop()
        for i in range(0,len(self.arr)-1):
            if temp <= i:
                temp = g_indices.pop()
            self.arr[i] = self.arr[temp]
        self.arr[len(self.arr)-1] = -1
        print("Final Array: {}".format(self.arr))

if __name__=="__main__":
    sol = Greatest_Right([17,18,5,4,6,1])
    sol.replace_with_greatest_right()            
