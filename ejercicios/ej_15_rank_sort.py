import numpy as np
from pandas import Series,DataFrame
import pandas as pd

# crear serie
ser1 = Series(range(3),index=['C','A','B'])

# desplegar
ser1

# ordenar por indice
ser1.sort_index()

# ordenar por valores
ser1.order()

# Rank

from numpy.random import randn
ser2 = Series(randn(10))

# desplegar
ser2

# desplegar el rank para ordenar los valores
ser2.rank()

# ordenar los valores
ser2.sort_values()

# desplegar
ser2

# despues de ordenar, checar el rank para ver si todo es logico
ser2.rank()