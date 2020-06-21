# Given a matrix, return all elements of the matrix in diagonal order.
class DiagonalOrder:
    def __init__(self, matrix):
        self.matrix = matrix
    def printDiagonalOrder(self):
        max_row = len(self.matrix)
        max_col = len(self.matrix[0])
        i = 0
        j = 0
        n = 0
        max_n = max_row + max_col - 1
        while n < max_n:
            #print(n)
            #print("{},{}".format(i,j))
            temp_i = i
            temp_j = j
            while temp_i >= 0 and temp_j < max_col:
                print(self.matrix[temp_i][temp_j])
                temp_i-=1
                temp_j+=1
            n += 1
            if n < max_row:
                i += 1
            if n >= max_row:
                j += 1



if __name__ == "__main__":
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    sol = DiagonalOrder(matrix)
    sol.printDiagonalOrder()
