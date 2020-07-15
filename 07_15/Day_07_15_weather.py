import requests
import re

url = ''
received = requests.get(url)
print(received)
print(received.text)