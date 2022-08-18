from bs4 import BeautifulSoup as bs

import requests
"""
before you run it change the dir SCRAPER TO your local folder yenye .py file
zako zinaishi ama kwenye this one iko sai
"""


def build(WORD,**args):
        URL=('http://example.python-scraping.com/places/default/index/')
        for page in range (1): 
            req=requests.get(URL+str(page)+'/')
            soup= bs(req.text,'lxml')
            cities=soup.find('div',id='results')
            details=cities.find_all('a')
            detlist=[]
            
            for det in details:
                    detlist.append(det.text)
            print(detlist)
            if WORD in detlist:
                    print(detlist)
                    with open (f'SCRAPPER\index{WORD}.txt','w') as f:
                            f.write(WORD,f'in page{page}')
                            print('page',page,'saved')
            elif WORD not in detlist:
                    print('bado')

        
        print("all done")
        return 
    


if __name__ == '__main__' :
    
    build('Albania')
