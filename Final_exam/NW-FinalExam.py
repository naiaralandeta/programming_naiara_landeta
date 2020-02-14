#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 13:18:20 2020

@author: naiara

NEEDLEMAN-WUNSCH - Global alignment WITH GAPS
"""
        
def global_alignment(seq1, seq2, BLOSUM52, gap_penalty):
    """ Do the global dynamic programming (scoring) matrix F and the path matrix P, and fullfill them
    and it going to return the matrices F and P"""
    rows = len(seq1) + 1 # num of rows for seq1 and + 1 for f(0,0)
    columns = len(seq2) + 1 # num of columns for seq2 and + 1 for f(0,0)
    
    # Generate matrices F and P with 0 and dimensions rows * columns
    F = [[0] * columns for x in range(rows)]
    P = [[0] * columns for x in range(rows)]
    
    # Fullfill firt row of the matrices F and P
    for i in range(rows):
        F[i][0] = gap_penalty * i # to obtain all the gap penalties you need to multiplicate with the iteration
        P[i][0] = 'l' # indicates left
        
    # Fullfill firt column of the matrices F and P
    for j in range(columns):
        F[0][j] = gap_penalty * j # to obtain all the gap penalties you need to multiplicate with the iteration
        P[0][j] = 'u' # indicates up
        
    # Full fill the rest of the matrices
    for i in range(1, rows): # Rows
        for j in range(1, columns): # Columns
            
            sDiagonal = F[i-1][j-1] + BLOSUM52[seq1[i-1] + seq2[j-1]] # Previous value in the diagonal + gap
            sColumn = F[i-1][j] + gap_penalty # Previous value in the diagonal + gap
            sRow = F[i][j-1] + gap_penalty # Previous value in the diagonal + gap
            
            # Obtain the maximun value
            max_score = max(sDiagonal, sColumn, sRow)
            
            # Add u = up, l = left and d = diagonal in the matrix P
            if max_score == sDiagonal:
                P[i][j] = "d" # d, represents diagonal
            elif max_score == sColumn:
                P[i][j] = "l" # l, represents column (left)
            else:
                P[i][j] = "u" # u, represents row (up)
                
            F[i][j] = max_score # strore the max score in the matrix F

    return F,P

def best_alignment(seq1, seq2, F, P):
    """ This function will align the seq1 and the seq2 using P matrix. 
    In the case of matrix F, we wil use to extract the value of the alignment. It going to return 
    the template (seq1), target (seq2) and best score"""
    
    i = len(P) - 1; j = len(P[0]) -1 # Start from the last position on the matrix
    template = ""; target = ""; score = F[i][j] # The last position of the matrix F is the best score in NW with gaps
    while i != 0 and j != 0:
        # Use gaps when the movement is to left or up, we are add a gap "-". It means no match.
        if P[i][j] == "d":
            template += seq1[i - 1] # Insert in template the letter of the sequence 1
            target += seq2[j - 1] # Insert in template the letter of the sequence 2
            i -= 1
            j -= 1  
        elif P[i][j] == "l":
            template += seq1[i - 1] # Insert in template the letter of the sequence 1
            target += "-" # Insert a gap for the movement
            i -= 1
        else:
            template += "-" #Insert a gap for the movement
            target += seq2[j - 1] # Insert in template the letter of the sequence 2
            j -= 1
            
    return template, target, score

def represent_alignment(template, target, score):            
    """ Print the template (sequence 1) and the target (sequence 2) representing the best alignment and the score"""
    template = template[::-1] # Reverse template
    target = target[::-1] # Reverse target
    print("Seq1:", template)
    print("Seq2:", target)
    print("Score:", score)
    
def obtain_data():
    """ Function to read the seq1, seq2 and the BLOSUM52 dictionary from the file input_data.py """
    import input_data
    dic = input_data.BLOSUM52
    seq1 = input_data.seq1
    seq2 = input_data.seq2
    return seq1, seq2, dic

if __name__ == "__main__":
    seq1, seq2, BLOSUM52 = obtain_data() # Sequences without gaps and dictionary BLOSUM52
    gap_penalty = -2 # Use the normal gap_penalty that we use in class, in the exam is not specificed
    F, P = global_alignment(seq1, seq2, BLOSUM52, gap_penalty)
    template, target, score = best_alignment(seq1, seq2, F, P)
    represent_alignment(template, target, score)