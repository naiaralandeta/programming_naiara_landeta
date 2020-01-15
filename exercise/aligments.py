#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given the following alignments:

    ALSKLASPALSAKDLDSPAL
    ALSKIADSLAPIKDLSPASL
    
    ALSKLA-SPALSAKDLDSPAL
    ALSKIADSLAP-IKDLSPASL
    
    ALSKLASPALSAKDLDSPA-L
    ALSKIADSLAPIKDLS-PASL
    
    ALSKLASPALSAKDLDSPA-LS
    ALSKIADSLAPIKDLS-PASLT

Which one gets the highest score using PAM250 and d = -1?
    ALSKLASPALSAKDLDSPA-LS
    ALSKIADSLAPIKDLS-PASLT
    
Which one gets the highest score using BLOSUM62 and d = -1?
    ALSKLASPALSAKDLDSPA-LS
    ALSKIADSLAPIKDLS-PASLT

Write the script using the following construct:
if __name__ == "__main__":
    ...

so that you can read the gap penalty and the matrix to use from the command line.
"""

def main(name):
    file = open(name, "r")
    dic_matrix = {}; list_file = []; num_row = 0
    rows = "ARNDCQEGHILKMFPSTWYV"
    cols = "ARNDCQEGHILKMFPSTWYV"
    
    for line in file:
        list_file.append(line.split())
        
    for elem in list_file:
        for i in range(len(elem)):
            dic_matrix[rows[num_row] + cols[i]] = elem[i]
        num_row += 1

    file.close()
    return dic_matrix
    
def aligment(dic_matrix, gap_penalty, name):
    list_sequences = [["ALSKLASPALSAKDLDSPAL", "ALSKIADSLAPIKDLSPASL"],
                      ["ALSKLA-SPALSAKDLDSPAL","ALSKIADSLAP-IKDLSPASL"],
                      ["ALSKLASPALSAKDLDSPA-L","ALSKIADSLAPIKDLS-PASL"],
                      ["ALSKLASPALSAKDLDSPA-LS","ALSKIADSLAPIKDLS-PASLT"]]
    num = 1
    for pair_seq in list_sequences:
        seq1 = pair_seq[len(pair_seq) -len(pair_seq)]
        seq2 = pair_seq[len(pair_seq) -1]
        score = 0; 
        for i in range(len(seq1)):
            pairwise = seq1[i]+seq2[i]
            if pairwise in dic_matrix:
                score += float(dic_matrix[seq1[i] + seq2[i]])
            elif seq1[i] == "-" or seq2[i] == "-":
                score -= float(gap_penalty)
            else:
                score += float(dic_matrix[seq2[i] + seq1[i]])
        print("\nAligment", num)
        print(seq1 + "\n"+ seq2)
        print("Score alignment ", score, "with ", name, " matrix \n")
        num += 1
if __name__ == "__main__":
    name = input("Type of the sustitution matrix: ").upper()
    gap_penalty = input("Value of gap penalty (in positive): ")
    aligment( main("./../data/sub_matrix_" + name + ".txt"), gap_penalty, name)
    
    
    