import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd
import csv

# Source data from UKC spreadsheet, filepath is absolute - specific to Chloe's macbook
df = pd.read_csv(r'/Users/chloejones/VSCode/UKC_Project-main/Deema Mozayen_Logbook.csv')

# //////    Count number of sport climbs per country

Sport_df = df[df['Grade Type'] == 'Sport']

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


# //////    Sport climbs by grade (clean vs failed)

Sport_grades = ('6a', '6a+', '6b', '6b+', '6c', '6c+', '7a', '7a+', '7b', '7b+', '7c', '7c+', '8a', '8a+')
# Would be great if the block of code below could instead be achieved with a for loop, iterating on the list above - but I don't know how to do this so that it generates variables

# Extract sport climbs at each grade 
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

# Of the list of sport climbs at each grade, determine which are clean or failed
# eg. failed_6bplus = _6bplus[(df['Style'].str.contains(('dog' or 'dnf') and not ('O/S' or 'β' or 'G/U' or 'RP')))].sum() - why doesn't this work?

failed_6a = _6a[(df['Style'].str.contains('dog' or 'dnf'))].sum()
clean_6a = _6a[(df['Style'].str.contains('O/S' or 'β' or 'G/U' or 'RP' or (('G/U' or 'RP') and ('dog' or 'dnf'))))].sum()
failed_6aplus = _6aplus[(df['Style'].str.contains('dog' or 'dnf'))].sum()
clean_6aplus = _6aplus[(df['Style'].str.contains('O/S' or 'β' or 'G/U' or 'RP' or (('G/U' or 'RP') and ('dog' or 'dnf'))))].sum()
failed_6b = _6b[(df['Style'].str.contains('dog' or 'dnf'))].sum()
clean_6b = _6b[(df['Style'].str.contains('O/S' or 'β' or 'G/U' or 'RP' or (('G/U' or 'RP') and ('dog' or 'dnf'))))].sum()
failed_6bplus = _6bplus[(df['Style'].str.contains('dog' or 'dnf'))].sum()
clean_6bplus = _6bplus[(df['Style'].str.contains('O/S' or 'β' or 'G/U' or 'RP' or (('G/U' or 'RP') and ('dog' or 'dnf'))))].sum()
failed_6c = _6c[(df['Style'].str.contains('dog' or 'dnf'))].sum()
clean_6c = _6c[(df['Style'].str.contains('O/S' or 'β' or 'G/U' or 'RP' or (('G/U' or 'RP') and ('dog' or 'dnf'))))].sum()
failed_6cplus = _6cplus[(df['Style'].str.contains('dog' or 'dnf'))].sum()
clean_6cplus = _6cplus[(df['Style'].str.contains('O/S' or 'β' or 'G/U' or 'RP' or (('G/U' or 'RP') and ('dog' or 'dnf'))))].sum()
failed_7a = _7a[(df['Style'].str.contains('dog' or 'dnf'))].sum()
clean_7a = _7a[(df['Style'].str.contains('O/S' or 'β' or 'G/U' or 'RP' or (('G/U' or 'RP') and ('dog' or 'dnf'))))].sum()
failed_7aplus = _7aplus[(df['Style'].str.contains('dog' or 'dnf'))].sum()
clean_7aplus = _7aplus[(df['Style'].str.contains('O/S' or 'β' or 'G/U' or 'RP' or (('G/U' or 'RP') and ('dog' or 'dnf'))))].sum()
failed_7b = _7b[(df['Style'].str.contains('dog' or 'dnf'))].sum()
clean_7b = _7b[(df['Style'].str.contains('O/S' or 'β' or 'G/U' or 'RP' or (('G/U' or 'RP') and ('dog' or 'dnf'))))].sum()
failed_7bplus = _7bplus[(df['Style'].str.contains('dog' or 'dnf'))].sum()
clean_7bplus = _7bplus[(df['Style'].str.contains('O/S' or 'β' or 'G/U' or 'RP' or (('G/U' or 'RP') and ('dog' or 'dnf'))))].sum()
failed_7c = _7c[(df['Style'].str.contains('dog' or 'dnf'))].sum()
clean_7c = _7c[(df['Style'].str.contains('O/S' or 'β' or 'G/U' or 'RP' or (('G/U' or 'RP') and ('dog' or 'dnf'))))].sum()
failed_7cplus = _7cplus[(df['Style'].str.contains('dog' or 'dnf'))].sum()
clean_7cplus = _7cplus[(df['Style'].str.contains('O/S' or 'β' or 'G/U' or 'RP' or (('G/U' or 'RP') and ('dog' or 'dnf'))))].sum()
failed_8a = _8a[(df['Style'].str.contains('dog' or 'dnf'))].sum()
clean_8a = _8a[(df['Style'].str.contains('O/S' or 'β' or 'G/U' or 'RP' or (('G/U' or 'RP') and ('dog' or 'dnf'))))].sum()
failed_8aplus = _8aplus[(df['Style'].str.contains('dog' or 'dnf'))].sum()
clean_8aplus = _8aplus[(df['Style'].str.contains('O/S' or 'β' or 'G/U' or 'RP' or (('G/U' or 'RP') and ('dog' or 'dnf'))))].sum()

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

#plt.show()


# Display the duplicate rows - these are climbs where I have logged as dog, then proceeded to make a separate log of the clean ascent (RP)
duplicates = Sport_df[df.duplicated(subset='Climb name')]
print("Duplicate Rows:")
print(duplicates)
