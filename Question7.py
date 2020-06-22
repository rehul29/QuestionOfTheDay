# Print a given matrix in spiral form. Time O[m*n]. Space O[1]
class Spiral_Order:
    def __init__(self, matrix):
        self.matrix = matrix
    def printSpiralOrder(self):
        m = len(self.matrix) #rows
        n = len(self.matrix[0])  #columns
        #left, right, top, bottom
        l = t = 0
        r = n-1
        b = m-1
        #direction 1 l->r, 2 t->b, 3 r->l, 4 b->t
        dir = 1
        i = j = 0
        while l<=r and t<=b:
            print(self.matrix[i][j])
            if dir == 1:
                j+=1
                if j==r:
                    dir = 2
                    t+=1
            elif dir == 2:
                i+=1
                if i==b:
                    dir = 3
                    r -= 1
            elif dir == 3:
                j-=1
                if j==l:
                    dir = 4
                    b -= 1
            elif dir == 4:
                i-=1
                if i==t:
                    dir = 1
                    l+=1
        print(self.matrix[i][j])

if __name__ == "__main__":
    #matrix = [[1,2,3],[4,5,6],[7,8,9]]
    #matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    matrix = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]]
    sol = Spiral_Order(matrix)
    sol.printSpiralOrder()
            
