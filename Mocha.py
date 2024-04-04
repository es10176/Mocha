# importing modules

import time
from datetime import datetime
from plyer import notification
import webbrowser
from bs4 import BeautifulSoup
import requests
import random

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

# copilot code

end_tags_coding = [': GeeksforGeeks', ': Stack Overflow', ': W3 Schools']

notification.notify(
    title = 'Mocha',
    message = 'Welcome to your web scraping copilot',
    app_icon = None,
    timeout = 3,
)


Task = input('\n\nSearch the web or type a URL\n\n: ')

URL = ('https://www.google.com/search?q= ' + Task + '&oq= ' + Task + '&aqs=chrome..69i57.30j0j7&sourceid=chrome&ie=UTF-8' + '')
URL2 = ('https://www.bing.com/search?q= ' + Task + '&qs=n&form=QBRE&sp=-1&lq=0&pq= ' + Task + '&sc=11-17&sk=&cvid=68CFBFF6CEB74EC38F8C1EBEDA82F639&ghsh=0&ghacc=0&ghpl=&adlt=strict&toWww=1&redig=82384E32C28D4032B8627498876A93E4')


if Task.lower().startswith('https'):
    URL3 = str(Task)
    Extract_Option = input('\n\nWhat would you like to do with this link?:\n\n[1] Extract links\n[2] Extract text\n[3] check connectivity status\n\n: ')

    if Extract_Option == '1':
        print('\nScraping content...')
        time.sleep(2)

        r = requests.get(URL3) 
    
        soup = BeautifulSoup(r.content, 'html.parser') 
  
        for link in soup.find_all('a'): 
            print(link.get('href'))

        spit = input('')

    elif Extract_Option == '2':
        page = requests.get(URL3)

        print('Scraping content...')
        time.sleep(2)


        soup = BeautifulSoup(page.content, 'html.parser')

        lines = soup.find_all('p')

        for line in lines:
            print(line.text)

        spit2 = input('') 

    elif Extract_Option == '3':
        response_code = requests.get(URL3)

        if response_code.status_code == 200:
            print("\n\nConnectivity Status: Online...")
            input2 = input('')

        else:
            print(f'Connectivity Status: Offline')
            input1 = input('')
       

else:
    print('\nSearching the web...')
    time.sleep(2)
    task_formed = Task + random.choice(end_tags_coding)
    webbrowser.open('https://www.google.com/search?q= ' + task_formed + '&oq= ' + task_formed + '&aqs=chrome..69i57.30j0j7&sourceid=chrome&ie=UTF-8' + random.choice(end_tags_coding) + '')
