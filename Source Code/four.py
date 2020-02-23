#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
**Titel: Aufgabe 4**
*Autor: Johannes Fleisch*
Beschreibung: Kurzes Programm zum Plotten der saisonalen Mittel der 2m-Temperatur und des Niederschlages über 1979-2019 auf einer Weltkarte.
"""

# import required modules
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
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

    :variable LONS: Längengrad

    :variable LATS: Breitengrad

    :variable AIRS: Temperatur

    :variable RAINS: Niederschlagsrate
    """
    global LONS
    global LATS
    global AIRS
    global RAINS
    LONS = TEMP.variables['lon'][:]
    LATS = TEMP.variables['lat'][:]
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

def plot_winter_temp():
    """
    **Titel: Funktion plotten**    

    *Beschreibung: Plotten der mittleren 2m-Temperatur im Winter über 1979-2019 auf einer Weltkarte*
    
    :variable transform: transformiert Koordinaten

    :variable lons_trans: transformierte Längengrade

    :variable ind: übergibt Indizes der Längengrade

    :variable lons_trans_ind: Indizes der transformierten Längengrade

    :variable airs_new: neue Temperaturdaten

    :variable m: erstellt Basemap

    :variable lon, lat: Längen- und Breitengrade

    :variable xis, yis: x- und y-Koordinaten

    :variale met: spielt die Daten auf die Karte

    :variable cbar: erstellt Legende

    :method plt.figure: erstellt Figure

    :method m.drawparallels: zeichnet Breitengrade

    :method m.drawmeridians: zeichnet Längengrade

    :method m.drawcoastlines: zeichnet Küste

    :method m.drawstates: zeichnet Staaten

    :method m.drawcountries: zeichnet Länder

    :method cbar.set_label: erstellt Legendenbeschriftung

    :method plt.xlabel: erstellt x-Achsenbeschriftung 

    :method plt.ylabel: erstellt y-Achsenbeschriftung

    :method plt.title: erstellt Titel

    :method plt.savefig: speichert den Plot

    :method plt.show: zeigt den Plot
    """
    # transform coordinates
    transform = lambda x: ((x+180) % 360) - 180
    lons_trans = transform(LONS)

    # rearange data
    ind = np.argsort(lons_trans)
    lons_trans_ind = lons_trans[ind]
    winter_new = WINTER[:, :, ind]

    # create figure and basemap
    plt.figure(figsize=(16, 10))
    m = Basemap(projection='mill', llcrnrlat=-90, urcrnrlat=90, llcrnrlon=-180, urcrnrlon=180, resolution='c')

    # create 2D arrays
    lon, lat = np.meshgrid(lons_trans_ind, LATS)
    xis, yis = m(lon, lat)

    # add grid lines
    m.drawparallels(np.arange(-90., 120., 30.), labels=[1, 0, 0, 0])
    m.drawmeridians(np.arange(-180., 180., 60.), labels=[0, 0, 0, 1])

    # add coastlines, states, and country boundaries
    m.drawcoastlines()
    m.drawstates()
    m.drawcountries()

    # plot data and add colorbar
    met = m.contourf(xis, yis, winter_new[0, :, :])
    cbar = m.colorbar(met, location='bottom', pad="12%")
    cbar.set_label('Temperatur in [K]', size=12)

     # add title and labels
    plt.xlabel('Breitengrade', labelpad=25, size=12)
    plt.ylabel('Längengrade', labelpad=25, size=12)
    plt.title('Mittlere 2m-Temperatur im Winter über 1979-2019', size=16)

    # show plot and save figure
    plt.savefig('D1_Mittelwert_2m-Temperatur_Winter_1979-2019.png')
    plt.show()

