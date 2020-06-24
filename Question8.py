# minimum number of steps to move in a 2D grid.
class Grid:
    def __init__(self, arr):
        self.arr = arr

    def find_minimum_steps(self):
        res = 0
        for i in range(0, len(self.arr)-1):
            res = res + self.min_of_two(self.arr[i], self.arr[i+1])
        print("Min Steps: {}".format(res))

    def min_of_two(self, first, second):
        x1, y1 = first
        x2, y2 = second
        return max(abs(x2-x1), abs(y2-y1))
    
if __name__ == "__main__":
    arr = [(0,0),(1,1),(1,2)]
    sol = Grid(arr)
    sol.find_minimum_steps()
