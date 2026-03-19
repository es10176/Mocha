# importing modules

import time
from bs4 import BeautifulSoup
import requests
import random

while True:
    Task = input('\n\nEnter a URL: ')


    if Task.lower().startswith('https'):
        URL3 = str(Task)
        Extract_Option = input('\n\nWhat would you like to do with this link?:\n\n[1] Extract links\n[2] Extract text\n\n: ')

        if Extract_Option == '1':
            print('\nScraping content...\n')
            time.sleep(2)

            r = requests.get(URL3) 
    
            soup = BeautifulSoup(r.content, 'html.parser') 
  
            for link in soup.find_all('a'): 
                print(link.get('href'))


        elif Extract_Option == '2':
            page = requests.get(URL3)

            print('Scraping content...\n')
            time.sleep(2)


            soup = BeautifulSoup(page.content, 'html.parser')

            lines = soup.find_all('p')

            for line in lines:
                print(line.text)
