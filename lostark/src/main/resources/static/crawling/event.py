import requests
from bs4 import BeautifulSoup


    
url = "https://lostark.game.onstove.com/News/Event/Now"

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    titlelist = []
    linklist = []
    #모든 제목 찾기
    txt = (soup.find_all('span', 'list__title'))
    for i in txt:
        title = str(i.text)
        #제목 중 업데이트 내역 안내만 검색
        titlelist.append(title)

    ul = soup.find('div','list list--event').find('ul')
    #ul 목록 중 'a' 태그 찾기
    for link in ul.find_all('a'):
        #a 태그의 href 검색
        if 'href' in link.attrs:
            if len(linklist)<5:
                linklist.append('lostark.game.onstove.com'+link.attrs['href'])
    print(linklist)
    

else:
    print(response.status_code)

'''
<ul>
    <li class="">
        <a href="/Promotion/Package/210915">
            <div class="list__thumb"><img src="https://cdn-lostark.game.onstove.com/uploadfiles/banner/1b88ad1a7e1d4d2d93b9e9408fef6ffe.jpg" alt="글라이드 앤 네온 패키지"></div>
            <div class="list__subject" aria-label="제목">
                <span class="list__title">글라이드 앤 네온 패키지</span>
            </div>
            <div class="list__term"><strong>이벤트 기간</strong> : 2021.09.15 06:00 - 10.13 06:00</div>
            <div class="list__status">
                    <span class="list__status--ongoing">진행</span>
            </div>
        </a>
    </li>
    <li class="">
        <a href="/Promotion/Mission/210915">
            <div class="list__thumb"><img src="https://cdn-lostark.game.onstove.com/uploadfiles/banner/d3f793801efa4762a3730f48b0959b67.jpg" alt="가을 안부 편지"></div>
            <div class="list__subject" aria-label="제목">
                <span class="list__title">가을 안부 편지</span>
            </div>
            <div class="list__term"><strong>이벤트 기간</strong> : 2021.09.15 06:00 - 10.13 06:00</div>
                <div class="list__receive"><strong>보상 수령 기간</strong> : 2021.09.15 06:00 ~ 10.20 06:00</div>
            <div class="list__status">
                    <span class="list__status--ongoing">진행</span>
            </div>
        </a>
    </li>
    <li class="">
        <a href="/Promotion/InGame/210929">
            <div class="list__thumb"><img src="https://cdn-lostark.game.onstove.com/uploadfiles/banner/ea4abaa1a6b54b0b9979cc9722632d0c.jpg" alt="돌아온 모코모코 야시장"></div>
            <div class="list__subject" aria-label="제목">
                <span class="list__title">돌아온 모코모코 야시장</span>
                    <span class="icon icon--new">새 글</span>
            </div>
            <div class="list__term"><strong>이벤트 기간</strong> : 2021.09.29 06:00 - 10.27 06:00</div>
            <div class="list__status">
                    <span class="list__status--ongoing">진행</span>
            </div>
        </a>
    </li>
    <li class="">
        <a href="/News/Notice/Views/1661">
            <div class="list__thumb"><img src="https://cdn-lostark.game.onstove.com/uploadfiles/banner/060014b541b54c9c80f37fa4a576db73.jpg" alt="음성 커스터마이징 기념 이벤트"></div>
            <div class="list__subject" aria-label="제목">
                <span class="list__title">음성 커스터마이징 기념 이벤트</span>
                    <span class="icon icon--new">새 글</span>
            </div>
            <div class="list__term"><strong>이벤트 기간</strong> : 2021.09.29 06:00 - 10.27 06:00</div>
            <div class="list__status">
                    <span class="list__status--ongoing">진행</span>
            </div>
        </a>
    </li>
    <li class="">
        <a href="/Promotion/Collaboration/210929">
            <div class="list__thumb"><img src="https://cdn-lostark.game.onstove.com/uploadfiles/banner/c25f9164fde84cc58bf829b871a5b2e4.jpg" alt="매운맛의 지배자, 게이머즈컵 소서리스 등장!"></div>
            <div class="list__subject" aria-label="제목">
                <span class="list__title">매운맛의 지배자, 게이머즈컵 소서리스 등장!</span>
                    <span class="icon icon--new">새 글</span>
            </div>
            <div class="list__term"><strong>이벤트 기간</strong> : 2021.09.29 06:00 - 12.31 23:59</div>
            <div class="list__status">
                    <span class="list__status--ongoing">진행</span>
            </div>
        </a>
    </li>
    <li class="">
        <a href="/News/Notice/Views/1663">
            <div class="list__thumb"><img src="https://cdn-lostark.game.onstove.com/uploadfiles/banner/2ffa55971d1748418dbf40287b3a45e6.jpg" alt="개천절 &amp; 한글날 핫타임 이벤트"></div>
            <div class="list__subject" aria-label="제목">
                <span class="list__title">개천절 &amp; 한글날 핫타임 이벤트</span>
                    <span class="icon icon--new">새 글</span>
            </div>
            <div class="list__term"><strong>이벤트 기간</strong> : 2021.10.02 06:00 - 10.12 05:58</div>
            <div class="list__status">
                    <span class="list__status--before">예정</span>
            </div>
        </a>
    </li>
</ul>
'''