import pandas as pd
s = pd.Series(['X','Y','T','Aaba','Baca','CABA',None,'bird','horse','dog'])
lower = s.str.lower()
upper = s.str.upper()
len_of_str = s.str.len()
res = pd.DataFrame({'Original':s ,'Lower':lower,'Upper':upper,"Len_of_str":len_of_str})
print(res)