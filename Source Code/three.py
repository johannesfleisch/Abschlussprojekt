#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
**Titel: Aufgabe 3**
*Autor: Johannes Fleisch*
Beschreibung: Kurzes Programm zum Plotten des Monatsmittels der 2m-Temperatur und des Niederschlages über 1979-2019 inklusive Standardabweichung.
"""

# import required modules
import numpy as np
import matplotlib.pyplot as plt
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
    RAINS = RAIN.variables['prate'][:]

def get_january():
    """
    **Titel: Jänner-Daten generieren**

    *Beschreibung: Berechnen der mittleren 2m-Temperatur und des mittleren Niederschlages im Jänner über 1979-2019*

    :variable january: Werte der 2m-Temperatur im Jänner

    :variable january_r: Werte der Niederschlagsrate im Jänner

    :constant JANUARY_MEAN: Mittelwert der 2m-Temperatur im Jänner

    :constant JANUARY_STD: Standardabweichung der 2m-Temperatur im Jänner

    :constant JANUARY_R_MEAN: Mittelwert der Niederschlagsrate im Jänner

    :constant JANUARY_R_STD: Standardabweichung der Niederschlagsrate im Jänner 
    """
    global JANUARY_MEAN
    global JANUARY_STD
    global JANUARY_R_MEAN
    global JANUARY_R_STD

    liste_1 = []
    liste_13 = []
    i = 372
    while True:
        if i < 863:
            jan = AIRS[i]
            jan_r = RAINS[i]
            liste_1.extend(jan)
            liste_13.extend(jan_r)
            i = i + 12
        else:
            break

    january = np.array(liste_1)
    JANUARY_MEAN = np.mean(january)
    JANUARY_STD = np.std(january)

    january_r = np.array(liste_13)
    JANUARY_R_MEAN = np.mean(january_r)
    JANUARY_R_STD = np.std(january_r)

def get_february():
    """
    **Titel: Februar-Daten generieren**

    *Beschreibung: Berechnen der mittleren 2m-Temperatur und des mittleren Niederschlages im Februar über 1979-2019*

    :variable february: Werte der 2m-Temperatur im Februar

    :variable february_r: Werte der Niederschlagsrate im Februar

    :constant FEBRUARY_MEAN: Mittelwert der 2m-Temperatur im Februar

    :constant FEBRUARY_STD: Standardabweichung der 2m-Temperatur im Februar

    :constant FEBRUARY_R_MEAN: Mittelwert der Niederschlagsrate im Februar

    :constant FEBRUARY_R_STD: Standardabweichung der Niederschlagsrate im Februar
    """    
    global FEBRUARY_MEAN
    global FEBRUARY_STD
    global FEBRUARY_R_MEAN
    global FEBRUARY_R_STD

    liste_2 = []
    liste_14 = []
    i = 373
    while True:
        if i < 863:
            feb = AIRS[i]
            feb_r = RAINS[i]
            liste_2.extend(feb)
            liste_14.extend(feb_r)
            i = i + 12
        else:
            break

    february = np.array(liste_2)
    FEBRUARY_MEAN = np.mean(february)
    FEBRUARY_STD = np.std(february)

    february_r = np.array(liste_14)
    FEBRUARY_R_MEAN = np.mean(february_r)
    FEBRUARY_R_STD = np.std(february_r)

def get_march():
    """
    **Titel: März-Daten generieren**

    *Beschreibung: Berechnen der mittleren 2m-Temperatur und des mittleren Niederschlages im März über 1979-2019*

    :variable march: Werte der 2m-Temperatur im März

    :variable march_r: Werte der Niederschlagsrate im März

    :constant MARCH_MEAN: Mittelwert der 2m-Temperatur im März

    :constant MARCH_STD: Standardabweichung der 2m-Temperatur im März

    :constant MARCH_R_MEAN: Mittelwert der Niederschlagsrate im März

    :constant MARCH_R_STD: Standardabweichung der Niederschlagsrate im März
    """    
    global MARCH_MEAN
    global MARCH_STD
    global MARCH_R_MEAN
    global MARCH_R_STD

    liste_3 = []
    liste_15 = []
    i = 374
    while True:
        if i < 863:
            mar = AIRS[i]
            mar_r = RAINS[i]
            liste_3.extend(mar)
            liste_15.extend(mar_r)
            i = i + 12
        else:
            break

    march = np.array(liste_3)
    MARCH_MEAN = np.mean(march)
    MARCH_STD = np.std(march)

    march_r = np.array(liste_15)
    MARCH_R_MEAN = np.mean(march_r)
    MARCH_R_STD = np.std(march_r)

def get_april():
    """
    **Titel: April-Daten generieren**

    *Beschreibung: Berechnen der mittleren 2m-Temperatur und des mittleren Niederschlages im März über 1979-2019*

    :variable april: Werte der 2m-Temperatur im April

    :variable april_r: Werte der Niederschlagsrate im April

    :constant APRIL_MEAN: Mittelwert der 2m-Temperatur im April

    :constant APRIL_STD: Standardabweichung der 2m-Temperatur im April

    :constant APRIL_R_MEAN: Mittelwert der Niederschlagsrate im April

    :constant APRIL_R_STD: Standardabweichung der Niederschlagsrate im April
    """    
    global APRIL_MEAN
    global APRIL_STD
    global APRIL_R_MEAN
    global APRIL_R_STD

    liste_4 = []
    liste_16 = []
    i = 375
    while True:
        if i < 863:
            apr = AIRS[i]
            apr_ = RAINS[i]
            liste_4.extend(apr)
            liste_16.extend(apr_)
            i = i + 12
        else:
            break

    april = np.array(liste_4)
    APRIL_MEAN = np.mean(april)
    APRIL_STD = np.std(april)

    april_r = np.array(liste_16)
    APRIL_R_MEAN = np.mean(april_r)
    APRIL_R_STD = np.std(april_r)

def get_may():
    """
    **Titel: Mai-Daten generieren**

    *Beschreibung: Berechnen der mittleren 2m-Temperatur und des mittleren Niederschlages im Mai über 1979-2019*

    :variable may: Werte der 2m-Temperatur im Mai

    :variable may_r: Werte der Niederschlagsrate im Mai

    :constant MAY_MEAN: Mittelwert der 2m-Temperatur im Mai

    :constant MAY_STD: Standardabweichung der 2m-Temperatur im Mai

    :constant MAY_R_MEAN: Mittelwert der Niederschlagsrate im Mai

    :constant MAY_R_STD: Standardabweichung der Niederschlagsrate im Mai
    """
    global MAY_MEAN
    global MAY_STD
    global MAY_R_MEAN
    global MAY_R_STD

    liste_5 = []
    liste_17 = []
    i = 376
    while True:
        if i < 863:
            ma_ = AIRS[i]
            ma_r = RAINS[i]
            liste_5.extend(ma_)
            liste_17.extend(ma_r)
            i = i + 12
        else:
            break

    may = np.array(liste_5)
    MAY_MEAN = np.mean(may)
    MAY_STD = np.std(may)

    may_r = np.array(liste_17)
    MAY_R_MEAN = np.mean(may_r)
    MAY_R_STD = np.std(may_r)

def get_june():
    """
    **Titel: Juni-Daten generieren**

    *Beschreibung: Berechnen der mittleren 2m-Temperatur und des mittleren Niederschlages im Juni über 1979-2019*

    :variable june: Werte der 2m-Temperatur im Juni

    :variable june_r: Werte der Niederschlagsrate im Juni

    :constant JUNE_MEAN: Mittelwert der 2m-Temperatur im Juni

    :constant JUNE_STD: Standardabweichung der 2m-Temperatur im Juni

    :constant JUNE_R_MEAN: Mittelwert der Niederschlagsrate im Juni

    :constant JUNE_R_STD: Standardabweichung der Niederschlagsrate im Juni
    """
    global JUNE_MEAN
    global JUNE_STD
    global JUNE_R_MEAN
    global JUNE_R_STD

    liste_6 = []
    liste_18 = []
    i = 377
    while True:
        if i < 863:
            jun = AIRS[i]
            jun_r = RAINS[i]
            liste_6.extend(jun)
            liste_18.extend(jun_r)
            i = i + 12
        else:
            break

    june = np.array(liste_6)
    JUNE_MEAN = np.mean(june)
    JUNE_STD = np.std(june)

    june_r = np.array(liste_18)
    JUNE_R_MEAN = np.mean(june_r)
    JUNE_R_STD = np.std(june_r)

def get_july():
    """
    **Titel: Juli-Daten generieren**

    *Beschreibung: Berechnen der mittleren 2m-Temperatur und des mittleren Niederschlages im Juli über 1979-2019*

    :variable july: Werte der 2m-Temperatur im Juli

    :variable july_r: Werte der Niederschlagsrate im Juli

    :constant JULY_MEAN: Mittelwert der 2m-Temperatur im Juli

    :constant JULY_STD: Standardabweichung der 2m-Temperatur im Juli

    :constant JULY_R_MEAN: Mittelwert der Niederschlagsrate im Juli

    :constant JULY_R_STD: Standardabweichung der Niederschlagsrate im Juli
    """
    global JULY_MEAN
    global JULY_STD
    global JULY_R_MEAN
    global JULY_R_STD

    liste_7 = []
    liste_19 = []
    i = 378
    while True:
        if i < 863:
            jul = AIRS[i]
            jul_r = RAINS[i]
            liste_7.extend(jul)
            liste_19.extend(jul_r)
            i = i + 12
        else:
            break

    july = np.array(liste_7)
    JULY_MEAN = np.mean(july)
    JULY_STD = np.std(july)

    july_r = np.array(liste_19)
    JULY_R_MEAN = np.mean(july_r)
    JULY_R_STD = np.std(july_r)

def get_august():
    """
    **Titel: März-Daten generieren**

    *Beschreibung: Berechnen der mittleren 2m-Temperatur und des mittleren Niederschlages im August über 1979-2019*

    :variable august: Werte der 2m-Temperatur im August

    :variable august_r: Werte der Niederschlagsrate im August

    :constant AUGUST_MEAN: Mittelwert der 2m-Temperatur im August

    :constant AUGUST_STD: Standardabweichung der 2m-Temperatur im August

    :constant AUGUST_R_MEAN: Mittelwert der Niederschlagsrate im August

    :constant AUGUST_R_STD: Standardabweichung der Niederschlagsrate im August
    """    
    global AUGUST_MEAN
    global AUGUST_STD
    global AUGUST_R_MEAN
    global AUGUST_R_STD

    liste_8 = []
    liste_20 = []
    i = 379
    while True:
        if i < 863:
            aug = AIRS[i]
            aug_r = RAINS[i]
            liste_8.extend(aug)
            liste_20.extend(aug_r)
            i = i + 12
        else:
            break

    august = np.array(liste_8)
    AUGUST_MEAN = np.mean(august)
    AUGUST_STD = np.std(august)

    august_r = np.array(liste_20)
    AUGUST_R_MEAN = np.mean(august_r)
    AUGUST_R_STD = np.std(august_r)

def get_september():
    """
    **Titel: September-Daten generieren**

    *Beschreibung: Berechnen der mittleren 2m-Temperatur und des mittleren Niederschlages im September über 1979-2019*

    :variable september: Werte der 2m-Temperatur im September

    :variable september_r: Werte der Niederschlagsrate im September

    :constant SEPTEMBER_MEAN: Mittelwert der 2m-Temperatur im September

    :constant SEPTEMBER_STD: Standardabweichung der 2m-Temperatur im September

    :constant SEPTEMBER_R_MEAN: Mittelwert der Niederschlagsrate im September

    :constant SEPTEMBER_R_STD: Standardabweichung der Niederschlagsrate im September
    """
    global SEPTEMBER_MEAN
    global SEPTEMBER_STD
    global SEPTEMBER_R_MEAN
    global SEPTEMBER_R_STD

    liste_9 = []
    liste_21 = []
    i = 380
    while True:
        if i < 863:
            sep = AIRS[i]
            sep_r = RAINS[i]
            liste_9.extend(sep)
            liste_21.extend(sep_r)
            i = i + 12
        else:
            break

    september = np.array(liste_9)
    SEPTEMBER_MEAN = np.mean(september)
    SEPTEMBER_STD = np.std(september)

    september_r = np.array(liste_21)
    SEPTEMBER_R_MEAN = np.mean(september_r)
    SEPTEMBER_R_STD = np.std(september_r)

def get_october():
    """
    **Titel: Oktober-Daten generieren**

    *Beschreibung: Berechnen der mittleren 2m-Temperatur und des mittleren Niederschlages im Oktober über 1979-2019*

    :variable october: Werte der 2m-Temperatur im Oktober

    :variable october_r: Werte der Niederschlagsrate im Oktober

    :constant OCTOBER_MEAN: Mittelwert der 2m-Temperatur im Oktober

    :constant OCTOBER_STD: Standardabweichung der 2m-Temperatur im Oktober

    :constant OCTOBER_R_MEAN: Mittelwert der Niederschlagsrate im Oktober

    :constant OCTOBER_R_STD: Standardabweichung der Niederschlagsrate im Oktober
    """
    global OCTOBER_MEAN
    global OCTOBER_STD
    global OCTOBER_R_MEAN
    global OCTOBER_R_STD

    liste_10 = []
    liste_22 = []
    i = 381
    while True:
        if i < 863:
            octo = AIRS[i]
            octo_r = RAINS[i]
            liste_10.extend(octo)
            liste_22.extend(octo_r)
            i = i + 12
        else:
            break

    october = np.array(liste_10)
    OCTOBER_MEAN = np.mean(october)
    OCTOBER_STD = np.std(october)

    october_r = np.array(liste_22)
    OCTOBER_R_MEAN = np.mean(october_r)
    OCTOBER_R_STD = np.std(october_r)

def get_november():
    """
    **Titel: November-Daten generieren**

    *Beschreibung: Berechnen der mittleren 2m-Temperatur und des mittleren Niederschlages im November über 1979-2019*

    :variable november: Werte der 2m-Temperatur im November

    :variable november_r: Werte der Niederschlagsrate im November

    :constant NOVEMBER_MEAN: Mittelwert der 2m-Temperatur im November

    :constant NOVEMBER_STD: Standardabweichung der 2m-Temperatur im November

    :constant NOVEMBER_R_MEAN: Mittelwert der Niederschlagsrate im November

    :constant NOVEMBER_R_STD: Standardabweichung der Niederschlagsrate im November
    """    
    global NOVEMBER_MEAN
    global NOVEMBER_STD
    global NOVEMBER_R_MEAN
    global NOVEMBER_R_STD

    liste_11 = []
    liste_23 = []
    i = 382
    while True:
        if i < 863:
            nov = AIRS[i]
            nov_r = RAINS[i]
            liste_11.extend(nov)
            liste_23.extend(nov_r)
            i = i + 12
        else:
            break

    november = np.array(liste_11)
    NOVEMBER_MEAN = np.mean(november)
    NOVEMBER_STD = np.std(november)

    november_r = np.array(liste_23)
    NOVEMBER_R_MEAN = np.mean(november_r)
    NOVEMBER_R_STD = np.std(november_r)

def get_december():
    """
    **Titel: Dezember-Daten generieren**

    *Beschreibung: Berechnen der mittleren 2m-Temperatur und des mittleren Niederschlages im Dezember über 1979-2019*

    :variable december: Werte der 2m-Temperatur im Dezember

    :variable december_r: Werte der Niederschlagsrate im Dezember

    :constant DECEMBER_MEAN: Mittelwert der 2m-Temperatur im Dezember

    :constant DECEMBER_STD: Standardabweichung der 2m-Temperatur im Dezember

    :constant DECEMBER_R_MEAN: Mittelwert der Niederschlagsrate im Dezember

    :constant DECEMBER_R_STD: Standardabweichung der Niederschlagsrate im Dezember
    """
    global DECEMBER_MEAN
    global DECEMBER_STD
    global DECEMBER_R_MEAN
    global DECEMBER_R_STD

    liste_12 = []
    liste_24 = []
    i = 383
    while True:
        if i < 863:
            dec = AIRS[i]
            dec_r = RAINS[i]
            liste_12.extend(dec)
            liste_24.extend(dec_r)
            i = i + 12
        else:
            break

    december = np.array(liste_12)
    DECEMBER_MEAN = np.mean(december)
    DECEMBER_STD = np.std(december)

    december_r = np.array(liste_24)
    DECEMBER_R_MEAN = np.mean(december_r)
    DECEMBER_R_STD = np.std(december_r)

def plot_months_temp():
    """
    **Titel: Funktion plotten**    

    *Beschreibung: Plotten des Monatsmittels der 2m-Temperatur über 1979-2019 inklusive Standardabweichung*

    :variable monate: Monatsnamen

    :variable monatsmitteltemperaturen: Mittelwerte der 2m-Temperatur aller Monate

    :variable y_err: Standardabweichungen der 2m-Temperatur aller Monate 

    :method plt.figure: erstellt Figure

    :method plt.errorbar: erstellt Fehlerbalken

    :method plt.xlabel: erstellt x-Achsenbeschriftung 

    :method plt.ylabel: erstellt y-Achsenbeschriftung

    :method plt.title: erstellt Titel 

    :method plt.plot: führt Daten der x- und y-Achse zusammen

    :method plt.savefig: speichert den Plot

    :method plt.show: zeigt den Plot
    """
    # create figure
    plt.figure(figsize=(16, 10))

    # create data
    monate = ['Jänner', 'Februar', 'März', 'April', 'Mai', 'Juni', 'Juli', 'August', 'September', 'Oktober', 'November', 'Dezember']
    monatsmitteltemperaturen = [JANUARY_MEAN, FEBRUARY_MEAN, MARCH_MEAN, APRIL_MEAN, MAY_MEAN, JUNE_MEAN, JULY_MEAN, AUGUST_MEAN, SEPTEMBER_MEAN, OCTOBER_MEAN, NOVEMBER_MEAN, DECEMBER_MEAN]

    # create errorbar
    y_err = [JANUARY_STD, FEBRUARY_STD, MARCH_STD, APRIL_STD, MAY_STD, JUNE_STD, JULY_STD, AUGUST_STD, SEPTEMBER_STD, OCTOBER_STD, NOVEMBER_STD, DECEMBER_STD]
    plt.errorbar(monate, monatsmitteltemperaturen, yerr=y_err, fmt='.')

    # create plot and add labels and title
    plt.xlabel('Monate', size=12)
    plt.ylabel('Temperatur in [K]')
    plt.title('Monatsmittel der 2m-Temperatur über 1979-2019 inklusive Standardabweichung', size=16)
    plt.plot(monate, monatsmitteltemperaturen)

    # show plot and save figure
    plt.savefig('C1_Monatsmittel_2m-Temperatur_1979-2019.png')
    plt.show()

def plot_months_rain():
    """
    **Titel: Funktion plotten**    

    *Beschreibung: Plotten des Monatsmittels der Niederschlagsrate über 1979-2019 inklusive Standardabweichung*
    
    :variable monate: Monatsnamen

    :variable monatsmitteltemperaturen: Mittelwerte der Niederschlagsrate aller Monate

    :variable y_err: Standardabweichungen der Niederschlagsrate aller Monate 

    :method plt.figure: erstellt Figure

    :method plt.errorbar: erstellt Fehlerbalken

    :method plt.xlabel: erstellt x-Achsenbeschriftung 

    :method plt.ylabel: erstellt y-Achsenbeschriftung

    :method plt.title: erstellt Titel 

    :method plt.plot: führt Daten der x- und y-Achse zusammen

    :method plt.savefig: speichert den Plot

    :method plt.show: zeigt den Plot
    """
    # create figure
    plt.figure(figsize=(16, 10))

    # create data
    monate_r = ['Jänner', 'Februar', 'März', 'April', 'Mai', 'Juni', 'Juli', 'August', 'September', 'Oktober', 'November', 'Dezember']
    monatsmitteltemperaturen_r = [JANUARY_MEAN * 100000, FEBRUARY_MEAN * 100000, MARCH_MEAN * 100000, APRIL_MEAN * 100000, MAY_MEAN * 100000, JUNE_MEAN * 100000, JULY_MEAN * 100000, AUGUST_MEAN * 100000, SEPTEMBER_MEAN * 100000, OCTOBER_MEAN * 100000, NOVEMBER_MEAN * 100000, DECEMBER_MEAN * 100000]

    # create errorbars
    y_err_r = [JANUARY_STD * 100000, FEBRUARY_STD * 100000, MARCH_STD * 100000, APRIL_STD * 100000, MAY_STD * 100000, JUNE_STD * 100000, JULY_STD * 100000, AUGUST_STD * 100000, SEPTEMBER_STD * 100000, OCTOBER_STD * 100000, NOVEMBER_STD * 100000, DECEMBER_STD * 100000]
    plt.errorbar(monate_r, monatsmitteltemperaturen_r, yerr=y_err_r, fmt='.')

    # create plot and add labels and title
    plt.xlabel('Monate', size=12)
    plt.ylabel('Niederschlagsrate in [g/dm²/s]', size=12)
    plt.title('Monatsmittel der Niederschlagsrate über 1979-2019 inklusive Standardabweichung', size=16)
    plt.plot(monate_r, monatsmitteltemperaturen_r)

    # show plot and save figure
    plt.savefig('C2_Monatsmittel_Niederschlagsrate_1979-2019.png')
    plt.show()

# execute functions
if __name__ == '__main__':
    read_data()
    read_variables()
    get_january()
    get_february()
    get_march()
    get_april()
    get_may()
    get_june()
    get_july()
    get_august()
    get_september()
    get_october()
    get_november()
    get_december()
    plot_months_temp()
    plot_months_rain()
    