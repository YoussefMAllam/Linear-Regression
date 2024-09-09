from random import sample, random

import numpy as np
from Matrix import Matrix

def build_poly(sample_size,degree):
    samples=poly_samples(sample_size)
    x=[[0]*(degree+1) for i in range(sample_size)]
    for i in range(sample_size):
        for j in range(degree+1):
            x[i][j]=pow(samples[i],j)
    X=Matrix(x)
    return X

def poly_samples(sample_size):
    x=[0 for i in range (sample_size)]
    for i in range(sample_size):
        x[i]=np.random.randint(100)
    return x

def build_out(Coeff,poly):
    y = [0 for j in range(poly.m)]
    x = [0 for j in range(poly.m)]
    for row in range(poly.m):
        temp = 0
        x[row] = poly.matrix[row][1]
        for i in range(poly.n):
            temp = temp + Coeff[i] * poly.matrix[row][i]
        y[row] = temp
    return y
def add_poly_noise(y,max):
    for i in range(len(y)):
        y[i]=y[i]+np.random.rand()*max
    return y
