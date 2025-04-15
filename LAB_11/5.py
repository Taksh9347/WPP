import pandas as pd
import itertools
concert = pd.DataFrame({
    'artist': ['A', 'C', 'B', 'A', 'B', 'C', 'A'],
    'Venue': ['v1', 'v2', 'v3', 'v1', 'v2', 'v3', 'v2'],
    'Year-Month': ['2020-03', '2021-04', '2023-05', '2020-03', '2023-05', '2020-03', '2020-03']
})
arti = pd.Series(sorted(concert['artist'].unique()), name='artist')
ven = pd.Series(sorted(concert['Venue'].unique()), name='Venue')
wide = pd.pivot_table(concert,
                      columns=['artist', 'Venue'],
                      index='Year-Month',
                      aggfunc='size',
                      fill_value=0)
# Create all combinations
all_comb = list(itertools.product(arti, ven)) # cross product 
for a, v in all_comb:
    if (a, v) not in wide.columns:
        wide[(a, v)] = 0  # if a col is missing then make it zero
wide = wide.reindex(sorted(wide.columns), axis=1) # give proper index after editing wide.columns
wide.columns = [f'({a},{v})' for a, v in wide.columns] # convert ('A','v1') -> (A,v1)
print(wide)