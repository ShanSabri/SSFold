#!/usr/bin/env python

'''
matstack.py
Author: Shan Sabri
Date Created: 06/04/2015
Date Modified: 06/25/2015

Implementation of the proposed matstack class

'''

class Matstack:

    def __init__(self,s):
        self.a=s
        self.dict={}
        self.stackdict={}

    def matchcheck(self,i,j):
        if  (self.a[i]=="a" and self.a[j]=="u") or \
            (self.a[i]=="c" and self.a[j]=="g") or \
            (self.a[i]=="u" and self.a[j]=="a") or \
            (self.a[i]=="g" and self.a[j]=="c") or \
            (self.a[i]=="g" and self.a[j]=="u") or \
            (self.a[i]=="u" and self.a[j]=="g"):
            m=True
        else:
            m=False

        return m

    def match(self,i,j):
        result=[]
        if (i,j) in self.dict:
            t=self.dict[i,j]
            result.append(t)
        else:
            if j-i+1<=2:
                t=0
                result.append(t)
            else:
                s=i
                while s<j+1:
                    t=0
                    if self.matchcheck(s,j)==True:
                        t=self.match(i,s-1)+self.stack(s,j)
                        result.append(t)
                    s=s+1
                t=self.match(i,j-1)
                result.append(t)
            self.dict[i,j]=max(result)

        return max(result)


    def stack(self,i,j):
        result=[]
        if (i,j) in self.stackdict:
            t=self.stackdict[i,j]
            result.append(t)
        else:
            if j-i+1<=2:
                t=-len(self.a)
                result.append(t)
            elif self.matchcheck(i,j)==False:
                t=-len(self.a)
                result.append (t)
            else:
                # self.matchcheck (i,j)==True:
                t=self.stack(i+1,j-1)+1
                result.append(t)
                t=self.match(i+1,j-1)
                result.append (t)
                self.stackdict[i,j]=max(result)

        return max(result)


    def trace(self,i,j):
        structure =[]
        if j-i+1 <=2:
            pass
        else:
            s=i
            while s<j:
                if self.matchcheck(s,j) == True:
                    if self.match(i,s-1)+self.stack(s,j-1):
                        structure=self.trace(i,s-1)+self.tracestack(s,j-1)
                s=s+1
            if len(structure) == 0:
                structure=self.trace(i,j-1)
        return structure



    def tracestack(self,i,j):
        structure = []
        if j-i+1 == 2:
            if self.matchcheck(i,j) == True:
                structure.append((i,j))
        elif j-i+1 < 2:
            pass
        else:
            if self.matchcheck(i,j) == True:
                if i+1<j-1 and self.matchcheck(i+1,j-1) == True and self.stack(i,j) == self.stack(i+1,j-1) + 1:
                    structure=[(i,j)]+self.tracestack(i+1,j-1)
                else:
                    structure=self.trace(i+1,j-1)+[(i,j)]
        return structure



if __name__ == '__main__':
    
    ## EXAMPLE
    seq = "GGGCUAUUAGCUCAGUUGGUUAGAGCGCACCCCUGAUAAGGGUGAGGUCGCUGAUUCGAAUUCAGCAUAGCCCA"
    a = Matstack(seq.lower())
    i = 0
    j = len(seq) - 1

    print a.match(i,j)
    print a.stack(i,j)
    print a.tracestack(i,j)
    print a.trace(i,j)