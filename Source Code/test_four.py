#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
**Titel: Testing 1**
*Autor: Johannes Fleisch*
Beschreibung: Kurzes Programm zum Testen einer Funktion.
"""

# import required modules
import numpy as np
from netCDF4 import Dataset

def read_data_and_get_january(AIRS):
    TEMP = Dataset('air.2m.mon.mean.nc', 'r')
    AIRS = TEMP.variables['air'][:]

    liste_1 = []
    i = 372
    while True:
        if i < 862:
            jan = AIRS[i]
            liste_1.extend(jan)
            i = i + 12
        else:
            break
        
    january = np.array(liste_1)
    return january

def test_for_read_data_and_get_january():
    """Testfunktion, um die korrekte Durchführbarkeit der Funktion zu überprüfen"""
    assert type(read_data_and_get_january([862])) == "<class 'numpy.ndarray'>"
    