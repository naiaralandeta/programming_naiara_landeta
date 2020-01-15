#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 11:31:41 2019

@author: naiara
"""

""" 

A: TCA
B: GA

   A   C   T   G
A  2  -1  -1   0
C      2   0  -1
T          2  -1
G              2

"""
seq1 = "TCA"
seq2 = "GA"

scoring_matrix = {"AA": 2, "AC": -1, "AT": -1, "AG": 0, "CA": -1, "CC": 2, "CT": 0, "CG": -1,
                  "TA": -1, "TC": 0, "TT": 2, "TG": -1, "GA": 0, "GC": -1, "GT": -1, "GG": 2}

def combinations(seq1, seq2):
    list_seq1 = []; list_seq2 = []; total_len = len(seq1) + len(seq2)
    for i in range(total_len - 1):
        if i > 0 and i <= total_len - len(seq2):
            list_seq2.append("-"*i + seq2)
            if i == 1:
                list_seq2.append(seq2 + "-"*i)
            elif i == 2:
                list_seq2.append(seq2 + "-"*i)
                
        if i <= total_len - len(seq1):
            list_seq1.append(seq1 + "-"*i)
            if i == 0:
                list_seq1.append(seq1 + "-"*i)
            elif i == 1:
                list_seq1.append("-"*i + seq1)
                
    return list_seq1, list_seq2 
            
def score_alignment(list_seq1, list_seq2):
    for num_seq in range(len(list_seq1)):
        score = 0
        for seq in range(len(list_seq1[num_seq])):
            if list_seq1[num_seq][seq] + list_seq2[num_seq][seq] in scoring_matrix:
                score += scoring_matrix[list_seq1[num_seq][seq] + list_seq2[num_seq][seq]]
                
        print("Alignment", num_seq + 1)
        print(list_seq1[num_seq])
        print(list_seq2[num_seq])
        print("Score: ", score, "\n")

            
list_seq1, list_seq2 = combinations(seq1, seq2)
score_alignment(list_seq1, list_seq2)



