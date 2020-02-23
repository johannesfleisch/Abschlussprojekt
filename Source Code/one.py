#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
**Titel: Aufgabe 1**
*Autor: Johannes Fleisch*
Beschreibung: Kurzes Programm zum Plotten des Mittelwertes der 2m-Temperatur und des Niederschlages über 1979-2019 auf einer Weltkarte.
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
    AIRS = TEMP.variables['air'][372:864]
    RAINS = RAIN.variables['prate'][372:864] * 100000

def plot_mean_temp():
    """
    **Titel: Funktion plotten**    

    *Beschreibung: Plotten des Mittelwertes der 2m-Temperatur über 1979-2019 auf einer Weltkarte*
    
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
    airs_new = AIRS[:, :, ind]

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
    met = m.contourf(xis, yis, airs_new[0, :, :])
    cbar = m.colorbar(met, location='bottom', pad="12%")
    cbar.set_label('Temperatur in [K]', size=12)

     # add title and labels
    plt.xlabel('Breitengrade', labelpad=25, size=12)
    plt.ylabel('Längengrade', labelpad=25, size=12)
    plt.title('Mittelwert der 2m-Temperatur über 1979-2019', size=16)

    # show plot and save figure
    plt.savefig('A1_Mittelwert_2m-Temperatur_1979-2019.png')
    plt.show()

def plot_mean_rain():
    """
    **Titel: Funktion plotten**    

    *Beschreibung: Plotten des Mittelwertes des Niederschlages über 1979-2019 auf einer Weltkarte*
    
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
    rains_new = RAINS[:, :, ind]

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
    met = m.contourf(xis, yis, rains_new[0, :, :])
    cbar = m.colorbar(met, location='bottom', pad="12%")
    cbar.set_label('Niederschlagsrate in [g/dm²/s]', size=12)

    # add title and labels
    plt.xlabel('Breitengrade', labelpad=25, size=12)
    plt.ylabel('Längengrade', labelpad=25, size=12)
    plt.title('Mittelwert der Niederschlagsrate über 1979-2019', size=16)

    # show plot and save figure
    plt.savefig('A2_Mittelwert_Niederschlagsrate_1979-2019.png')
    plt.show()

# execute functions
if __name__ == '__main__':
    read_data()
    read_variables()
    plot_mean_temp()
    plot_mean_rain()
