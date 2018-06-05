#!/usr/lib/python3.4
#-*-coding:utf-8-*-

import requests
from pprint import pprint

r = requests.get('https://api.spotify.com/v1/search?type=artist&q=snoop')
pprint(r.json())