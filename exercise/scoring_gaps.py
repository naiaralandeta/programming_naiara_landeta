#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 Write a script that generates all the possible ungapped alignments of two
 sequences, scores them and identifies the best scoring ones.
 
 These are all the possible ungapped alignments of the two sequences: TCA and GA:
     --TCA  -TCA  TCA  TCA  TCA-  TCA--
     GA---  GA--  GA-  -GA  --GA  ---GA
     
 Using the following scoring scheme:
   score_matrix = {'AA': 2, 'AC':-1, 'AT':-1, 'AG': 0,
                   'CA':-1, 'CC': 2, 'CT': 0, 'CG':-1,
                   'TA':-1, 'TC': 0, 'TT': 2, 'TG':-1,
                   'GA': 0, 'GC':-1, 'GT':-1, 'GG': 2
                   }
   
   The best scoring alignment is:
       TCA
       -GA
   
"""

score_matrix = {'AA': 2, 'AC':-1, 'AT':-1, 'AG': 0,
               'CA':-1, 'CC': 2, 'CT': 0, 'CG':-1,
               'TA':-1, 'TC': 0, 'TT': 2, 'TG':-1,
               'GA': 0, 'GC':-1, 'GT':-1, 'GG': 2}


#ungapped_seq1 = ["--TCA", "-TCA", "TCA", "TCA", "TCA-", "TCA--"]
#ungapped_seq2 = ["GA---", "GA--", "GA-", "-GA", "--GA", "---GA"]

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

def scoring_ungapped_alignment():
    dic_sum = {}
    for i in range(len(ungapped_seq1)):
        sum = 0
        seq1 = ungapped_seq1[i]
        seq2 = ungapped_seq2[i]
        for j in range(len(seq1)):
            if seq1[j]+seq2[j] in score_matrix: 
                sum += score_matrix[seq1[j] + seq2[j]]
        dic_sum[seq1 + "/" + seq2] = sum
    return dic_sum

ungapped_seq1, ungapped_seq2 = combinations("TCA", "GA")
print(scoring_ungapped_alignment())
    