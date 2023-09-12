import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd
import csv

# Source data from UKC spreadsheet, filepath is absolute - specific to Chloe's macbook
df = pd.read_csv(r'/Users/chloejones/VSCode/UKC_Project-main/Deema Mozayen_Logbook.csv')

Trad_df = df[df['Grade Type'] == 'Trad']

# //////    Count number of trad climbs, by grade
# Need to work out how to iterate over different string values
# i.e Each HVS has a different tech grade and number of stars and I need to count them all in one category 
#HVS_5a_3s = Trad_df['Grade'].value_counts()['HVS 5a ***']

#VS = Trad_df['Grade'].apply(lambda x: 'VS' in x).sum() -> This doesn't work as it will count HVS logs as they contain 'VS'
HVS = Trad_df['Grade'].apply(lambda x: 'HVS' in x)
E1 = Trad_df['Grade'].apply(lambda x: 'E1' in x)
E2 = Trad_df['Grade'].apply(lambda x: 'E2' in x)
E3 = Trad_df['Grade'].apply(lambda x: 'E3' in x)
E4 = Trad_df['Grade'].apply(lambda x: 'E4' in x)
E5 = Trad_df['Grade'].apply(lambda x: 'E5' in x)
E6 = Trad_df['Grade'].apply(lambda x: 'E6' in x)

Trad_climbs = {'HVS': HVS, 'E1': E1, 'E2': E2, 'E3': E3, 'E4': E4, 'E5': E5}

#plt.bar(Trad_climbs.keys(), Trad_climbs.values())
#plt.title('Number of Trad climbs per Grade')
#plt.show()


# //////    Next step: grouped bar chart with Clean vs Failed Ascents, per grade
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

#plt.show()