def plot_spring_temp():
    """
    **Titel: Funktion plotten**    

    *Beschreibung: Plotten der mittleren 2m-Temperatur im Frühling über 1979-2019 auf einer Weltkarte*
    
    :variable transform: transformiert Koordinaten

    :variable lons_trans: transformierte Längengrade

    :variable ind: übergibt Indizes der Längengrade

    :variable lons_trans_ind: Indizes der transformierten Längengrade

    :variable airs_new: neue Temperaturdaten

    :variable m: erstellt Basemap

    :variable lon, lat: Längen- und Breitengrade

    :variable xis, yis: x- und y-Koordinaten

    :variale met: spielt die Daten auf die Karte

    :variable cbar: erstellt Legende

    :method plt.figure: erstellt Figure

    :method m.drawparallels: zeichnet Breitengrade

    :method m.drawmeridians: zeichnet Längengrade

    :method m.drawcoastlines: zeichnet Küste

    :method m.drawstates: zeichnet Staaten

    :method m.drawcountries: zeichnet Länder

    :method cbar.set_label: erstellt Legendenbeschriftung

    :method plt.xlabel: erstellt x-Achsenbeschriftung 

    :method plt.ylabel: erstellt y-Achsenbeschriftung

    :method plt.title: erstellt Titel

    :method plt.savefig: speichert den Plot

    :method plt.show: zeigt den Plot
    """
    # transform coordinates
    transform = lambda x: ((x+180) % 360) - 180
    lons_trans = transform(LONS)

    # rearange data
    ind = np.argsort(lons_trans)
    lons_trans_ind = lons_trans[ind]
    spring_new = SPRING[:, :, ind]

    # create figure and basemap
    plt.figure(figsize=(16, 10))
    m = Basemap(projection='mill', llcrnrlat=-90, urcrnrlat=90, llcrnrlon=-180, urcrnrlon=180, resolution='c')

    # create 2D arrays
    lon, lat = np.meshgrid(lons_trans_ind, LATS)
    xis, yis = m(lon, lat)

    # add grid lines
    m.drawparallels(np.arange(-90., 120., 30.), labels=[1, 0, 0, 0])
    m.drawmeridians(np.arange(-180., 180., 60.), labels=[0, 0, 0, 1])

    # add coastlines, states, and country boundaries
    m.drawcoastlines()
    m.drawstates()
    m.drawcountries()

    # plot data and add colorbar
    met = m.contourf(xis, yis, spring_new[0, :, :])
    cbar = m.colorbar(met, location='bottom', pad="12%")
    cbar.set_label('Temperatur in [K]')

     # add title and labels
    plt.xlabel('Breitengrade', labelpad=25, size=12)
    plt.ylabel('Längengrade', labelpad=25, size=12)
    plt.title('Mittlere 2m-Temperatur im Frühling über 1979-2019', size=16)

    # show plot and save figure
    plt.savefig('D2_Mittelwert_2m-Temperatur_Fruehling_1979-2019.png')
    plt.show()

def plot_summer_temp():
    """
    **Titel: Funktion plotten**    

    *Beschreibung: Plotten der mittleren 2m-Temperatur im Sommer über 1979-2019 auf einer Weltkarte*
    
    :variable transform: transformiert Koordinaten

    :variable lons_trans: transformierte Längengrade

    :variable ind: übergibt Indizes der Längengrade

    :variable lons_trans_ind: Indizes der transformierten Längengrade

    :variable airs_new: neue Temperaturdaten

    :variable m: erstellt Basemap

    :variable lon, lat: Längen- und Breitengrade

    :variable xis, yis: x- und y-Koordinaten

    :variale met: spielt die Daten auf die Karte

    :variable cbar: erstellt Legende

    :method plt.figure: erstellt Figure

    :method m.drawparallels: zeichnet Breitengrade

    :method m.drawmeridians: zeichnet Längengrade

    :method m.drawcoastlines: zeichnet Küste

    :method m.drawstates: zeichnet Staaten

    :method m.drawcountries: zeichnet Länder

    :method cbar.set_label: erstellt Legendenbeschriftung

    :method plt.xlabel: erstellt x-Achsenbeschriftung 

    :method plt.ylabel: erstellt y-Achsenbeschriftung

    :method plt.title: erstellt Titel

    :method plt.savefig: speichert den Plot

    :method plt.show: zeigt den Plot
    """
    # transform coordinates
    transform = lambda x: ((x+180) % 360) - 180
    lons_trans = transform(LONS)

    # rearange data
    ind = np.argsort(lons_trans)
    lons_trans_ind = lons_trans[ind]
    summer_new = SUMMER[:, :, ind]

    # create figure and basemap
    plt.figure(figsize=(16, 10))
    m = Basemap(projection='mill', llcrnrlat=-90, urcrnrlat=90, llcrnrlon=-180, urcrnrlon=180, resolution='c')

    # create 2D arrays
    lon, lat = np.meshgrid(lons_trans_ind, LATS)
    xis, yis = m(lon, lat)

    # add grid lines
    m.drawparallels(np.arange(-90., 120., 30.), labels=[1, 0, 0, 0])
    m.drawmeridians(np.arange(-180., 180., 60.), labels=[0, 0, 0, 1])

    # add coastlines, states, and country boundaries
    m.drawcoastlines()
    m.drawstates()
    m.drawcountries()

    # plot data and add colorbar
    met = m.contourf(xis, yis, summer_new[0, :, :])
    cbar = m.colorbar(met, location='bottom', pad="12%")
    cbar.set_label('Temperatur in [K]', size=12)

     # add title and labels
    plt.xlabel('Breitengrade', labelpad=25, size=12)
    plt.ylabel('Längengrade', labelpad=25, size=12)
    plt.title('Mittlere 2m-Temperatur im Sommer über 1979-2019', size=16)

    # show plot and save figure
    plt.savefig('D3_Mittelwert_2m-Temperatur_Sommer_1979-2019.png')
    plt.show()

