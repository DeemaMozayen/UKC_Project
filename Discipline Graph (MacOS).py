import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd
import csv

# Source data from UKC spreadsheet, filepath is absolute - specific to Chloe's macbook
df = pd.read_csv(r'/Users/chloejones/VSCode/UKC_Project-main/Deema Mozayen_Logbook.csv')

# //////    Count number of climbs by discipline
n_trad = df['Grade Type'].value_counts()["Trad"]
n_sport = df['Grade Type'].value_counts()["Sport"]
n_bouldering = df['Grade Type'].value_counts()["Bouldering"]
n_alpine = df['Grade Type'].value_counts()["Alpine"]
n_winter = df['Grade Type'].value_counts()["Winter"]
n_scrambling = df['Grade Type'].value_counts()["Scrambling"]
n_mixed = df['Grade Type'].value_counts()["Mixed"]
n_special = df['Grade Type'].value_counts()["Special"]

Disciplines = {'Trad': n_trad, 'Sport': n_sport, 'Bouldering': n_bouldering, 'Alpine': n_alpine, 'Winter': n_winter, 'Scrambling': n_scrambling, 'Mixed': n_mixed, 'Special': n_special}

#plt.bar(Disciplines.keys(), Disciplines.values())
#plt.title('Number of Climbs by Discipline')
#plt.show()