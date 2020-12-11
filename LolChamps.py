import pandas as pd
import numpy as np
import sys
from scipy import stats
import matplotlib.pyplot as plt

# its in json format:
# {
#   "name": {...data...},
#   "name": {...data...},
#   ...
# }
# columns = ['type', 'format', 'version', 'data']
# otherColumns = ['id', 'key', 'name', 'title', 'image']

data = pd.read_json(sys.argv[1],  orient='index')
# print(data['data'])
data_format = data['data']
print(data_format)

data_formatting = data_format.loc[:'id':]
print(data_formatting)