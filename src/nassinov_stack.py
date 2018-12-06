#!/usr/bin/env python

'''
nassinov_stack.py
Author: Shan Sabri
Date Created: 08/17/2015

Modified dynamic programming implementation of the 
Nassinov algorithm to predict RNA secondary 
structure. The goal of this proposed algorithm is to
maximize the number of base pair stacks. 

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
       (j == "U" and k == "G") or \
       (j == "G" and k == "C"):
        return True
    else:
        return False


def initialize(W, V, length):
    for l in range (-1 ,4):
        for i in range(0, length-l):
            W[i][i+l] = 0
            V[i][i+l] = -float('infinity')
    return (W, V)


def fillMatrix(W, V, s1, length):
    # maxScore = 0
    for l in range(4, length):
        for i in range(0,length-l):

            # Compute V[i][j]
            if (basepair(s1[i],s1[i+l])):
                V[i][i+l] = max(W[i+1][i+l-1], 1+V[i+1][i+l-1])
            else :
                V[i][i+l] = -float('infinity')

            # Compute W[i][j]
            W[i][i+l] = W[i+1][i+l]
            maxScore = 0
            for k in range(i+4, i+l+1):
                maxScore = max(maxScore, V[i][k]+W[k+1][i+l])
            maxScore  = max(maxScore, V[i][i+l])
            W[i][i+l] = max(W[i+1][i+l], maxScore)

    return W, V, maxScore


def traceVpath(i, j, W, V):
    if V[i][j]==W[i+1][j-1]:
        traceWpath(i+1, j-1, W, V)
    elif V[i][j]==1+V[i+1][j-1]:
        traceVpath(i+1, j-1, W, V)
    if i not in structure and j not in structure:
        structure[i] = j; structure[j] = i


def traceWpath(i, j, W, V):
    if i < j and W[i][j] == W[i+1][j]:
        # print('branch 1')
        traceWpath(i+1, j, W, V)
    else:
        # print('branch 2')
        if i < j:
            # print('branch 3')
            for k in range(i+3, j+1):
                if W[i][j] == V[i][k] + W[k+1][j]:
                    # print('branch 4')
                    traceWpath(k+1, j, W, V); traceVpath(i, k, W, V)
                    break


def main(seq):

    start = time.clock()

    s1 = readInSeq(seq)
    length = len(s1)
    
    global structure
    structure = [None for i in range(0, length)]
    W = [[None for c in range(1,length+3)] for d in range(1,length+3)]
    V = [[None for c in range(1,length+3)] for d in range(1,length+3)]

    initW, initV = initialize(W, V, length)
    calcW, calcV, maxScore = fillMatrix(initW, initV, s1, length)

    traceWpath(0, length-1, calcW, calcV)
    # note: the value of 'structure' has been changed to what you want

    annot = ''.join(['.' if j is None else ')' if j < i else '(' for i, j in enumerate(structure)])
    # getScoreRNA(tracedStruct, length)


    # Annotate dot-bracket notation
    bg = fgb.BulgeGraph()
    bg.from_dotbracket(annot)

    # print structure
    print s1
    print "The structure in string form:         " + annot
    print "The corresponding annotated notation: " + bg.to_element_string()
    print "\nFinished in ",time.clock() - start,"seconds"

    return (calcW, calcV)


if __name__ == "__main__":

    ## EXAMPLE WITH KNOWN STRUCTURE 
    # >  File PDB_01011.ct. RNA SSTRAND database. External source: RCSB Protein Data Bank 2DU5, number of molecules: 1. The secondary structure annotation was obtained with RNAview.
    a = "GCCAGGGUGGCAGAGGGGCUUUGCGGCGGACUUCAGAUCCGCUUUACCCCGGUUCGAAUCCGGGCCCUGGC"
        # alg2.: ((((((((.(((.((...)).))).(((((.......)))))...))(((((.......))))).))))))
               # ((((((((.(((.((...)).))).(((((.......)))))...)))).((((((....)))))).)))) # allowing for GU/UG wobble
        # alg1.: ((((.((.((((.((...))).))((((((..(...))))))....)(((((.(...).))))))))))))
        # known: (((((((..(((.........))).(((((.......))))).....(((((.......))))))))))))
    main(a)