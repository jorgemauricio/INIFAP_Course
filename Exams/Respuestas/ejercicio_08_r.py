#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 16:17:25 2017

@author: jorgemauricio

- 	Escribir un programa el cual encuentre los numeros divisibles entre 7 pero que no sean multiplos
	de 5, entre los valores 1, 1000. Los numeros que se obtengan deben de imprimirse separados por una ","

"""

l = []
for i in range(1, 1000):
	if (i%7==0) and (i%5!=0):
		l.append(str(i))
print(','.join(l))
