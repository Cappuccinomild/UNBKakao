import requests
from bs4 import BeautifulSoup
'''
악보바다 악보존재여부 판단후 있을경우 1 없으면 0

'''

#악보바다 악보존재여부
def check_score(lists):
    #http://www.akbobada.com/searchAll.html?searchKeyword=노래제목&searchFlag=10&searchSecod=&artistOrderBy=1

    lists = lists.split('\n')

    for i in range(len(lists)):
        lists[i] = lists[i].replace(' ', '+')
        lists[i] = 'http://www.akbobada.com/searchAll.html?searchKeyword='\
        + lists[i] + '&searchFlag=10&searchSecod=&artistOrderBy=1'

    for url in lists:
        search_score(url)


    return 0

def search_score(url):  #검색

        html = get_html(url)

        soup = BeautifulSoup(html, 'html.parser')
            
        #akbo2 > table > tbody > tr:nth-child(1) > td.music > a
        music_area = soup.select( 'td.music > a' )
        
        print(music_area)

        scores = soup.select( 'tr > td.bpmoc' )

        print(scores)

def extract_data():#검색한 코드를 분석
    return 0




def get_html(url): # html 코드를 가져온다
    resp = requests.get(url)
    html = resp.text

    return html


songs = input()

check_score(songs)