from request import request
from typing import Optional as Opt
import sys

def _player_info(player_name: str) -> Opt[dict]:
  """ Request against the riot api w/ key.
    
    Parameters:
      endpoint (string): the api endpoint of the request.
      headers (dict): headers sent to the server, apikey is already included.
      retry (bool): indicates if a retry should occur in the event of rate throttling.

    Returns:
      dict of json response or the error code.
  """
  if type(player_name) != str:
    return None

  return request('/lol/summoner/v4/summoners/by-name/%s' % player_name)

def _get_field(player_name: str, field: str):
  if type(field) != str:
    return None

  info = _player_info(player_name)

  if type(info) == dict:
    return info[field]
  else:
    return None

def get_player_id(player_name: str):
  return _get_field(player_name, 'id')

def get_account_id(player_name: str):
  return _get_field(player_name, 'accountId')

def main():
  name = sys.argv[1]
  print(_player_info(name))

if __name__ == "__main__":
  main()