def plot_fall_temp():
    """
    **Titel: Funktion plotten**    

    *Beschreibung: Plotten der mittleren 2m-Temperatur im Herbst über 1979-2019 auf einer Weltkarte*
    
    :variable transform: transformiert Koordinaten

    :variable lons_trans: transformierte Längengrade

    :variable ind: übergibt Indizes der Längengrade

    :variable lons_trans_ind: Indizes der transformierten Längengrade

    :variable airs_new: neue Temperaturdaten

    :variable m: erstellt Basemap

    :variable lon, lat: Längen- und Breitengrade

    :variable xis, yis: x- und y-Koordinaten

    :variale met: spielt die Daten auf die Karte

    :variable cbar: erstellt Legende

    :method plt.figure: erstellt Figure

    :method m.drawparallels: zeichnet Breitengrade

    :method m.drawmeridians: zeichnet Längengrade

    :method m.drawcoastlines: zeichnet Küste

    :method m.drawstates: zeichnet Staaten

    :method m.drawcountries: zeichnet Länder

    :method cbar.set_label: erstellt Legendenbeschriftung

    :method plt.xlabel: erstellt x-Achsenbeschriftung 

    :method plt.ylabel: erstellt y-Achsenbeschriftung

    :method plt.title: erstellt Titel

    :method plt.savefig: speichert den Plot

    :method plt.show: zeigt den Plot
    """
    # transform coordinates
    transform = lambda x: ((x+180) % 360) - 180
    lons_trans = transform(LONS)

    # rearange data
    ind = np.argsort(lons_trans)
    lons_trans_ind = lons_trans[ind]
    fall_new = FALL[:, :, ind]

    # create figure and basemap
    plt.figure(figsize=(16, 10))
    m = Basemap(projection='mill', llcrnrlat=-90, urcrnrlat=90, llcrnrlon=-180, urcrnrlon=180, resolution='c')

    # create 2D arrays
    lon, lat = np.meshgrid(lons_trans_ind, LATS)
    xis, yis = m(lon, lat)

    # add grid lines
    m.drawparallels(np.arange(-90., 120., 30.), labels=[1, 0, 0, 0])
    m.drawmeridians(np.arange(-180., 180., 60.), labels=[0, 0, 0, 1])

    # add coastlines, states, and country boundaries
    m.drawcoastlines()
    m.drawstates()
    m.drawcountries()

    # plot data and add colorbar
    met = m.contourf(xis, yis, fall_new[0, :, :])
    cbar = m.colorbar(met, location='bottom', pad="12%")
    cbar.set_label('Temperatur in [K]', size=12)

     # add title and labels
    plt.xlabel('Breitengrade', labelpad=25, size=12)
    plt.ylabel('Längengrade', labelpad=25, size=12)
    plt.title('Mittlere 2m-Temperatur im Herbst über 1979-2019', size=16)

    # show plot and save figure
    plt.savefig('D4_Mittelwert_2m-Temperatur_Herbst_1979-2019.png')
    plt.show()

