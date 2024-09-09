from numpy.matrixlib.defmatrix import matrix
from Matrix import Matrix
import numpy as np

def generate_in(sample_size, feature_size):
    data=[[0]*feature_size for i in range(sample_size)]
    for i in range(sample_size):
        for j in range(feature_size):
            data[i][j]=np.random.randint(100)
    X=Matrix(data)
    return X

def generate_out(A,X):
    Y=X*A
    add_noise(Y,5)
    return Y

def add_noise(A,max):
    for i in range(A.m):
        for j in range(A.n):
            A.matrix[i][j]=A.matrix[i][j]+np.random.rand()*max

def get_point(beta,x0,x1):
    return (float(beta.matrix[0][0])*float(x0)+float(beta.matrix[1][0])*float(x1))

