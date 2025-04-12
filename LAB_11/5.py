import pandas as pd
concert = pd.DataFrame({'artist':['A','C','B','A','B','C','A'],
                        'Venue':['v1','v2','v3','v1','v2','v3','v2'],
                        'Year-Month':['2020-03','2021-04','2023-05','2023-07','2023-05','2020-03','2020-03']})
# get unique series of artists and venues
arti = pd.Series(sorted(list(set(concert['artist']))),name='artist')
ven = pd.Series(sorted(list(set(concert['Venue']))),name='Venue')
# counting the number of concerts for the pair (artist,venue)
counts = concert.groupby(['artist','Venue','Year-Month']).size().reset_index(name='Counts')
# create a wide table for output
wide = pd.pivot_table(concert,
                      columns=['artist','Venue'],
                      index='Year-Month',
                      aggfunc='size',
                      fill_value=0)
# Flatten Column multi-index -> i.e (artist,value) pairs
wide.columns = [f'({a},{v})' for a, v in wide.columns]
print(wide)