import matplotlib.pyplot as plt 
import pandas as pd
import csv

df = pd.read_csv(r'C:\Users\SMoza\Downloads\Deema Mozayen_Logbook.csv')

# df.loc extracts all rows from the table based on another specified column value 
Trad = df.loc[df['Grade Type'] == 'Trad']
Sport = df.loc[df['Grade Type'] == 'Sport']
Bouldering = df.loc[df['Grade Type'] == 'Bouldering']
Alpine = df.loc[df['Grade Type'] == 'Alpine']
Winter = df.loc[df['Grade Type'] == 'Winter']
Scrambling = df.loc[df['Grade Type'] == 'Scrambling']
Mixed = df.loc[df['Grade Type'] == 'Mixed']
Special = df.loc[df['Grade Type'] == 'Special']

# Count number of climbs by discipline
n_trad = df['Grade Type'].value_counts()["Trad"]
n_sport = df['Grade Type'].value_counts()["Sport"]
n_bouldering = df['Grade Type'].value_counts()["Bouldering"]
n_alpine = df['Grade Type'].value_counts()["Alpine"]
n_winter = df['Grade Type'].value_counts()["Winter"]
n_scrambling = df['Grade Type'].value_counts()["Scrambling"]
n_mixed = df['Grade Type'].value_counts()["Mixed"]
n_special = df['Grade Type'].value_counts()["Special"]

Disciplines = {'Trad': n_trad, 'Sport': n_sport, 'Bouldering': n_bouldering, 'Alpine': n_alpine, 'Winter': n_winter, 'Scrambling': n_scrambling, 'Mixed': n_mixed, 'Special': n_special}

plt.bar(Disciplines.keys(), Disciplines.values())
plt.title('Number of Climbs by Discipline')
plt.show()

# Count number, specifically of sport climbs, in each country
Sport_England = df[df['Grade Type'] == 'Sport']['Country'].value_counts()['England']
Sport_Wales = df[df['Grade Type'] == 'Sport']['Country'].value_counts()['Wales']
Sport_Spain = df[df['Grade Type'] == 'Sport']['Country'].value_counts()['Spain']
Sport_France = df[df['Grade Type'] == 'Sport']['Country'].value_counts()['France']
Sport_Italy = df[df['Grade Type'] == 'Sport']['Country'].value_counts()['Italy']
Sport_Greece = df[df['Grade Type'] == 'Sport']['Country'].value_counts()['Greece']
Sport_Turkey = df[df['Grade Type'] == 'Sport']['Country'].value_counts()['Turkey']

Sport_by_country = {'England': Sport_England, 'Wales': Sport_Wales, 'Spain': Sport_Spain, 'France': Sport_France, 'Greece': Sport_Greece, 'Turkey': Sport_Turkey}

plt.bar(Sport_by_country.keys(), Sport_by_country.values())
plt.title('Number of Sport Climbs by Country')
plt.show()
