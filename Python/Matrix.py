import math
class Matrix:
    def __init__(self,arroarr):
        check= True
        n=len(arroarr[0])
        for i in arroarr:
            if (len(i)!=n):
                check=False
        if(check):
            self.matrix = arroarr
            self.m = len(arroarr)
            self.n=len(arroarr[0])
        else:
            raise ValueError("Invalid Dimensions")

    def print(self):
        print('Rows: ',self.m,' Cols: ',self.n)
        for arr in self.matrix:
            for ind in arr:
                print(round(ind,5), end=" ")
            print("\n")

    def peek(self,row,col):
        if(row>self.m or col>self.n):
            raise ValueError("Out of Bounds")
        else:
            return self.matrix[row][col]

    def edit(self,row, col, val):
        if(row>self.m or col>self.n):
            raise ValueError("Out of Bounds")
        else:
            self.matrix[row][col]=val

    def __add__(self, other):
        if(self.m==other.m and self.n==other.n):
            newmat = [[0] * self.n for i in range(self.m)]
            for i in range(0,self.m):
                for j in range(0,self.n):
                    newmat[i][j]=self.peek(i,j)+other.peek(i,j)
            result=Matrix(newmat)
            return result
        else:
            raise ValueError("Invalid Dimensions")

    def __sub__(self, other):
        if(self.m==other.m and self.n==other.n):
            newmat = [[0] * self.n for i in range(self.m)]
            for i in range(0,self.m):
                for j in range(0,self.n):
                    newmat[i][j]=self.peek(i,j)-other.peek(i,j)
            result=Matrix(newmat)
            return result
        else:
            raise ValueError("Invalid Dimensions")

    def __mul__(self, other):
        if(self.n!=other.m):
            raise ValueError("Invalid Dimensions")
            return
        result=[[0]*other.n for l in range(self.m)]
        for i in range(0,self.m):
            for j in range(0,other.n):
                result[i][j]=sum(self.matrix[i][k]*other.matrix[k][j] for k in range(0,other.m))
        R=Matrix(result)
        return R


    def row_scale(self,row,scale):
        if(row>self.m):
            raise ValueError("Out of Bounds")
        else:
            for i in range(0,self.n):
                self.matrix[row][i]=scale*self.matrix[row][i]

    def row_add(self,row1,row2,row2scale):
        if(row1>self.m or row2>self.m):
            raise ValueError("Out of Bounds")
        else:
            for i in range(0,self.n):
                self.matrix[row1][i]=self.matrix[row1][i]+row2scale*self.matrix[row2][i]

    def row_swap(self,row1,row2):
        if(row1==row2):
            return
        elif(row1>self.m or row2>self.m):
            raise ValueError("Out of Bounds")
        else:
            for i in range(0,self.n):
                temp=self.matrix[row1][i]
                self.matrix[row1][i]=self.matrix[row2][i]
                self.matrix[row2][i]=temp

    def transpose(self):
        newmat=[[0]*self.m for i in range(self.n)]
        for i in range(0,self.m):
            for j in range(0,self.n):
                newmat[j][i]=self.peek(i,j)
        result=Matrix(newmat)
        return result

    def determinant(self):
        temp = [[0] * self.m for i in range(self.m)]
        for k in range(self.m):
            for j in range(self.m):
                temp[k][j] = self.peek(k, j)
        T = Matrix(temp)
        if (T.square() == False):
            raise ValueError("Invalid Dimensions")
            return
        result=1
        for i in range(self.m):
            result=result*T.matrix[i][i]

    def REF(self,augment=None):
        c_row=0
        c_col=0
        while(c_row<self.m and c_col<self.n):
            j=c_row
            while(self.matrix[j][c_col]==0):
                j=j+1
                if (j==self.m):
                    break
            if(j!=self.m):
                self.row_swap(j,c_row)
                if(augment):
                    augment.row_swap(j,c_row)
                for i in range(c_row+1,self.m):
                    coeff=-self.matrix[i][c_col]/self.matrix[c_row][c_col]
                    self.row_add(i,c_row,coeff)
                    if(augment):
                        augment.row_add(i,c_row,coeff)
                c_row=c_row+1
                c_col=c_col+1
            else:
                c_col=c_col+1



    def RREF(self,augment=None):
        self.REF(augment)
        c_row=self.m-1
        c_col=self.n-1
        while(c_row>=0 and c_col>=0):
            while(self.matrix[c_row][c_col]==0):
                c_col=c_col-1
            for i in range(c_row-1,-1,-1):
                coeff=-self.matrix[i][c_col]/self.matrix[c_row][c_col]
                self.row_add(i,c_row,coeff)
                if (augment):
                    augment.row_add(i, c_row, coeff)
            c_col = c_col - 1
            c_row = c_row - 1
        for i in range(self.m):
            coeff=1/self.matrix[i][i]
            self.row_scale(i,coeff)
            if(augment):
                augment.row_scale(i,coeff)



    def inverse(self):
        temp=[[0]*self.m for i in range(self.m)]
        for k in range(self.m):
            for j in range(self.m):
                temp[k][j]=self.peek(k,j)
        T=Matrix(temp)
        if(T.square()==False):
            raise ValueError("Invalid Dimensions")
            return
        augment=[[0]*T.m for i in range (T.m)]
        for i in range (T.m):
            augment[i][i]=1
        A=Matrix(augment)
        T.RREF(A)
        return A



    def square(self):
        return(self.m==self.n)

    def sub_matrix_11(self):
        size=self.m//2
        newmat=[[0]*size for i in range(size)]
        for i in range(0,size):
            for j in range(0,size):
                newmat[i][j]=self.matrix[i][j]
        result=Matrix(newmat)
        return result

    def sub_matrix_12(self):
        size = self.m - self.m // 2
        newmat = [[0] * size for i in range(self.m//2)]
        for i in range(0, self.m//2):
            for j in range(self.m//2, self.m):
                newmat[i][j-self.m//2] = self.matrix[i][j]
        result = Matrix(newmat)
        return result

    def sub_matrix_21(self):
        newmat = [[0] * (self.m//2) for i in range(self.m-self.m//2)]
        for i in range(self.m//2, self.m):
            for j in range(0, self.m//2):
                newmat[i-self.m//2][j] = self.matrix[i][j]
        result = Matrix(newmat)
        return result

    def sub_matrix_22(self):
        size=self.m-self.m//2
        newmat = [[0] * size for i in range(size)]
        for i in range(self.m//2, self.m):
            for j in range(self.m//2, self.m):
                newmat[i-self.m//2][j-self.m//2] = self.matrix[i][j]
        result = Matrix(newmat)
        return result

