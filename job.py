import requests
import os

def callUpdateApi() :
  print('Hit the url .........................')
  url = os.getenv('URL')
  response = requests.post(url)
  print(response)
