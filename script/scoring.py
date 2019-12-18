#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 02:17:30 2019

@author: naiara
"""

def scoring(cad1, cad2):
    score = 0
    for i in range(len(cad1)):
        if cad1[i] == cad2[i]:
            score += 1
        else:
            score += 0
    return score


cad1 = "ACCAGGCA"
cad2 = "ACCAGGCP"
print("Length seq1:", len(cad1), "Length seq2:", len(cad2))
if len(cad1) == len(cad2):
    print("Scoring: ", scoring(cad1, cad2))
else:
    print("The length are different")
    