def plot_winter_rain():
    """
    **Titel: Funktion plotten**    

    *Beschreibung: Plotten der mittleren Niederschlagsrate im Winter über 1979-2019 auf einer Weltkarte*
    
    :variable transform: transformiert Koordinaten

    :variable lons_trans: transformierte Längengrade

    :variable ind: übergibt Indizes der Längengrade

    :variable lons_trans_ind: Indizes der transformierten Längengrade

    :variable airs_new: neue Temperaturdaten

    :variable m: erstellt Basemap

    :variable lon, lat: Längen- und Breitengrade

    :variable xis, yis: x- und y-Koordinaten

    :variale met: spielt die Daten auf die Karte

    :variable cbar: erstellt Legende

    :method plt.figure: erstellt Figure

    :method m.drawparallels: zeichnet Breitengrade

    :method m.drawmeridians: zeichnet Längengrade

    :method m.drawcoastlines: zeichnet Küste

    :method m.drawstates: zeichnet Staaten

    :method m.drawcountries: zeichnet Länder

    :method cbar.set_label: erstellt Legendenbeschriftung

    :method plt.xlabel: erstellt x-Achsenbeschriftung 

    :method plt.ylabel: erstellt y-Achsenbeschriftung

    :method plt.title: erstellt Titel

    :method plt.savefig: speichert den Plot

    :method plt.show: zeigt den Plot
    """
    # transform coordinates
    transform = lambda x: ((x+180) % 360) - 180
    lons_trans = transform(LONS)

    # rearange data
    ind = np.argsort(lons_trans)
    lons_trans_ind = lons_trans[ind]
    winter_r_new = WINTER_R[:, :, ind]

    # create figure and basemap
    plt.figure(figsize=(16, 10))
    m = Basemap(projection='mill', llcrnrlat=-90, urcrnrlat=90, llcrnrlon=-180, urcrnrlon=180, resolution='c')

    # create 2D arrays
    lon, lat = np.meshgrid(lons_trans_ind, LATS)
    xis, yis = m(lon, lat)

    # add grid lines
    m.drawparallels(np.arange(-90., 120., 30.), labels=[1, 0, 0, 0])
    m.drawmeridians(np.arange(-180., 180., 60.), labels=[0, 0, 0, 1])

    # add coastlines, states, and country boundaries
    m.drawcoastlines()
    m.drawstates()
    m.drawcountries()

    # plot data and add colorbar
    met = m.contourf(xis, yis, winter_r_new[0, :, :])
    cbar = m.colorbar(met, location='bottom', pad="12%")
    cbar.set_label('Niederschlagsrate in [g/dm²/s]', size=12)

     # add title and labels
    plt.xlabel('Breitengrade', labelpad=25, size=12)
    plt.ylabel('Längengrade', labelpad=25, size=12)
    plt.title('Mittlere Niederschlagsrate im Winter über 1979-2019', size=16)

    # show plot and save figure
    plt.savefig('D5_Mittelwert_Niederschlagsrate_Winter_1979-2019.png')
    plt.show()

