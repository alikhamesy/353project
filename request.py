import requests
from typing import Optional as Opt
import json
import sys
import time
from secret import key

limit = 120 / 100 # 100 requests per 120 seconds

last_req = 0
def request(endpoint: str, headers: dict = {}, retry: bool = True) -> Opt[dict]:
  """ Request against the riot api w/ key.
    
    Parameters:
      endpoint: the api endpoint of the request.
      headers: headers sent to the server, apikey is already included.
      retry: indicates if a retry should occur in the event of rate throttling.

    Returns:
      dict of json response or the error code.
  """
  global last_req

  if type(endpoint) != str or type(headers) != dict or type(retry) != bool:
    return None

  print('[REQUEST] [retry=%d] \'%s\'' % (not retry, endpoint))

  headers['X-Riot-Token'] = key
  url = 'https://na1.api.riotgames.com%s' % endpoint

  now = time.time()
  delta = limit - (now - last_req)
  if delta > 0:
    time.sleep(delta)

  last_req = time.time()
  req = requests.get(url, headers=headers)

  if req.status_code == 200:
    return req.json()
  elif req.status_code == 429 and retry:
    # if rate limited, retry in 5 seconds
    time.sleep(5)
    request(endpoint, headers, False)
  else:
    return req.status_code


def request_field(endpoint: str, field: str, headers: dict = {}, retry: bool = True) -> any:
  """ Request against the riot api w/ key.

    Parameters:
      endpoint: the api endpoint of the request.
      field: the field to retrive from the json response
      headers: headers sent to the server, apikey is already included.
      retry: indicates if a retry should occur in the event of rate throttling.

    Returns:
      the value of the json response with key = field or None.
  """
  if type(field) != str:
    return None

  data = request(endpoint, headers, retry)
  return data[field] if type(data) == dict else data