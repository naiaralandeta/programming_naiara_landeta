#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 11:40:22 2020

@author: naiara
"""
#
#import input_data
#
#d = input_data.PAM250_dict

#from input_data import PAM250_dict
#
#print(input_data)

def read_matrices(matrix_name):
    file = open("./" + matrix_name + ".txt", "r")
    dic = {}; list_file = []; num_row = 0
    
    for line in file:
        if "rows" in line:
            aux = line.split()
            rows = aux[3].replace(",","")
            columns = aux[6].replace(",","")
        else:
            list_file.append(line.split())
        
    for elem in list_file:
        for i in range(len(elem)):
            dic[rows[num_row] + columns[i]] = elem[i]
        num_row += 1

    file.close()
    return dic

def read_fasta(fasta_name):
    file = open("./" + fasta_name + ".fasta", "r")
    list_alignments = []
    for line in file:
        if not ">" in line:
            list_alignments.append(line.rstrip())
    return list_alignments
   
def score_alignment(dic_m1, dic_m2, list_aligments, matrix_name1, matrix_name2):
    gap_penalty = -2; first_seq = ""; second_seq = ""; num = 1
    
    for num_element in range(len(list_aligments)):
        score_m1 = 0; score_m2 = 0
        first_seq = list_aligments[num_element]
        if first_seq != second_seq:
            if num_element < len(list_aligments):
                second_seq = list_aligments[num_element + 1]

                for i in range(len(first_seq)):
                    pairwise = first_seq[i]+second_seq[i]
                    if pairwise in dic_m1:
                        score_m1 += float(dic_m1[first_seq[i] + second_seq[i]])
                    elif first_seq[i] == "-" or second_seq[i] == "-":
                        score_m1 += float(gap_penalty)
                    else:
                        score_m1 += float(dic_m1[second_seq[i] + first_seq[i]])
                        
                    if pairwise in dic_m2:
                        score_m2 += float(dic_m2[first_seq[i] + second_seq[i]])
                    elif first_seq[i] == "-" or second_seq[i] == "-":
                        score_m2 += float(gap_penalty)
                    else:
                        score_m2 += float(dic_m2[second_seq[i] + first_seq[i]])
                
            print("\nAligment", num)
            print(matrix_name1, ":", score_m1)
            print(matrix_name2, ":", score_m2,  "\n")
            num += 1
        

def main(matrix_name1, matrix_name2 ,fasta_name):
    dic_m1 = read_matrices(matrix_name1)
    dic_m2 = read_matrices(matrix_name2)
    list_alignments = read_fasta(fasta_name)
    score_alignment(dic_m1, dic_m2, list_alignments, matrix_name1, matrix_name2)
    
   

if __name__ == "__main__":
    #matrix_name1 = input("Which matrix do you use?").upper()
    #matrix_name2 = input("Which matrix do you use?").upper()
    main("PAM250", "BLOSUM62","alignments")
   # matrix_name = input("Which matrix do you use?").upper()
   # main(matrix_name,"alignments")