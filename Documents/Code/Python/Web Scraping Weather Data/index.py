# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 01:35:07 2022

@author: Davey
"""

from requests_html import HTMLSession

session = HTMLSession()

query = 'london'
url = f'https://www.google.com/search?q=weather+{query}'

response = session.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.62'})

print(response.html.find('title', first = True).text) # output: weather london - Google Search

temperature = response.html.find('span#wob_tm', first = True).text

unit = response.html.find('div.vk_bk.wob-unit span.wob_t', first = True).text

desc = response.html.find('#wob_dc', first = True).text

print(f'{query} is {temperature} {unit} {desc}')