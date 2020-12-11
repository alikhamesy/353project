import sys
import json
import pandas as pd
import numpy as np
from releases import releases
import matplotlib.pyplot as plt
from scipy.stats import linregress

in_file = pd.read_json(sys.argv[1], orient='index')
out_file = sys.argv[2]

def parse(row):
  return pd.Series({
    'name': row['id'],
    'date': releases[row['id']]['date'],
    'passive': releases[row['id']]['passive'],
    # 'passive': row['passive']['description'],
    'q': row['spells'][0]['tooltip'],
    'w': row['spells'][1]['tooltip'],
    'e': row['spells'][2]['tooltip'],
    'r': row['spells'][3]['tooltip'],
  })

champions = pd.json_normalize(in_file['data'], max_level=0).apply(parse, axis=1)

length = lambda arr: len(arr)

champions['q'] = champions['q'].str.split().apply(length)
champions['w'] = champions['w'].str.split().apply(length)
champions['e'] = champions['e'].str.split().apply(length)
champions['r'] = champions['r'].str.split().apply(length)
champions['passive'] = champions['passive'].str.split().apply(length)
champions['date'] = pd.to_datetime(champions['date'])

champions['total'] = champions['q'] + champions['w'] + champions['e'] + champions['r'] + champions['passive']

champions['date_float'] = champions['date'].apply(lambda d : d.timestamp())

sorted_champions = champions.sort_values(by=['total', 'date', 'name'], ascending=False)

sorted_champions.to_csv(out_file)

fit = linregress(champions['date_float'], champions['total'].values)
print(fit.slope, fit.intercept, fit.pvalue)


plt.figure(figsize=(12, 4))
plt.plot(champions['date'], champions['total'], 'b.', alpha=0.5)
plt.plot(champions['date'], champions['date_float']*fit.slope + fit.intercept, "r-", linewidth=3)
plt.savefig('champions.png')
