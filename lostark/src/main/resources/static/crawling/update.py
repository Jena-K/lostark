import requests
from bs4 import BeautifulSoup



    
url = "https://lostark.game.onstove.com/News/Notice/List?page=1&searchtype=2&searchtext=%EC%97%85%EB%8D%B0%EC%9D%B4%ED%8A%B8%20%EB%82%B4%EC%97%AD&noticetype=all"

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    titlelist = []
    linklist = []
    #모든 제목 찾기
    div = soup.find('div','list list--default')
    ul = div.find_all('ul')[1]
    '''
    for i in txt:
        print(i)
        title = str(i.text)
        #제목 중 업데이트 내역 안내만 검색
        if '업데이트 내역 안내' in title:
            if len(titlelist)<5:
                titlelist.append(title)
    '''
    
    div = soup.find('div','list list--default')
    ul = div.find_all('ul')[1]
    #ul 목록 중 'a' 태그 찾기
    for link in ul.find_all('a'):
        #a 태그의 href 검색
        if 'href' in link.attrs:
            if len(linklist)<5:
                linklist.append('lostark.game.onstove.com'+link.attrs['href'])

else:
    print(response.status_code)


