import requests
import environ

env = environ.Env()

class OMDbApiClient:
  def __init__(self):
    self.api_key = env('OMDBAPI_KEY')
    self.base_url = 'http://www.omdbapi.com/'

  def search_movie_by_name(self, name):
    url = f'{self.base_url}?apikey={self.api_key}&t={name}'
    response = requests.get(url)
    if response.status_code == 200:
      return response.json()
    else:
      return None
    
