from numpy.matrixlib.defmatrix import matrix

from Matrix import Matrix
from Data import generate_in, add_noise, generate_out, get_point
from Plotting import two_variable, one_variable, mesh_grid, poly_plot, two_plot
import numpy as np
from matplotlib import pyplot as plt
from poly import build_poly, build_out, add_poly_noise

# ##Single Variable
# #GENERATE SAMPLE DATA
# X = generate_in(100, 1)
# Coeff = Matrix([[5]])
# Y = generate_out(Coeff, X)
#
# # SOLVE FOR BETA USING NORMAL EQUATION
# BETA = (X.transpose() * X).inverse() * X.transpose() * Y
#
# #Plot Sample Data and Predicted Values
# one_variable(Y,X,BETA)
# plt.plot([i for i in range(200)],[5*i for i in range(200)])
# plt.title('y=5x1')
# plt.xlabel('x1')
# plt.ylabel('y')
# plt.axis((0,200,0,1000))
# plt.show()


# ##Multivariable
# #GENERATE SAMPLE DATA
# X=generate_in(1000,2)
# Coeff=Matrix([[5],[3]])
# Y=generate_out(Coeff,X)
# #SOLVE FOR BETA USING NORMAL EQUATION
# BETA=(X.transpose()*X).inverse()*X.transpose()*Y
#
# ##GRAPH CONTOUR PLOT
# mesh_grid(BETA)
# two_variable(X,Y)
# mesh_grid(Coeff)


# #CALCULATE MSE
# y_hat=[[0]*Y.n for i in range(Y.m)]
# Y=X*Coeff
# for i in range(X.m):
#     y_hat[i][0]=get_point(BETA,X.matrix[i][0],X.matrix[i][1])
# Y_hat=Matrix(y_hat)
# Diff=Y_hat-Y
# MSE=sum((Diff.peek(i,0)*Diff.peek(i,0)) for i in range(Diff.m))/Diff.m
# print('MSE: ',round(MSE,3))


# #Building Sample Data
# degree=2
# X=build_poly(1000,degree)
# coeff=[2,3,6]
# x = [0 for j in range(X.m)]
# for row in range(X.m):
#     temp = 0
#     x[row] = X.matrix[row][1]
# y=build_out(coeff,X)
# y=add_poly_noise(y,100)
#
# #Plotting Sample Data
# two_plot(x,y)
#
# #Evaluating Coeffecients
# Y=Matrix([y])
# Y=Y.transpose()
# BETA = (X.transpose() * X).inverse() * X.transpose() * Y
#
# #Plotting Predicted Outcome
# x=[[0]*(degree+1) for i in range(200)]
# for i in range(200):
#     for j in range(degree+1):
#         x[i][j]=pow(i,j)
# X=Matrix(x)
# poly_plot(BETA.transpose().matrix[0],X)