def plot_spring_rain():
    """
    **Titel: Funktion plotten**    

    *Beschreibung: Plotten der mittleren Niederschlagsrate im Frühling über 1979-2019 auf einer Weltkarte*
    
    :variable transform: transformiert Koordinaten

    :variable lons_trans: transformierte Längengrade

    :variable ind: übergibt Indizes der Längengrade

    :variable lons_trans_ind: Indizes der transformierten Längengrade

    :variable airs_new: neue Temperaturdaten

    :variable m: erstellt Basemap

    :variable lon, lat: Längen- und Breitengrade

    :variable xis, yis: x- und y-Koordinaten

    :variale met: spielt die Daten auf die Karte

    :variable cbar: erstellt Legende

    :method plt.figure: erstellt Figure

    :method m.drawparallels: zeichnet Breitengrade

    :method m.drawmeridians: zeichnet Längengrade

    :method m.drawcoastlines: zeichnet Küste

    :method m.drawstates: zeichnet Staaten

    :method m.drawcountries: zeichnet Länder

    :method cbar.set_label: erstellt Legendenbeschriftung

    :method plt.xlabel: erstellt x-Achsenbeschriftung 

    :method plt.ylabel: erstellt y-Achsenbeschriftung

    :method plt.title: erstellt Titel

    :method plt.savefig: speichert den Plot

    :method plt.show: zeigt den Plot
    """
    # transform coordinates
    transform = lambda x: ((x+180) % 360) - 180
    lons_trans = transform(LONS)

    # rearange data
    ind = np.argsort(lons_trans)
    lons_trans_ind = lons_trans[ind]
    spring_r_new = SPRING_R[:, :, ind]

    # create figure and basemap
    plt.figure(figsize=(16, 10))
    m = Basemap(projection='mill', llcrnrlat=-90, urcrnrlat=90, llcrnrlon=-180, urcrnrlon=180, resolution='c')

    # create 2D arrays
    lon, lat = np.meshgrid(lons_trans_ind, LATS)
    xis, yis = m(lon, lat)

    # add grid lines
    m.drawparallels(np.arange(-90., 120., 30.), labels=[1, 0, 0, 0])
    m.drawmeridians(np.arange(-180., 180., 60.), labels=[0, 0, 0, 1])

    # add coastlines, states, and country boundaries
    m.drawcoastlines()
    m.drawstates()
    m.drawcountries()

    # plot data and add colorbar
    met = m.contourf(xis, yis, spring_r_new[0, :, :])
    cbar = m.colorbar(met, location='bottom', pad="12%")
    cbar.set_label('Niederschlagsrate in [g/dm²/s]')

     # add title and labels
    plt.xlabel('Breitengrade', labelpad=25, size=12)
    plt.ylabel('Längengrade', labelpad=25, size=12)
    plt.title('Mittlere Niederschlagsrate im Frühling über 1979-2019', size=16)

    # show plot and save figure
    plt.savefig('D6_Mittelwert_Niederschlagsrate_Fruehling_1979-2019.png')
    plt.show()

def plot_summer_rain():
    """
    **Titel: Funktion plotten**    

    *Beschreibung: Plotten der mittleren Niederschlagsrate im Sommer über 1979-2019 auf einer Weltkarte*
    
    :variable transform: transformiert Koordinaten

    :variable lons_trans: transformierte Längengrade

    :variable ind: übergibt Indizes der Längengrade

    :variable lons_trans_ind: Indizes der transformierten Längengrade

    :variable airs_new: neue Temperaturdaten

    :variable m: erstellt Basemap

    :variable lon, lat: Längen- und Breitengrade

    :variable xis, yis: x- und y-Koordinaten

    :variale met: spielt die Daten auf die Karte

    :variable cbar: erstellt Legende

    :method plt.figure: erstellt Figure

    :method m.drawparallels: zeichnet Breitengrade

    :method m.drawmeridians: zeichnet Längengrade

    :method m.drawcoastlines: zeichnet Küste

    :method m.drawstates: zeichnet Staaten

    :method m.drawcountries: zeichnet Länder

    :method cbar.set_label: erstellt Legendenbeschriftung

    :method plt.xlabel: erstellt x-Achsenbeschriftung 

    :method plt.ylabel: erstellt y-Achsenbeschriftung

    :method plt.title: erstellt Titel

    :method plt.savefig: speichert den Plot

    :method plt.show: zeigt den Plot
    """
    # transform coordinates
    transform = lambda x: ((x+180) % 360) - 180
    lons_trans = transform(LONS)

    # rearange data
    ind = np.argsort(lons_trans)
    lons_trans_ind = lons_trans[ind]
    summer_r_new = SUMMER_R[:, :, ind]

    # create figure and basemap
    plt.figure(figsize=(16, 10))
    m = Basemap(projection='mill', llcrnrlat=-90, urcrnrlat=90, llcrnrlon=-180, urcrnrlon=180, resolution='c')

    # create 2D arrays
    lon, lat = np.meshgrid(lons_trans_ind, LATS)
    xis, yis = m(lon, lat)

    # add grid lines
    m.drawparallels(np.arange(-90., 120., 30.), labels=[1, 0, 0, 0])
    m.drawmeridians(np.arange(-180., 180., 60.), labels=[0, 0, 0, 1])

    # add coastlines, states, and country boundaries
    m.drawcoastlines()
    m.drawstates()
    m.drawcountries()

    # plot data and add colorbar
    met = m.contourf(xis, yis, summer_r_new[0, :, :])
    cbar = m.colorbar(met, location='bottom', pad="12%")
    cbar.set_label('Niederschlagsrate in [g/dm²/s]', size=12)

    # add title and labels
    plt.xlabel('Breitengrade', labelpad=25, size=12)
    plt.ylabel('Längengrade', labelpad=25, size=12)
    plt.title('Mittlere Niederschlagsrate im Sommer über 1979-2019', size=16)

    # show plot and save figure
    plt.savefig('D7_Mittelwert_Niederschlagsrate_Sommer_1979-2019.png')
    plt.show()

