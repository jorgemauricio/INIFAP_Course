#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 16:17:25 2017

@author: jorgemauricio

- 	Escribir un programa que genere un password aleatorio de al menos 8 caracteres. Debes de considerar que un password fuerte
	incluye letras minúsculas, mayúsculas, números y símbolos

"""

import random

s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
passlen = 8
pwd =  "".join(random.sample(s,passlen ))
print("Tu password es : {}".format(pwd))
