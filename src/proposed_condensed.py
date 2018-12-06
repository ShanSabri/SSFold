#!/usr/bin/env python

'''
proposed_condensed.py
Author: Shan Sabri
Date Created: 08/07/2015

The proposed dynamic programming implementation 
for predicting the optimal RNA secondary structure.
Code has been condensed. 

'''

def bp(*b):
  return sum(map("ACGU".index, b)) in (3, 5)


def vw(s):
    v, w = {}, {}
    for i in xrange(0, len(s)):
        for j in xrange(i + 1, -1, -1):
            if j > i - 4 or not bp(s[i], s[j]):
                v[(j, i)] = (-2, lambda: ())
            else:
                v[(j, i)] = max((w[(j + 1, i - 1)][0], (lambda a, b: \
                lambda: ((a, b),) + w[(a + 1, b - 1)][1]())(j, i)),  \
                (1 + v[(j + 1, i - 1)][0], (lambda a, b: lambda: ((a,\
                b),) + v[(a + 1, b - 1)][1]())(j, i)))
            if j > i - 4:
                w[(j, i)] = (0, lambda: ())
            else:
                w[(j, i)] = max(w[(j + 1, i)], max((v[(j, k)][0] + \
                w[(k + 1, i)][0], (lambda a, b: lambda: v[(a, k)][1]()\
                + w[(k + 1, b)][1]())(j, i)) for k in xrange(j + 4, i + 1)))
    return w[(0, len(s) - 1)][0], w[(0, len(s) - 1)][1]()


if __name__ == '__main__':
    
    ## EXAMPLES
    # score, struct = vw("GGGGGGGGGGGGGGCCCCCCCCCCCCCCCCCCCCCCCCCCCCGGGGGGGGGGGGGG")
    score, struct = vw("UGCUCCUAGUACGAGAGGACCGGAGUG")
    print "Score: " + str(score) + " ---> Struct: " + str(struct)