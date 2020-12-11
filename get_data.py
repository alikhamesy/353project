import requests as req
import json
import sys
import time

if len(sys.argv) < 3:
  print('missing arguments. format: python3 get_data.py [patch] [output file]')
  exit()

out_file = open(sys.argv[2], 'w')

base = 'http://ddragon.leagueoflegends.com/cdn/%s.1/data/en_US/' % sys.argv[1]

print('Getting champion names... ', end='')

champions_req = req.get(base + 'champion.json')

if champions_req.status_code == 200:
  print("OK.")
else:
  print('Failed.\nGot error code:{}'.format(champions_req.status_code))
  exit(61)

champions = champions_req.json()

out = {}

names = list(champions['data'].keys())
for name in names:
  # each key is a champion name.
  print('Getting {}... '.format(name), end='', flush=True)

  #sleep due to api throttler. 100 reqs / 120 seconds
  time.sleep(1.21)

  champ = req.get('%schampion/%s.json' % (base, name))

  if champ.status_code == 200:
    print("OK.")
  else:
    print('Failed.\nGot error code:{}'.format(champ.status_code))
    exit(61)

  out[name] = {'data': champ.json()['data'][name]}

out_file.write(json.dumps(out))