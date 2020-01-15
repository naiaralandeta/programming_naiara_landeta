#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Write a script that scores into a Python dictionary a substitution matrix in 
    tabular format. For example:
        
       A  R  N  D  C  Q  E  G  H  I  L  K  M  F  P  S  T  W  Y  V
    A  4 -1 -2 -2  0 -1 -1  0 -2 -1 -1 -1 -1 -2 -1  1  0 -3 -2  0
    R -1  5  0 -2 -3  1  0 -2  0 -3 -2  2 -1 -3 -2 -1 -1 -3 -2 -3
    N -2  0  6  1 -3  0  0  0  1 -3 -3  0 -2 -3 -2  1  0 -4 -2 -3
    D -2 -2  1  6 -3  0  2 -1 -1 -3 -4 -1 -3 -3 -1  0 -1 -4 -3 -3
    C  0 -3 -3 -3  9 -3 -4 -3 -3 -1 -1 -3 -1 -2 -3 -1 -1 -2 -2 -1
    Q -1  1  0  0 -3  5  2 -2  0 -3 -2  1  0 -3 -1  0 -1 -2 -1 -2
    E -1  0  0  2 -4  2  5 -2  0 -3 -3  1 -2 -3 -1  0 -1 -3 -2 -2
    G  0 -2  0 -1 -3 -2 -2  6 -2 -4 -4 -2 -3 -3 -2  0 -2 -2 -3 -3
    H -2  0  1 -1 -3  0  0 -2  8 -3 -3 -1 -2 -1 -2 -1 -2 -2  2 -3
    I -1 -3 -3 -3 -1 -3 -3 -4 -3  4  2 -3  1  0 -3 -2 -1 -3 -1  3
    L -1 -2 -3 -4 -1 -2 -3 -4 -3  2  4 -2  2  0 -3 -2 -1 -2 -1  1
    K -1  2  0 -1 -3  1  1 -2 -1 -3 -2  5 -1 -3 -1  0 -1 -3 -2 -2
    M -1 -1 -2 -3 -1  0 -2 -3 -2  1  2 -1  5  0 -2 -1 -1 -1 -1  1
    F -2 -3 -3 -3 -2 -3 -3 -3 -1  0  0 -3  0  6 -4 -2 -2  1  3 -1
    P -1 -2 -2 -1 -3 -1 -1 -2 -2 -3 -3 -1 -2 -4  7 -1 -1 -4 -3 -2
    S  1 -1  1  0 -1  0  0  0 -1 -2 -2  0 -1 -2 -1  4  1 -3 -2 -2
    T  0 -1  0 -1 -1 -1 -1 -2 -2 -1 -1 -1 -1 -2 -1  1  5 -2 -2  0
    W -3 -3 -4 -4 -2 -2 -3 -2 -2 -3 -2 -3 -1  1 -4 -3 -2 11  2 -3
    Y -2 -2 -2 -3 -2 -1 -2 -3  2 -1 -1 -2 -1  3 -3 -2 -2  2  7 -1
    V  0 -3 -3 -3 -1 -2 -2 -3 -3  3  1 -2  1 -1 -2 -2  0 -3 -1  4
    
    You can find other substitution matrices here: https://www.genome.jp/aaindex/
    You can find matrix codes here:  https://www.genome.jp/aaindex/AAindex/list_of_matrices
"""
def scoring_matrix():
    file = open("./../data/sub_matrix.txt", "r")
    header_aa = ""; list_aa = []; dic_aa = {}
    for line in file:
        line = line.rstrip();
        if header_aa == "":
            header_aa = line.split()
        else:
            list_aa.append(line)

    for i in list_aa:
        list_elem = i.split()
        for j in range(len(list_elem)):
            if list_elem[j] != list_elem[0]:
                dic_aa[list_elem[0] + header_aa[j-1]] = list_elem[j]
    file.close()
    return dic_aa

#print(scoring_matrix())


"""    
    Store in dictionary the two following matrices (PAM250 and BLOSUM62, 
    one dictionary per matrix)
    
    PAM250:
    M rows = ARNDCQEGHILKMFPSTWYV, cols = ARNDCQEGHILKMFPSTWYV
      2.
     -2.      6.
      0.      0.      2.
      0.     -1.      2.      4.
     -2.     -4.     -4.     -5.     12.
      0.      1.      1.      2.     -5.      4.
      0.     -1.      1.      3.     -5.      2.      4.
      1.     -3.      0.      1.     -3.     -1.      0.      5.
     -1.      2.      2.      1.     -3.      3.      1.     -2.      6.
     -1.     -2.     -2.     -2.     -2.     -2.     -2.     -3.     -2.      5.
     -2.     -3.     -3.     -4.     -6.     -2.     -3.     -4.     -2.      2.      6.
     -1.      3.      1.      0.     -5.      1.      0.     -2.      0.     -2.     -3.      5.
     -1.      0.     -2.     -3.     -5.     -1.     -2.     -3.     -2.      2.      4.      0.      6.
     -4.     -4.     -4.     -6.     -4.     -5.     -5.     -5.     -2.      1.      2.     -5.      0.      9.
      1.      0.     -1.     -1.     -3.      0.     -1.     -1.      0.     -2.     -3.     -1.     -2.     -5.      6.
      1.      0.      1.      0.      0.     -1.      0.      1.     -1.     -1.     -3.      0.     -2.     -3.      1.      2.
      1.     -1.      0.      0.     -2.     -1.      0.      0.     -1.      0.     -2.      0.     -1.     -3.      0.      1.      3.
     -6.      2.     -4.     -7.     -8.     -5.     -7.     -7.     -3.     -5.     -2.     -3.     -4.      0.     -6.     -2.     -5.     17.
     -3.     -4.     -2.     -4.      0.     -4.     -4.     -5.      0.     -1.     -1.     -4.     -2.      7.     -5.     -3.     -3.      0.     10.
      0.     -2.     -2.     -2.     -2.     -2.     -2.     -1.     -2.      4.      2.     -2.      2.     -1.     -1.     -1.      0.     -6.     -2.      4.
