# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 20:05:57 2026

@author: sabin
"""

import requests

def get_songs():
    url='https://itunes.apple.com/search?term=taylor+swift&media=music&entity=album'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None
    
songs = get_songs()
print(songs)
