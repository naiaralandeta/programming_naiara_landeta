#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
1) Write a function that multiplies two N*N matrices.
As a test you can use:
    A = [[2,4],
         [3,1]]
    B = [[2,1],
         [1,3]]

the result of which is:

AB = [[8, 14]
      [7, 6]] 
"""

a = [[2,4], [3,1]]
b = [[2,1] , [1,3]]

def multiplation_matrixes(a, b):
    mul = []; 
    for i in range(len(a)):
        for j in range(len(b)):
            sum = 0
            for k in range(len(a)):
                sum += a[i][k] * b[k][j]
            mul.append(sum)
                
    print(mul)
            
multiplation_matrixes(a, b)