def plot_fall_rain():
    """
    **Titel: Funktion plotten**    

    *Beschreibung: Plotten der mittleren Niederschlagsrate im Herbst über 1979-2019 auf einer Weltkarte*
    
    :variable transform: transformiert Koordinaten

    :variable lons_trans: transformierte Längengrade

    :variable ind: übergibt Indizes der Längengrade

    :variable lons_trans_ind: Indizes der transformierten Längengrade

    :variable airs_new: neue Temperaturdaten

    :variable m: erstellt Basemap

    :variable lon, lat: Längen- und Breitengrade

    :variable xis, yis: x- und y-Koordinaten

    :variale met: spielt die Daten auf die Karte

    :variable cbar: erstellt Legende

    :method plt.figure: erstellt Figure

    :method m.drawparallels: zeichnet Breitengrade

    :method m.drawmeridians: zeichnet Längengrade

    :method m.drawcoastlines: zeichnet Küste

    :method m.drawstates: zeichnet Staaten

    :method m.drawcountries: zeichnet Länder

    :method cbar.set_label: erstellt Legendenbeschriftung

    :method plt.xlabel: erstellt x-Achsenbeschriftung 

    :method plt.ylabel: erstellt y-Achsenbeschriftung

    :method plt.title: erstellt Titel

    :method plt.savefig: speichert den Plot

    :method plt.show: zeigt den Plot
    """
    # transform coordinates
    transform = lambda x: ((x+180) % 360) - 180
    lons_trans = transform(LONS)

    # rearange data
    ind = np.argsort(lons_trans)
    lons_trans_ind = lons_trans[ind]
    fall_r_new = FALL_R[:, :, ind]

    # create figure and basemap
    plt.figure(figsize=(16, 10))
    m = Basemap(projection='mill', llcrnrlat=-90, urcrnrlat=90, llcrnrlon=-180, urcrnrlon=180, resolution='c')

    # create 2D arrays
    lon, lat = np.meshgrid(lons_trans_ind, LATS)
    xis, yis = m(lon, lat)

    # add grid lines
    m.drawparallels(np.arange(-90., 120., 30.), labels=[1, 0, 0, 0])
    m.drawmeridians(np.arange(-180., 180., 60.), labels=[0, 0, 0, 1])

    # add coastlines, states, and country boundaries
    m.drawcoastlines()
    m.drawstates()
    m.drawcountries()

    # plot data and add colorbar
    met = m.contourf(xis, yis, fall_r_new[0, :, :])
    cbar = m.colorbar(met, location='bottom', pad="12%")
    cbar.set_label('Niederschlagsrate in [g/dm²/s]', size=12)

     # add title and labels
    plt.xlabel('Breitengrade', labelpad=25, size=12)
    plt.ylabel('Längengrade', labelpad=25, size=12)
    plt.title('Mittlere Niederschlagsrate im Herbst über 1979-2019', size=16)

    # show plot and save figure
    plt.savefig('D8_Mittelwert_Niederschlagsrate_Herbst_1979-2019.png')
    plt.show()

# execute functions
if __name__ == '__main__':
    read_data()
    read_variables()
    get_winter()
    get_spring()
    get_summer()
    get_fall()
    plot_winter_temp()
    plot_spring_temp()
    plot_summer_temp()
    plot_fall_temp()
    plot_winter_rain()
    plot_spring_rain()
    plot_summer_rain()
    plot_fall_rain()
    