import requests as req
import json
import sys
import time

# with open(sys.argv[1], 'r') as champ_file:
#   champions = json.load(champ_file)
print('Getting champion names... '.format(name), end='')

champions_req = req.get('http://ddragon.leagueoflegends.com/cdn/10.24.1/data/en_US/champion.json')

if champions_req.status_code == 200:
  print("OK.")
else:
  print('Failed.\nGot error code:{}'.format(champions_req.status_code))
  exit(61)

champions = champions_req.json()


out_file = open(sys.argv[2], 'w')

out = {}

names = list(champions['data'].keys())
for name in names:
  # each key is a champion name.
  print('Getting {}... '.format(name), end='')

  champ = req.get('http://ddragon.leagueoflegends.com/cdn/10.24.1/data/en_US/champion/{}.json'.format(name))
  if champ.status_code == 200:
    print("OK.")
  else:
    print('Failed.\nGot error code:{}'.format(champ.status_code))
    exit(61)
  out[name] = champ.json()

  #sleep due to api throttler. 100 reqs / 120 seconds
  time.sleep(1.21)

out_file.write(json.dumps(out))