import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd
import csv

df = pd.read_csv(r'/Users/chloejones/VSCode/UKC_Project-main/Deema Mozayen_Logbook.csv')

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

#plt.bar(Disciplines.keys(), Disciplines.values())
#plt.title('Number of Climbs by Discipline')
#plt.show()

Sport_df = df[df['Grade Type'] == 'Sport']
# Count number, specifically of sport climbs, in each country
Sport_England = Sport_df['Country'].value_counts()['England']
Sport_Wales = Sport_df['Country'].value_counts()['Wales']
Sport_Spain = Sport_df['Country'].value_counts()['Spain']
Sport_France = Sport_df['Country'].value_counts()['France']
Sport_Italy = Sport_df['Country'].value_counts()['Italy']
Sport_Greece = Sport_df['Country'].value_counts()['Greece']
Sport_Turkey = Sport_df['Country'].value_counts()['Turkey']

Sport_by_country = {'England': Sport_England, 'Wales': Sport_Wales, 'Spain': Sport_Spain, 'France': Sport_France, 'Greece': Sport_Greece, 'Turkey': Sport_Turkey}

#plt.bar(Sport_by_country.keys(), Sport_by_country.values())
#plt.title('Number of Sport Climbs by Country')
#plt.show()

# Count number of trad climbs, by grade
# Need to work out how to iterate over different string values
# i.e Each HVS has a different tech grade and number of stars and I need to count them all in one category 
Trad_df = df[df['Grade Type'] == 'Trad']
#HVS_5a_3s = Trad_df['Grade'].value_counts()['HVS 5a ***']

#VS = Trad_df['Grade'].apply(lambda x: 'VS' in x).sum() -> This doesn't work as it will count HVS logs as they contain 'VS'
HVS = Trad_df['Grade'].apply(lambda x: 'HVS' in x)
E1 = Trad_df['Grade'].apply(lambda x: 'E1' in x)
E2 = Trad_df['Grade'].apply(lambda x: 'E2' in x)
E3 = Trad_df['Grade'].apply(lambda x: 'E3' in x)
E4 = Trad_df['Grade'].apply(lambda x: 'E4' in x)
E5 = Trad_df['Grade'].apply(lambda x: 'E5' in x)
E6 = Trad_df['Grade'].apply(lambda x: 'E6' in x)


#Trad_climbs = {'HVS': HVS, 'E1': E1, 'E2': E2, 'E3': E3, 'E4': E4, 'E5': E5}

#plt.bar(Trad_climbs.keys(), Trad_climbs.values())
#plt.title('Number of Trad climbs per Grade')
#plt.show()
#print(str(HVS_5a_3s))
#print(str(HVS))

# Next step: grouped bar chart with DNF vs Clean, per grade
# Could also try and do the same but with different tech grades or stars


clean_HVS = HVS[(df['Style'].str.contains('O/S' or 'β' or 'G/U'))].sum()
failed_HVS = HVS[(df['Style'].str.contains('dog' or 'dnf'))].sum()
clean_E1 = E1[(df['Style'].str.contains('O/S' or 'β' or 'G/U'))].sum()
failed_E1 = E1[(df['Style'].str.contains('dog' or 'dnf'))].sum()
clean_E2 = E2[(df['Style'].str.contains('O/S' or 'β' or 'G/U'))].sum()
failed_E2 = E2[(df['Style'].str.contains('dog' or 'dnf'))].sum()
clean_E3 = E3[(df['Style'].str.contains('O/S' or 'β' or 'G/U'))].sum()
failed_E3 = E3[(df['Style'].str.contains('dog' or 'dnf'))].sum()
clean_E4 = E4[(df['Style'].str.contains('O/S' or 'β' or 'G/U'))].sum()
failed_E4 = E4[(df['Style'].str.contains('dog' or 'dnf'))].sum()
clean_E5 = E5[(df['Style'].str.contains('O/S' or 'β' or 'G/U'))].sum()
failed_E5 = E5[(df['Style'].str.contains('dog' or 'dnf'))].sum()
clean_E6 = E6[(df['Style'].str.contains('O/S' or 'β' or 'G/U'))].sum()
failed_E6 = E6[(df['Style'].str.contains('dog' or 'dnf'))].sum()

#clean_sport_ascents = df[(df['Style'].str.contains('O/S' or 'β' or 'G/U' or 'RP')) & (df['Grade Type'] == 'Sport')]
#failed_sport_ascents = df[(df['Style'].str.contains('dog' or 'dnf')) & (df['Grade Type'] == 'Sport')]
#print(failed_sport_ascents)

Trad_grades = ('HVS', 'E1', 'E2', 'E3', 'E4', 'E5', 'E6')
Trad_ascents = {
    'Clean':(clean_HVS, clean_E1, clean_E2, clean_E3, clean_E4, clean_E5,clean_E6),
    'Failed':(failed_HVS, failed_E1, failed_E2, failed_E3, failed_E4, failed_E5, failed_E6)
}

x = np.arange(len(Trad_grades)) 
width = 0.25
multiplier = 0

fig, ax = plt.subplots(layout='constrained')

for Ascent_Style, number in Trad_ascents.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, number, width, label=Ascent_Style)
    ax.bar_label(rects, padding=3)
    multiplier += 1

ax.set_title('Number of Trad climbs by Grade')
ax.set_xticks(x + width, Trad_grades)
ax.legend(loc='upper left', ncols=2)
ax.set_ylim(0,70)

plt.show()

# Sport climbs by grade (clean vs failed)
# Need to turn a list of strings into variables and perform the lamda operator on each


#for grade in Sport_grades:


