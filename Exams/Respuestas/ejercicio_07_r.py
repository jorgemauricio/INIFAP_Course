#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 16:17:25 2017

@author: jorgemauricio

Instrucciones

- Cambiar el valor de dos variables sin utilizar una variable temporal

"""

x = 5
y = 7

print("Original")
print("x = {}".format(x))
print("y = {}".format(y))

x, y = y,x

print("Cambio")
print("x = {}".format(x))
print("y = {}".format(y))