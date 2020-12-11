from request import request
from typing import Optional as Opt
import sys
from players import get_account_id
import datetime as dt

QUEUE_IDS = {
  'RANKED_SOLO': 420,
  'SR_BLIND': 430,
  'SR_DRAFT': 400,
  'SR_BOTS_INTRO': 830,
  'SR_BOTS_EASY': 840,
  'SR_BOTS_HARD': 850,
  'ARAM': 450,
  'ONE_FOR_ALL': 1020,
  'URF': 900,
  'ALL': None
}

PATCHES = {
  '10.01': '08-01-2020',
  '10.02': '23-01-2020',
  '10.03': '02-05-2020',
  '10.04': '02-20-2020',
  '10.05': '03-04-2020',
  '10.06': '03-15-2020',
  '10.07': '04-01-2020',
  '10.08': '04-15-2020',
  '10.09': '04-29-2020',
  '10.10': '05-13-2020',
  '10.11': '05-28-2020',
  '10.12': '06-10-2020',
  '10.13': '06-24-2020',
  '10.14': '07-08-2020',
  '10.15': '07-22-2020',
  '10.16': '08-05-2020',
  '10.17': '08-19-2020',
  '10.18': '09-02-2020',
  '10.19': '09-16-2020',
  '10.20': '09-30-2020',
  '10.21': '10-14-2020',
  '10.22': '10-28-2020',
  '10.23': '11-11-2020',
  '10.24': '11-24-2020',
  '10.25': '12-09-2020',
}

def page_matches(player_name: Opt[str] = None, player_id: Opt[str] = None, queue_id: int = None, timestamp: int = None):
  if player_id is None:
    player_id = get_account_id(player_name)
    if player_id is None:
      return None

  endpoint = '/lol/match/v4/matchlists/by-account/%s?' % player_id
  if queue_id is not None:
    endpoint += 'queue=%s&' % str(queue_id)

  if timestamp is not None:
    endpoint += 'beginTime=%d&' % timestamp

  paged = []
  index = 0
  data = {'matches': [], 'endIndex': 1, 'startIndex': 0}
  while(data['endIndex'] - data['startIndex'] > 0):
    request_index = '%sbeginIndex=%d&' % (endpoint, index)
    data = request(request_index)

    if type(data) != dict:
      data = {'matches': [], 'endIndex': 0, 'startIndex': 0}

    paged.extend(data['matches'])
    index = data['endIndex']

  return paged


def get_matches(player_name: Opt[str] = None, player_id: Opt[str] = None, queue_id: int = None, age: Opt[str] = None):
  time = None
  if age is not None:
    try:
      time = dt.datetime.strptime(age, '%d-%m-%Y').timestamp() * 1000
    except ValueError as e:
      print('expected time format is dd-mm-yyyy.')
      raise e

  return page_matches(player_name, player_id, queue_id, time)


def main():
  player = sys.argv[1]

  queue_type = None
  if len(sys.argv) >= 3:
    if sys.argv[2] in QUEUE_IDS:
      queue_type = QUEUE_IDS[sys.argv[2]]
    else:
      queue_type = sys.argv[2]

  t = None
  if len(sys.argv) >= 4:
    t = sys.argv[3]
    if t in PATCHES:
      t = PATCHES[t]

  matches = get_matches(player_name=player, queue_id=queue_type, age=t)

  print('user %s has played %d matches.' % (player, len(matches)))


if __name__ == '__main__':
  main()

