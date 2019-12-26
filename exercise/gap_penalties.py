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
    list_comb = []
    for i in range(len(seq1) + len(seq2)):
        
    
    return list_comb

combinations(seq1, seq2)