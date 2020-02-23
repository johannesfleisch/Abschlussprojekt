#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
**Titel: Aufgabe 2**
*Autor: Johannes Fleisch*
Beschreibung: Kurzes Programm zum Plotten der mittleren 2m-Temperaturanomalie und Niederschlagsanomalie im Jahr 2019 im Vergleich zum Mittelwert über 1979-2019 auf einer Weltkarte.
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

    :variable AIRS_A: Temperaturanomalie

    :variable RAINS: Niederschlagsrate

    :variable RAINS_A: Niederschlagsanomalie
    """
    global LONS
    global LATS
    global AIRS
    global AIRS_A
    global RAINS
    global RAINS_A
    LONS = TEMP.variables['lon'][:]
    LATS = TEMP.variables['lat'][:]
    AIRS = TEMP.variables['air'][:]
    AIRS_A = (AIRS[372:384] + AIRS[384:396] + AIRS[396:408] + AIRS[408:420] + AIRS[420:432] + AIRS[432:444] + AIRS[444:456] + AIRS[456:468] + AIRS[468:480] + AIRS[480:492] + AIRS[492:504] + AIRS[504:516] + AIRS[516:528] + AIRS[528:540] + AIRS[540:552] + AIRS[552:564] + AIRS[564:576] + AIRS[576:588] + AIRS[588:600] + AIRS[600:612] + AIRS[612:624] + AIRS[624:636] + AIRS[636:648] + AIRS[648:660] + AIRS[660:672] + AIRS[672:684] + AIRS[684:696] + AIRS[696:708] + AIRS[708:720] + AIRS[720:732] + AIRS[732:744] + AIRS[744:756] + AIRS[756:768] + AIRS[768:780] + AIRS[780:792] + AIRS[792:804] + AIRS[804:816] + AIRS[816:828] + AIRS[828:840] + AIRS[840:852] + AIRS[852:864])/41 - AIRS[852:864]    
    RAINS = RAIN.variables['prate'][:]
    RAINS_A = ((RAINS[372:384] + RAINS[384:396] + RAINS[396:408] + RAINS[408:420] + RAINS[420:432] + RAINS[432:444] + RAINS[444:456] + RAINS[456:468] + RAINS[468:480] + RAINS[480:492] + RAINS[492:504] + RAINS[504:516] + RAINS[516:528] + RAINS[528:540] + RAINS[540:552] + RAINS[552:564] + RAINS[564:576] + RAINS[576:588] + RAINS[588:600] + RAINS[600:612] + RAINS[612:624] + RAINS[624:636] + RAINS[636:648] + RAINS[648:660] + RAINS[660:672] + RAINS[672:684] + RAINS[684:696] + RAINS[696:708] + RAINS[708:720] + RAINS[720:732] + RAINS[732:744] + RAINS[744:756] + RAINS[756:768] + RAINS[768:780] + RAINS[780:792] + RAINS[792:804] + RAINS[804:816] + RAINS[816:828] + RAINS[828:840] + RAINS[840:852] + RAINS[852:864])/41 - RAINS[852:864])  * 100000   

def plot_anomaly_temp():
    """
    **Titel: Funktion plotten**    

    *Beschreibung: Plotten der mittleren 2m-Temperaturanomalie im Jahr 2019 im Vergleich zum Mittelwert über 1979-2019 auf einer Weltkarte*
    
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
    airs_new = AIRS_A[:, :, ind]

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
    plt.title('Mittlere 2m-Temperaturanomalie im Jahr 2019 im Vergleich zum Mittelwert über 1979-2019', size=16)

    # show plot and save figure
    plt.savefig('B1_2m-Temperaturanomalie_2019.png')
    plt.show()

def plot_anomaly_rain():
    """
    **Titel: Funktion plotten**    

    *Beschreibung: Plotten der mittleren Niederschlagsanomalie im Jahr 2019 im Vergleich zum Mittelwert über 1979-2019 auf einer Weltkarte*
    
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
    rains_new = RAINS_A[:, :, ind]

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
    plt.title('Mittlere Niederschlagsanomalie im Jahr 2019 im Vergleich zum Mittelwert über 1979-2019', size=16)

    # show plot and save figure
    plt.savefig('B2_Niederschlagsanomalie_2019.png')
    plt.show()

# execute functions
if __name__ == '__main__':
    read_data()
    read_variables()
    plot_anomaly_temp()
    plot_anomaly_rain()
