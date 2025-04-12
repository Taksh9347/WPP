import pandas as pd
import random
asking_price = pd.Series(random.randint(100,1000) for _ in range(10))
fair_price = pd.Series(random.randint(100,1000) for _ in range(10))
good_deals = []
for i in range(10):
    if asking_price[i] < fair_price[i]:
        good_deals.append(i)
good_deal = ['Yes' if i in good_deals else 'No' for i in range(10)]
print(pd.DataFrame({'asking_price':asking_price,'fair_price':fair_price,'Deal??':good_deal}))
print(good_deals)