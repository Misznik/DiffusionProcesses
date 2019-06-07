# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 13:38:16 2019

@author: micha
"""
import numpy as np

class Vector:
    
    def __init__(self, dim = 3):
        self.dim = dim
        self.elements = [0]*dim
    
    def rand_element(self):
        for i in range(self.dim):
            self.elements[i] = np.random.random()

    def fromList(self, myList):
        self.elements = myList
        self.dim = len(myList)
        
    def __add__(self, other):
        if self.dim != other.dim:
            raise ValueError("dim not equal")
        else:
            res = Vector(self.dim)
            for i in range(self.dim):
                res.elements[i] = self.elements[i] + other.elements[i]
        return res
    
    def __sub__(self, other):
        pass
    
    def __neg__ (self, other):
        pass         #zmiana znaku na przeciwny
        
    def __mul__(self, other): #mnozenie *
        if type(other) in [int, float]:
            res = Vector(self.dim)
            for i in range(self.dim):
                res.elements[i] = self.elements[i] * other
            return res
        elif type(other) == Vector:
            if other.dim != self.dim:
                raise ValueError
            else:
                res = 0
                for i in range(self.dim):
                    res *= self.elements[i] * other.elements[i]
                return res
        else:
            raise TypeError
    
    def __rmul__(self, other):
        return self * other
    
    def __str__(self): #to do printa
        return str(self.elements)
    
    def __getitem__(self, i):
        return self.elements[i]
    
    def __setitem__(self, i, ele):
        #self.elements[i] = ele
        pass
    
    def __contains__(self,ele):
        return ele in self.elements
    

if __name__ == "__main__": #bezpiecznie, chroni przed importem z innych plikow
    v = Vector()
    v.fromList([1,0,0])
    w=Vector()
    w.fromList([0,1,0])
    v1 = w + v
    v2 = 3* v1
    print(v2, 3 in v2)
    #2 in [2,3]
    #2.__contains__([2,3])
        