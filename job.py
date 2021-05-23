import requests
import os

def callUpdateApi() :
  url = os.getenv('URL')
  response = requests.post(url)
  print(response)
