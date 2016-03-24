'''
Created on Mar 8, 2015

@author: edwingsantos
'''
""""
$ cython mycodepy.pyx
$ gcc -g -O2 -fpic -c mycode.c -o mycode.o
$ gcc -g -O2 -fpic `python-config --cflags` -c mycode.c -o mycode.o
$ gcc -shared -o mycode.so mycode.o `python-config --libs`
"""

