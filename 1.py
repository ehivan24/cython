'''
Created on Mar 6, 2015

@author: edwingsantos
'''
import cython


@cython.locals(n = cython.int)
def fibDeclare(n):
    cython.declare(a = cython.int,
                   b = cython.int,
                   i = cython.int)
                   
    a, b = 1,1
    for i in range(n):
        a,b = a+b, a
    return a

print fibDeclare(20)



