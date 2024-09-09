from idlelib.sidebar import LineNumbers

import numpy as np
from matplotlib import pyplot as plt
from numpy.matrixlib.defmatrix import matrix
from Matrix import Matrix
import matplotlib

def mesh_grid(beta):
    x1=np.arange(0,101,1)
    x2=np.arange(0,101,1)
    X1,X2=np.meshgrid(x1,x2)
    Y=beta.matrix[0]*X1+beta.matrix[1]*X2
    ctr = plt.contour(X1, X2, Y, levels=100, colors='k')
    fil = plt.contourf(X1, X2, Y, levels=100)
    plt.clabel(ctr)
    plt.colorbar(fil)
    plt.xlabel('x1')
    plt.ylabel('x2')
    plt.title('y=5x1+3x2')
    plt.show()

def two_variable(X,Y):
    x1=[0]*X.m
    x2=[0]*X.m
    y = [0] * Y.m
    for i in range (X.m):
        x1[i]=X.matrix[i][0]
        x2[i]=X.matrix[i][1]
    for i in range (Y.m):
        y[i]=Y.matrix[i][0]
    plt.tricontourf(x1, x2, y)
    plt.colorbar()
    plt.xlabel('x1')
    plt.ylabel('x2')
    plt.show()


def one_variable(Y,X,beta):
    x1 = [0] *(X.m)
    y=[0] *(Y.m)
    for i in range (X.m):
        x1[i]=X.matrix[i][0]
    for i in range (Y.m):
        y[i]=Y.matrix[i][0]
    ynew=[beta.matrix[0][0]*x1 for x1 in range(200)]
    plt.plot(x1,y,'ro')
    plt.plot([i for i in range(200)],ynew)
    plt.title('Scatter Plot of Sample Data and Best Fit Line')
    plt.xlabel('x1')
    plt.ylabel('y')
    plt.axis((0,200,0,1000))
    plt.show()

def poly_plot(Coeff,X):
    y=[0 for j in range(X.m)]
    x=[0 for j in range(X.m)]
    for row in range(X.m):
        temp=0
        x[row]=X.matrix[row][1]
        for i in range(X.n):
            temp=temp+Coeff[i]*X.matrix[row][i]
        y[row]=temp
    plt.plot(x,y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Curve Fit')
    plt.show()
def two_plot(x,y):
    plt.title('Original Sample Data')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.scatter(x, y)
    plt.show()