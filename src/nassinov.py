#!/usr/bin/env python

'''
nassinov.py
Author: Shan Sabri
Date Created: 08/17/2015

Dynamic programming implementation of the 
Nassinov algorithm to predict RNA secondary 
structure. The goal of the Nussinov algorithm 
is to build a structure with the greatest amount 
of base parings.

'''

import time, forgi.graph.bulge_graph as fgb


def readInSeq(a):
    s1 = ""
    for line in a:
        b = 0
        if line.startswith('>'):
            pass
        else :
            for b in range(0, len(line)):
                if line[b] != " " and line[b] != "\n":
                    s1 = s1 + line[b].capitalize()
    return s1


def basepair(j, k):
    if (j == "A" and k == "U") or \
       (j == "U" and k == "A") or \
       (j == "C" and k == "G") or \
       (j == "G" and k == "C"):
        return True
    else:
        return False


def Re(i, j, N):
    for l in range (-1, 3+1):
        for i in range(1, n-l+1):
            N[i][i+l] = 0

    for l in range(4, n-1+1):
        for i in range(1, n-l+1):
            N[i][i+l] = N[i+1][i+l]
            for k in range (i+4, i+l+1):
                if basepair(s1[i-1], s1[k-1]):
                    N[i][i+l] = max(N[i][i+l], 1+N[i+1][k-1] + N[k+1][i+l])
    return N[i][j]


def Backtrack(i, j, N):
    if N[i][j]==0:
        pass
    else:
        if N[i][j] ==N[i+1][j]:
            Backtrack(i+1, j, N)
        else:
            for k in range(i+4, j+1):
                if basepair(s1[i-1], s1[k-1]) and N[i][j]==1+N[i+1][k-1]+N[k+1][j]:
                    z[i]= '('
                    z[k]= ')'
                    Backtrack(i+1, k-1, N)
                    Backtrack(k+1, j, N)
                    break # Added break because there can only be one base pair per residue



if __name__ == "__main__":

    start = time.clock()

    ## EXAMPLE
    a = "CUUGGUGGCGAUAGCGAAGAGGUCAGACCCGUUCCCAUACCGAACACGGAAGUUAAGCUCUUCAGCGCCGAUGGUAGUCGGGGGUUUCCCCCGGUGACCGUCGGACGCCGCCAAGC"
    s1 = readInSeq(a)
    n  = len(s1)
    N  = [[None for c in range(1,n+3)] for d in range(1,n+3)]
    z  = [None for s in range(1,n+3)]

    resultRe = Re(1 ,n, N)
    # Backtrack(1,n,N)

    for h in range(1,n+1):
        if z[h] == None:
            z[h]= '.'

    thestring = ""
    for o in range(1,1+n): 
        thestring = thestring + str(z[o])


    # Annotate dot-bracket notation
    bg = fgb.BulgeGraph()
    bg.from_dotbracket(thestring)
    #print bg.to_bg_string()

    # print output
    print s1
    # print "The maximum number of basepairs in the sequence is: " + str(resultRe)
    print "The structure in string form:         " + thestring
    print "The corresponding annotated notation: " + bg.to_element_string()
    print "\nFinished in ",time.clock() - start,"seconds"