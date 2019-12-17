#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 20:49:27 2019

@author: naiara
"""

# MODULE 2

# Solo para los carbonos alpha
import math

def read_file(f):
    file = open("./" + f, "r")
    return file

def get_coordinates(line, next):
    coord = ()
    if next:
        coord = (line[5], line[6], line[7])
    else:
        coord = (line[6], line[7], line[8])
            
    return coord
 
def RMSD(ca_model1, ca_model2):
    
    result = 0
    distances = 0
    for i in range(len(ca_model1)):
        for j in range(len(ca_model1[i])):
            distances += (float(ca_model1[i][j]) - float(ca_model2[i][j])) ** 2
    result = math.sqrt((1/100) * distances)
    return result
    
def superimposition(f1):
   file = read_file(f1)
   no_next = True
   ca_model1 = [] ; ca_model2 = []; tuple_result = (); list_atoms = []
   for line in file:
       line = line.split()
       if line != [] and not line[0] == "MODEL":
           if line[0] == "ENDMDL":
              no_next = False
              
           elif line[0] == 'ATOM' and line[2] == 'CA':
               if no_next:
                   tuple_result = get_coordinates(line, False)
                   if not tuple_result == () and not line[5] in list_atoms:
                       ca_model1.append(tuple_result)
                       list_atoms.append(line[5])
               else:
                  tuple_result = get_coordinates(line, True)
                  if not tuple_result == () and not line[5] in list_atoms:
                      ca_model2.append(tuple_result)
                      list_atoms.append(line[4])

   print("RMSD result:", RMSD(ca_model1, ca_model2))

superimposition("model8.pdb")
    
    
    