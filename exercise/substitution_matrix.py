#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 10:16:35 2019

@author: naiara
"""

# SCORE MATRIX OR SUBSTITUTION MATRIX

"""
   1 = "ACAGGTGGACCT"     
   2 = "ACTGGTCGACTC"
   
   P(A) = 5/24    P(A, A) = 2/12     P(C, C) = 2/12    P(G, T) = 1
   P(C) = 6/24    P(A, C) = 1        P(C, G) = 1/12    P(T, T) =1/12
   P(G) = 7/24    P(A, G) = 1        P(C, T) = 1/12
   P(T) = 6/24    P(A, T) = 1/12     P(G, G) = 3/12
   
   We assume that whe the pairs do not exist the probability will be 1
   
 s(a,b) = int[k * log(P(ab) / Qa * Qb] -> K = 1
   
            A                    C                   T                    G
   
A   1.4294292643817876   1.2833012287035497   1.2163544390729364   1.3180633349627615 
  
C   1.2833012287035497   1.271066772286538    1.1719352992845236   1.2388820889151366

T   1.2163544390729364   1.1719352992845236   1.1671364164027547   1.1371731930253115

G   1.3180633349627615   1.2388820889151366   1.1371731930253115   1.271066772286538
     
"""
import math

seq1 = "ACAGGTGGACCT"     
seq2 = "ACTGGTCGACTT"

seq = "CTATATGG"
seq = "CCGGATCG"


def print_matrix(row):
    var = ""; list_bases = ["A", "C", "G", "T"]
    for i in range(len(row)):
        var += list_bases[i] + "\t"
        for j in row[i]:
            var += str(j) + "\t"
        var += "\n"
    print(var)

def sustitution_matrix(seq1, seq2):
    if len(seq1) == len(seq2):
        prob_res = {}; list_pairs = []; dic_pairs = {}; list_bases = ["A", "C", "G", "T"];
        k = 1; result_list = []; bases = ""; total_pairs = 0
        total_residuos = len(seq1) + len(seq2)
        prob_res["A"] = (seq1.count("A") + seq2.count("A")) / total_residuos
        prob_res["C"] = (seq1.count("C") + seq2.count("C")) / total_residuos
        prob_res["G"] = (seq1.count("G") + seq2.count("G")) / total_residuos
        prob_res["T"] = (seq1.count("T") + seq2.count("T")) / total_residuos
        print(prob_res, "\n")
        
        for i in range(len(seq1)):
            list_pairs.append(seq1[i] + seq2[i])
    
        for j in list_pairs:
            if not j in dic_pairs:
                bases = j
                if not bases[::-1] in dic_pairs:
                    if j == bases[::-1]:
                        total_pairs = list_pairs.count(j)
                    else:
                        total_pairs = list_pairs.count(j) + list_pairs.count(bases[::-1])
                    dic_pairs[j] = total_pairs / len(seq1)
                    dic_pairs[bases[::-1]] = dic_pairs[j]
        print(dic_pairs, "\n")
        
        for i in range(len(list_bases)):
            list_prob = []
            for j in range(len(list_bases)):
                pro_1 = prob_res[list_bases[i]]
                pro_2 = prob_res[list_bases[j]]
                
                if (list_bases[i]+list_bases[j] in dic_pairs):
                    pro_both = dic_pairs[list_bases[i]+list_bases[j]] + 1
                else:
                    pro_both = 1
                if pro_1 == 0 or pro_2 == 0:
                    list_prob.append(0)
                else:
                    list_prob.append( k * math.log10(pro_both / (pro_1 * pro_2)))
            result_list.append(list_prob)
        
    else:
        print("Length of the sequences are different")
        
    return result_list


print_matrix(sustitution_matrix(seq1, seq2))