_6a = Sport_df['Grade'].apply(lambda x: '6a' in x)
_6aplus = Sport_df['Grade'].apply(lambda x: '6a+' in x)
_6b = Sport_df['Grade'].apply(lambda x: '6b' in x)
_6bplus = Sport_df['Grade'].apply(lambda x: '6b+' in x)
_6c = Sport_df['Grade'].apply(lambda x: '6c' in x)
_6cplus = Sport_df['Grade'].apply(lambda x: '6c+' in x)
_7a = Sport_df['Grade'].apply(lambda x: '7a' in x)
_7aplus = Sport_df['Grade'].apply(lambda x: '7a+' in x)
_7b = Sport_df['Grade'].apply(lambda x: '7b' in x)
_7bplus = Sport_df['Grade'].apply(lambda x: '7b+' in x)
_7c = Sport_df['Grade'].apply(lambda x: '7c' in x)
_7cplus = Sport_df['Grade'].apply(lambda x: '7c+' in x)
_8a = Sport_df['Grade'].apply(lambda x: '8a' in x)
_8aplus = Sport_df['Grade'].apply(lambda x: '8a+' in x)


failed_6a = _6a[(df['Style'].str.contains('dog' or 'dnf'))].sum()
clean_6a = _6a[(df['Style'].str.contains('O/S' or 'β' or 'G/U' or 'RP'))].sum()
failed_6aplus = _6aplus[(df['Style'].str.contains('dog' or 'dnf'))].sum()
clean_6aplus = _6aplus[(df['Style'].str.contains('O/S' or 'β' or 'G/U' or 'RP'))].sum()
failed_6b = _6b[(df['Style'].str.contains('dog' or 'dnf'))].sum()
clean_6b = _6b[(df['Style'].str.contains('O/S' or 'β' or 'G/U' or 'RP'))].sum()
failed_6bplus = _6bplus[(df['Style'].str.contains('dog' or 'dnf'))].sum()
clean_6bplus = _6bplus[(df['Style'].str.contains('O/S' or 'β' or 'G/U' or 'RP'))].sum()
failed_6c = _6c[(df['Style'].str.contains('dog' or 'dnf'))].sum()
clean_6c = _6c[(df['Style'].str.contains('O/S' or 'β' or 'G/U' or 'RP'))].sum()
failed_6cplus = _6cplus[(df['Style'].str.contains('dog' or 'dnf'))].sum()
clean_6cplus = _6cplus[(df['Style'].str.contains('O/S' or 'β' or 'G/U' or 'RP'))].sum()
failed_7a = _7a[(df['Style'].str.contains('dog' or 'dnf'))].sum()
clean_7a = _7a[(df['Style'].str.contains('O/S' or 'β' or 'G/U' or 'RP'))].sum()
failed_7aplus = _7aplus[(df['Style'].str.contains('dog' or 'dnf'))].sum()
clean_7aplus = _7aplus[(df['Style'].str.contains('O/S' or 'β' or 'G/U' or 'RP'))].sum()
failed_7b = _7b[(df['Style'].str.contains('dog' or 'dnf'))].sum()
clean_7b = _7b[(df['Style'].str.contains('O/S' or 'β' or 'G/U' or 'RP'))].sum()
failed_7bplus = _7bplus[(df['Style'].str.contains('dog' or 'dnf'))].sum()
clean_7bplus = _7bplus[(df['Style'].str.contains('O/S' or 'β' or 'G/U' or 'RP'))].sum()
failed_7c = _7c[(df['Style'].str.contains('dog' or 'dnf'))].sum()
clean_7c = _7c[(df['Style'].str.contains('O/S' or 'β' or 'G/U' or 'RP'))].sum()
failed_7cplus = _7cplus[(df['Style'].str.contains('dog' or 'dnf'))].sum()
clean_7cplus = _7cplus[(df['Style'].str.contains('O/S' or 'β' or 'G/U' or 'RP'))].sum()
failed_8a = _8a[(df['Style'].str.contains('dog' or 'dnf'))].sum()
clean_8a = _8a[(df['Style'].str.contains('O/S' or 'β' or 'G/U' or 'RP'))].sum()
failed_8aplus = _8aplus[(df['Style'].str.contains('dog' or 'dnf'))].sum()
clean_8aplus = _8aplus[(df['Style'].str.contains('O/S' or 'β' or 'G/U' or 'RP'))].sum()

Sport_grades = ('6a', '6a+', '6b', '6b+', '6c', '6c+', '7a', '7a+', '7b', '7b+', '7c', '7c+', '8a', '8a+')

Sport_ascents = {
    'Clean':(clean_6a, clean_6aplus, clean_6b, clean_6bplus, clean_6c, clean_6cplus, clean_7a, clean_7aplus, clean_7b, clean_7bplus, clean_7c, clean_7cplus, clean_8a, clean_8aplus),
    'Failed':(failed_6a, failed_6aplus, failed_6b, failed_6bplus, failed_6c, failed_6cplus, failed_7a, failed_7aplus, failed_7b, failed_7bplus, failed_7c, failed_7cplus, failed_8a, failed_8aplus)
}

x = np.arange(len(Sport_grades)) 
width = 0.25
multiplier = 0

fig, ax = plt.subplots(layout='constrained')

for Ascent_Style, number in Sport_ascents.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, number, width, label=Ascent_Style)
    ax.bar_label(rects, padding=3)
    multiplier += 1

ax.set_title('Number of Sport climbs by Grade')
ax.set_xticks(x + width, Sport_grades)
ax.legend(loc='upper left', ncols=2)
ax.set_ylim(0,70)

plt.show()