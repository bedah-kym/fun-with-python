from bs4 import BeautifulSoup as bs

import requests
"""
before you run it change the dir SCRAPER TO your local folder yenye .py file
zako zinaishi ama kwenye this one iko sai
"""


def build(URL):
    try:
        for page in range (1,25): 
            req=requests.get(URL+str(page)+'/')
            soup= bs(req.text,'lxml')
            cities=soup.find_all('div',id= 'results')
            city=cities.find_all('a')
            for city in cities:
                with open (f'SCRAPPER\index{page}.txt','w') as f:
                    f.write(cty.text)
                    print('page',page,'saved')
        print("all done")
        return
    except:
        print('error,action stopped')
        



if __name__ == '__main__' :
    
    build('http://example.python-scraping.com/places/default/index/')
