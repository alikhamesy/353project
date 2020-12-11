import sys
import json
import pandas as pd
import numpy as np
from releases import releases

in_file = pd.read_json(sys.argv[1], orient='index')

def parse(row):
  return pd.Series({
    'champion': row['id'],
    'date': releases[row['id']],
    'passive': row['passive']['description'],
    'q': row['spells'][0]['description'],
    'w': row['spells'][1]['description'],
    'e': row['spells'][2]['description'],
    'r': row['spells'][3]['description'],
  })

champions = pd.json_normalize(in_file['data'], max_level=0).apply(parse, axis=1)

champions['q'] = champions['q'].str.split()
print(champions['q'])
# print(champions.explode('q').groupby(by='champion').count())