"""  
rows = "ARNDCQEGHILKMFPSTWYV"
cols = "ARNDCQEGHILKMFPSTWYV"

def PAM250():
    file = open("./../data/sub_matrix_PAM250.txt", "r")
    dic_PAM250 = {}; list_file = []; num_row = 0
    
    for line in file:
        list_file.append(line.split())
        
    
    for elem in list_file:
        for i in range(len(elem)):
            dic_PAM250[rows[num_row] + cols[i]] = elem[i]
        num_row += 1

    file.close()
    return dic_PAM250
    
#print(PAM250())

"""  

    BLOSUM62:
    M rows = ARNDCQEGHILKMFPSTWYV, cols = ARNDCQEGHILKMFPSTWYV
      6.
     -2.      8.
     -2.     -1.      8.
     -3.     -2.      2.      9.
     -1.     -5.     -4.     -5.     13.
     -1.      1.      0.      0.     -4.      8.
     -1.      0.      0.      2.     -5.      3.      7.
      0.     -3.     -1.     -2.     -4.     -3.     -3.      8.
     -2.      0.      1.     -2.     -4.      1.      0.     -3.     11.
     -2.     -4.     -5.     -5.     -2.     -4.     -5.     -6.     -5.      6.
     -2.     -3.     -5.     -5.     -2.     -3.     -4.     -5.     -4.      2.      6.
     -1.      3.      0.     -1.     -5.      2.      1.     -2.     -1.     -4.     -4.      7.
     -1.     -2.     -3.     -5.     -2.     -1.     -3.     -4.     -2.      2.      3.     -2.      8.
     -3.     -4.     -4.     -5.     -4.     -5.     -5.     -5.     -2.      0.      1.     -5.      0.      9.
     -1.     -3.     -3.     -2.     -4.     -2.     -2.     -3.     -3.     -4.     -4.     -2.     -4.     -5.     11.
      2.     -1.      1.      0.     -1.      0.      0.      0.     -1.     -4.     -4.      0.     -2.     -4.     -1.      6.
      0.     -2.      0.     -2.     -1.     -1.     -1.     -2.     -3.     -1.     -2.     -1.     -1.     -3.     -2.      2.      7.
     -4.     -4.     -6.     -6.     -3.     -3.     -4.     -4.     -4.     -4.     -2.     -4.     -2.      1.     -5.     -4.     -4.     16.
     -3.     -3.     -3.     -5.     -4.     -2.     -3.     -5.      3.     -2.     -2.     -3.     -1.      4.     -4.     -3.     -2.      3.     10.
      0.     -4.     -4.     -5.     -1.     -3.     -4.     -5.     -5.      4.      1.     -3.      1.     -1.     -4.     -2.      0.     -4.     -2.      6.


"""

#rows = "ARNDCQEGHILKMFPSTWYV"
#cols = "ARNDCQEGHILKMFPSTWYV"

def BLOSUM62():
    file = open("./../data/sub_matrix_BLOSUM62.txt", "r")
    dic_BLOSUM62 = {}; list_file = []; num_row = 0
    
    for line in file:
        list_file.append(line.split())
        
    
    for elem in list_file:
        for i in range(len(elem)):
            dic_BLOSUM62[rows[num_row] + cols[i]] = elem[i]
        num_row += 1

    file.close()
    return dic_BLOSUM62
    
#print(BLOSUM62())
