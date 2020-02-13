#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SMITH AND WATERMAN ALGORITHM

seq1 = "ACTCT"
seq2 = "ATTAA"

best alignment:
    ACT
    ATT
    
(Si) Best alignment is in wherever position in the matrix

(No) Generate all the local alignments

(Si) Stop when we find the first 0 (while != 0)

(No) Check that the values are not incluide in other alignments

"""

# Visualize in matrix form
def print_matrix(m):
    for i in range(len(m)):
        value = ""
        for j in range(len(m[0])):
            value += str(m[i][j]) + "\t"
        print(value, "\n")
        
def local_align(s1, s2, sub_matrix, d):
    """
    Calculates the global dynamic programming (scoring) matrix
    """
    rows = len(s1) + 1 # num of rows for seq1 and + 1 for f(0,0)
    columns = len(s2) + 1 # num of columns for seq2 and + 1 for f(0,0)
    
    # Init matrix with 0 and dimensions rows * columns
    F = [[0] * columns for x in range(rows)]
    P = [[0] * columns for x in range(rows)]
    
    # Init. rows
    for i in range(rows):
        F[i][0] = 0
        P[i][0] = 'u'
    # Init. columns
    for j in range(columns):
        F[0][j] = 0
        P[0][j] = 'l'
        
    # Iteration to fill matrices P and F
    for i in range(1, rows): # Rows
        for j in range(1, columns): # Columns
            # Previous value in the diagonal + gap
            sDiagonal = F[i-1][j-1] + sub_matrix[s1[i-1] + s2[j-1]] 
            sColumn = F[i-1][j] + d # Fill columns
            sRow = F[i][j-1] + d # Fill rows
            
            # Get the maximun value, we consider 0 in the case that the values are negative
            max_value = max(sDiagonal, sColumn, sRow, 0)
            
            # Add u = up, l = left and d = diagonal in the matrix P
            if max_value == sDiagonal:
                P[i][j] = "d"
            elif max_value == sColumn:
                P[i][j] = "l"
            elif max_value == sRow:
                P[i][j] = "u"
                
            F[i][j] = max_value

    return F,P

def start_alignment(F):
    """
    Find the position of the best alignment and return the position (i,j)
    """
    max = F[0][0]
    for i in range(len(F)):
        for j in range(len(F[0])):
            if max < F[i][j]:
                max = F[i][j]
                pos_i = i
                pos_j = j
    return pos_i,pos_j

def all_alignments(F):
    list_l =[]
    for i in range(len(F)):
        for j in range(len(F[0])):
            
            if list_l == [] and F[i][j] > 0:
                list_l.append([i,j])
                
            if list_l != [] and F[i][j] > 0 and not [i,j] in list_l:
                list_l.append([i,j])
        #No etsa bien       
        for i in range(len(list_l)):
            element_1 = list_l[i]; y = element_1[0]; z = element_1[1]
            for j in range(i, len(list_l)):
                element_2 = list_l[j]; w = element_2[0]; q = element_2[1]
                if F[y][z] < F[w][q]:
                    list_l.remove([w,q])
                    list_l.insert(j-1,[w,q])
    
    print(list_l)
    print("\n")
    return list_l
          
def alignment(s1, s2, F, P):
    """ 
    This function will align the s1 and the s2 using P matrix. 
    In the case of matrix F, we wil use to extract the value of the alignment
    """
    print_matrix(F)
    list_l = all_alignments(F); list_position = []
   # List_l have all the possible alignments
    for x in list_l:
        i = x[0]; j = x[1]; isInList = False; template = ""; target = ""; score = F[i][j]
        while i != 0 and j != 0 and F[i][j] != 0:
            if not [i,j] in list_position:
                # Use gaps when the movement is to left or up, we are add a gap "-". Means no match.
                list_position.append([i,j])
                if P[i][j] == "d":
                    template += s1[i - 1]
                    target += s2[j - 1]
                    i -= 1; j -= 1  
                # Left - target   
                elif P[i][j] == "l":
                    template += s1[i - 1]
                    target += "-"
                    i -= 1; j -= 1
                # Up - template 
                else:
                    template += "-"
                    target += s2[j - 1]
                    i -= 1; j -= 1
            else:
                isInList = True
                i -= 1; j -= 1
                
         # if the position are not in list_position print the result
        if not isInList:
            template = template[::-1]
            target = target[::-1]
            print("S1:", template)
            print("S2:", target)
            print("Score:", score)
            print("\n")

if __name__ == "__main__":
    # Sequences without gaps
    s1 = "ACTCT" # Rows
    s2 = "ATTAA" #Columns
    d = -2
    
    sub_matrix = {"AA": 2, "AC": -1, "AT": -1, "AG": 0,
              "CA": -1, "CC": 2, "CT": 0, "CG": -1,
              "TA": -1, "TC":0, "TT": 2, "TG": -1,
              "GA": 0, "GC": -1, "GT": -1, "GG": 2} 

    F, P = local_align(s1, s2, sub_matrix, d)
    alignment(s1, s2, F, P)