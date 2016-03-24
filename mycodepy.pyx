cdef extern from "mycode.h":
    cdef int myfunc(int, int)
def myfunc(a, b):
    return a + b
def callCfunc():
    print myfunc(1,2)