import sys
import json
import pandas as pd

in_file = pd.read_json(sys.argv[1], orient='index')
# out_file = open(sys.argv[2], 'w')

# champions = json.loads(in_file)

print(in_file['data'][in_file.index.values])