#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
**Titel: Aufgabe 5.1**
*Autor: Johannes Fleisch*
Beschreibung: Kurzes Programm zum Plotten des saisonalen und räumlichen Mittels der 2m-Temperatur über 1979-2019.
"""

#importieren der Module
import numpy as np
import pandas as pd
import seaborn as sns
from netCDF4 import Dataset

def read_data():
    """
    **Titel: Daten einlesen**

    *Beschreibung: Funktion zum Lesen der netCDF-Datei*
     
    :variable TEMP: Daten für Temperaturen

    :variable RAIN: Daten für Niederschlagsraten

    :method Dataset: Lesen der Datei
    """
    global TEMP
    global RAIN
    TEMP = Dataset('air.2m.mon.mean.nc', 'r')
    RAIN = Dataset('prate.sfc.mon.mean.nc', 'r')

def read_variables():
    """
    **Titel: Variablen definieren**

    *Beschreibung: Funktion zum Definieren der Variablen*

    :variable AIRS: Temperatur

    :variable RAINS: Niederschlagsrate
    """
    global AIRS
    global RAINS
    AIRS = TEMP.variables['air'][:]
    RAINS = RAIN.variables['prate'][:] * 100000

def get_winter():
    """
    **Titel: Winter-Daten generieren**

    *Beschreibung: Zusammenführen der 2m-Temperatur bzw. des Niederschlages aller Wintermonate über 1979-2019*

    :constant WINTER: Werte der 2m-Temperatur im Winter

    :constant WINTER_R: Werte der Niederschlagsrate im Winter
    """
    global WINTER
    global WINTER_R
    liste_1 = []
    liste_5 = []
    i = 371
    while True:
        if i < 862:
            win = AIRS[i:i+3]
            win_r = RAINS[i:i+3]
            liste_1.extend(win)
            liste_5.extend(win_r)
            i = i + 12
        else:
            break
    WINTER = np.array(liste_1)
    WINTER_R = np.array(liste_5)

def get_spring():
    """
    **Titel: Frühlings-Daten generieren**

    *Beschreibung: Zusammenführen der 2m-Temperatur bzw. des Niederschlages aller Frühlingsmonate über 1979-2019*

    :constant SPRING: Werte der 2m-Temperatur im Frühling

    :constant SPRING_R: Werte der Niederschlagsrate im Frühling
    """
    global SPRING
    global SPRING_R
    liste_2 = []
    liste_6 = []
    i = 374
    while True:
        if i < 862:
            spr = AIRS[i:i+3]
            spr_r = RAINS[i:i+3]
            liste_2.extend(spr)
            liste_6.extend(spr_r)
            i = i + 12
        else:
            break
    SPRING = np.array(liste_2)
    SPRING_R = np.array(liste_6)

def get_summer():
    """
    **Titel: Sommer-Daten generieren**

    *Beschreibung: Zusammenführen der 2m-Temperatur bzw. des Niederschlages aller Sommermonate über 1979-2019*

    :constant SUMMER: Werte der 2m-Temperatur im Sommer

    :constant SUMMER_R: Werte der Niederschlagsrate im Sommer
    """
    global SUMMER
    global SUMMER_R
    liste_3 = []
    liste_7 = []
    i = 377
    while True:
        if i < 862:
            sum_ = AIRS[i:i+3]
            sum_r = RAINS[i:i+3]
            liste_3.extend(sum_)
            liste_7.extend(sum_r)
            i = i + 12
        else:
            break
    SUMMER = np.array(liste_3)
    SUMMER_R = np.array(liste_7)

def get_fall():
    """
    **Titel: Herbst-Daten generieren**

    *Beschreibung: Zusammenführen der 2m-Temperatur bzw. des Niederschlages aller Herbstmonate über 1979-2019*

    :constant FALL: Werte der 2m-Temperatur im Herbst

    :constant FALL_R: Werte der Niederschlagsrate im Herbst
    """
    global FALL
    global FALL_R
    liste_4 = []
    liste_8 = []
    i = 380
    while True:
        if i < 862:
            fal = AIRS[i:i+3]
            fal_r = RAINS[i:i+3]
            liste_4.extend(fal)
            liste_8.extend(fal_r)
            i = i + 12
        else:
            break
    FALL = np.array(liste_4)
    FALL_R = np.array(liste_8)

def plot_violinplot_temp():
    """
    **Titel: Funktion plotten** 

    *Beschreibung: Plotten des saisonalen und räumlichen Mittels der 2m-Temperatur über 1979-2019*

    :variable win_temp: wandelt Winter-Daten für 2m-Temperatur um

    :variable spr_temp: wandelt Frühlings-Daten für 2m-Temperatur um

    :variable sum_temp: wandelt Sommer-Daten für 2m-Temperatur um

    :variable fal_temp: wandelt Herbst-Daten für 2m-Temperatur um

    :variable temp: DataFrame

    :variable axair: bespielt Diagramm mit Daten

    :method axair.set_title: erstellt Titel

    :method axair.grid: erstellt Raster

    :method figair.savefig: speichert den Plot 
    """
    # convert 3D-Array into 1D-Array
    win_temp = WINTER.ravel()
    spr_temp = SPRING.ravel()
    sum_temp = SUMMER.ravel()
    fal_temp = FALL.ravel()

    temp = pd.DataFrame(
        {
            "Jahreszeiten": ["Winter", "Frühling", "Sommer", "Herbst"],
            "Temperatur in [K]": [
                win_temp,
                spr_temp,
                sum_temp,
                fal_temp,
            ],
        }
    )

    temp = temp.explode("Temperatur in [K]")
    temp["Temperatur in [K]"] = temp["Temperatur in [K]"].astype("float")
    axair = sns.violinplot(x="Jahreszeiten", y="Temperatur in [K]", data=temp, gridsize=100)
    axair.set_title("Saisonle Mittel der 2m-Temperatur über 1979-2019 als Percentile")
    axair.grid()

    figair = axair.get_figure()
    figair.savefig("E1_2m-Temperatur_Percentile_1979-2019.png")

# execute functions
if __name__ == '__main__':
    read_data()
    read_variables()
    get_winter()
    get_spring()
    get_summer()
    get_fall()
    plot_violinplot_temp()
