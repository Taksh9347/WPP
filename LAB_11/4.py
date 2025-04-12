import pandas as pd
import random
party = pd.DataFrame({'days':range(1,11),
                      'John':[random.choice(["Yes","No"]) for _ in range(1,11)],
                      'Judy':[random.choice(["Yes","No"]) for _ in range(1,11)]})
can_party = [i for i in range(10) if party['John'][i]=='Yes' and party['Judy'][i]=='Yes']
days=[]
for i in range(10):
    future_parties = [day - i for day in can_party if day >= i]
    days.append(min(future_parties) if future_parties else None)
party['days_till_party'] = days
print(party)