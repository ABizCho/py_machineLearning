

########### Data collection with python ###################
########### 파이썬 웹 스크래핑 튜토리얼 #####################

''''''
# 1. Basic 
''''''

'''
1.1 urllib 패키지를 사용하여 http 요청 : 인터넷 리소스 가져오기

ssl : secure socket layer : 보안 소켓 계층
        : 웹사이트와 브라우저 사이에 전송되는 데이터를 암호화하여 인터넷 보안을 유지하는데 사용된다

urlopen() : urllib.request에 포함되어 있는 함수 : (필수 인자 : 열고자 하는 url 문자열)
urlopen().read([nbytes]) : nbyte의 데이터를 바이트 문자열로 읽음​
urlopen().readline() : 한 줄의 텍스트를 바이트 문자열로 읽음
urlopen().info() : URL에 연관된 메타 정보를 담은 매핑 객체를 반환​
urlopen().getcode() : HTTP 응답 코드를 정수로 반환( 200, 404 )
urlopen().close() : 연결을 닫는다
'''
# import ssl # ssl 사이트를 다루기 위해서 ssl 의존성 추가
# from urllib.request import urlopen #해당 모듈은 url을 가져오기 위해 사용된다.

# ssl._create_default_default_https_context = ssl._create_unverified_context  # ssl 전달로 의존성 추가

# html = urlopen('http://pythonscraping.com/pages/page1.html') # html 받아오기
# print(html.read()) #받아온 html을 read 메서드로 읽는다.
# html.close()


'''
'''
# import ssl
# ssl._create_default_default_https_context = ssl._create_unverified_context
# from urllib.request import urlopen
# from bs4 import BeautifulSoup

# html = urlopen('http://pythonscraping.com/pages/page1.html') # html 받아오기
# bs = BeautifulSoup(html.read(), 'html.parser') #BS모듈을 사용하여 ( html 소스 => Soup 객체 ) 로 변환
# print(bs.h1) # bs객체의 첫번째 h1태그 및 컨텐츠를 반환


'''
    * 예외처리 : 크롤링할 때 예외처리를 빈틈없이 파악해 놓는 것이 좋은 크롤러를 만드는 비결
        - HTTPError : 페이지를 찾을 수 없거나, URL 해석에서 에러가 생긴 경우 ( 서버 접속 이후 발생하는 404같은 에러 )
        - URLError : 서버를 찾을 수 없는 경우 (서버 접속조차 실패한 경우 )
'''
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context
# from urllib.request import urlopen
# from urllib.error import HTTPError 
# from urllib.error import URLError 

# try:
#     html = urlopen("https://pythonscrapingthisurldoesnotexist.com")
# except HTTPError as e:
#     print("The server returned an HTTP error")
# except URLError as e:
#     print("The server could not be found!")
# else:
#     print(html.read())


''''''
# 2. Adbanced HTML Parsing
''''''

'''
'''
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
# bs = BeautifulSoup(html, "html.parser")

#     # bs.findAll('태그명', { key : value }) : 특정 조건의 태그 찾기
# nameList = bs.findAll('span', {'class': 'green'}) # bs 객체가 가진 span태그 중 class='green'인 태그만 모두 찾아서 리스트로 저장
# for name in nameList: 
#     print(name.get_text()) # namelist에 저장된 모든 태그객체 속에 담긴 text-contents만 개별로 출력 
 
#     #  re.compile()메서드 활용 : .find_all() 메소드로 특정 텍스트컨텐츠 가진 bs객체 반환 + 정규표현식을 사용한 패턴탐색 ( 참고 : https://systemtrade.tistory.com/345 )
# import re
# TAGS = bs.find_all(text=re.compile('First of all, dear friend+'))
# print(TAGS)

#     # p 글자를 포함하는 태그명 탐색 반환
# import re
# TAGS = bs.find_all(re.compile('^p'))
# print(TAGS)

#     # text 부개내용 포함하는 태그 탐색 반환
# import re
# TAGS= bs.find_all(text = re.compile('text+')) 
# print(TAGS)

#    # header : bs.find_all( [태그1,태그2,태그3,...] ) : 다수의 태그 찾기
# titles = bs.find_all(['h1', 'h2','h3','h4','h5','h6']) # bs객체에서 해당하는 태그들을 모두 찾아 titles에 리스트로 저장
# print([title for title in titles]) # 저장된 모든 title에 해당하는 태그들을 태그채로 출력

#     # bs.find_all( '태그명', { 'key' : { 'value1', 'value2' }} ) : 다수의 value 조건값을 건 태그 찾기
# allText = bs.find_all('span', {'class':{'green', 'red'}}) #class='green' or class='red'에 해당하는 span 모두를 선택하여 저장
# print([text for text in allText]) # 

#     # 연습 : {key:value} 조건을 건 태그 찾기
# html = urlopen('https://news.v.daum.net/v/20220319141033996')
# bs = BeautifulSoup(html, 'html.parser')
# all = bs.find_all('p',{'dmcf-ptype':'general'})
# for i in all :
#     print(i)

#     # text contents value가 'the prince'와 일치하는 값을 모두 찾고 개수를 출력
# nameList = bs.find_all(text='the prince')
# print(nameList)
# print(len(nameList))


'''
########################
* bs의 트리 구조 및 선택자
    (참고 : https://yganalyst.github.io/web/crawling_3/)

    bs.find('태그명') : 기본 : 조건 태그를 반환
        자식 : 항상 부모보다 한 태그 아래에 위치한 태그 : bs.find('태그명').childern : 조건 태그의 한계층 밑의 자식 태그들을 반환
        자손 : 부모태그 아래에 위치한 '모든' 태그들 : bs.find('태그명').descendants : 조건 태그 밑 모든 depth의 자식태그들을 반환
        부모 : bs.find('태그명').parent : 조건 태그를 포함하는 부모 태그를 반환
    
            - bs.find('태그명1').find_parent('태그명2') : 조건태그1의 부모 태그 중 조건태그2를 포함하는 내용까지만 거슬러 올라가서 이를 반환
            - bs.find('태그명1').find_parents('태그명2') : 조건태그1의 부모 태그 중 조건태그2를 포함하는 모든 내용을 찾아서 반환 
            - bs.find('태그명').find_parents() : 조건태그1 상위의 모든 부모태그를 찾아서 반환
        
        형제 : bs.find('태그명',{'key : value'}).tr.next_siblings : 해당 next_siblings() 함수는 웹페이지의 '테이블(표)'에서 데이터를 쉽게 수집 가능하다.
'''
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context
# from urllib.request import urlopen
# from bs4 import BeautifulSoup

# html = urlopen('http://www.pythonscraping.com/pages/page3.html')
# bs = BeautifulSoup(html, 'html.parser')

#     # bs.find('태그명', { 'key' : 'value' }) : 키:값 조건을 충족하는 특정 태그를 반환 // bs.children
# for child in bs.find('table',{'id':'giftList'}).children: 
#     print(child)
    

''' 
형제(siblings) : 

        bs.find(조건).next_siblings : 

            - siblings는 특정 객체의 동일 부모, 동일 레벨에 있는 타 객체들을 말한다.
            -next_siblings() 는 말그대로 ( 선택한 bs객체를 제외하고 ) 선택한 객체의 형제인 태그(아래 예제에선 형제 중 tr태그를 특정했음)를 가져오는 것이다.
            
            -해당 next_siblings() 함수는 웹페이지의 '테이블(표)'에서 데이터를 쉽게 수집 가능하다.
                특히 헤더가 있을 때 유용하다.
'''
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context
# from urllib.request import urlopen
# from bs4 import BeautifulSoup

# html = urlopen('http://www.pythonscraping.com/pages/page3.html')
# bs = BeautifulSoup(html, 'html.parser')

# for sibling in bs.find('table', {'id':'giftList'}).tr.next_siblings: # tr은 특정 태그의 형제들 중 tr태그를 가진 형제를 특정한 태그명임 ( 없으면 모든 형제를 반환)
#     print(sibling) 


    
'''
부모( parent / parents ) : 보통은 구조를 이해하고 부모부터 자식으로 객체들을 긁어나가기 마련이지만,
                            자식을 선택하고 이로부터 부모를 찾아야할 때가 있다.

        bs.find('태그명').parent : 조건 태그를 포함하는 부모 태그를 반환
    
            - bs.find('태그명1').find_parent('태그명2') : 조건태그1의 부모 태그 중 조건태그2를 포함하는 내용까지만 거슬러 올라가서 이를 반환
            - bs.find('태그명1').find_parents('태그명2') : 조건태그1의 부모 태그 중 조건태그2를 포함하는 모든 내용을 찾아서 반환 
            - bs.find('태그명').find_parents() : 조건태그1 상위의 모든 부모태그를 찾아서 반환
'''

#     # 아래의 예제는 특정 이미지를 이용해서, 그 이미지를 가진 부모로 거슬러올라가, 특정 이미지에 해당되는 가격을 가져온 것이다.
# from urllib.request import urlopen
# from bs4 import BeautifulSoup

# html = urlopen('http://www.pythonscraping.com/pages/page3.html')
# bs = BeautifulSoup(html, 'html.parser')
# print(bs.find('img',{'src':'../img/gifts/img1.jpg'}).parent.previous_sibling.get_text()) 
#         # (1)조건에 해당하는 특정 이미지를 find()
#          # (2) 해당 bs객체의 직전레벨 부모 태그를 선택(.parent) 
#           # (3) 선택한 부모태그의 직전형제태그를 선택(.previous_siblings) 
#            # (4) 태그 내 텍스트 반환 


'''
#############
정규표현식(Regular Expression)과 람다표현식(Lambda Expression)을 사용하여 HTML 분석하기
(https://m.blog.naver.com/sohyunst/221658044640)



# re모듈 : regex는 정규표현식으로 알려져있다.
            파이썬에서 정규 표현식을 사용할 때, 내장모듈인 re를 사용한다.
  
  why 정규표현식? : 파이썬에서는 문자열에서도 기본적으로 특정 문자 또는 문자열이 존재하는지나 어느 위치에 있는지와 같은 기능을 제공한다.
                    그러나, 만약 문자열 안에 정수만 추출하고 싶다면, 문자열 제공함수만으로는 한계가 있다.
                    
                    이 때, 정규표현식을 사용하면 쉽게 찾을 수 있다.
    
    re.compile() 메서드 : 같은 정규식 패턴을 반복문 내에서 반복해서 사용해야 할 경우 re.match/re.sub 등의 메서드를 직접 가져다 사용하면 성능상의 부담이 있다.
                         정규식은 컴파일이란 과정을 거치기 때문인데, re모듈로부터 직접 갖다 쓰면 매번 컴파일이란 비싼 계산을 해야하기 때문에 성능이 떨어지는 것이다.
                         re.compile은 컴파일을 미리 해두고 이를 저장할 수 있는 효율적 메소드이다.
'''
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import re   

# html = urlopen('http://www.pythonscraping.com/pages/page3.html')
# bs = BeautifulSoup(html, 'html.parser')

#     # <img>태그 중 키인 src의 값에 re.compile함수를 사용하여 정규표현식을 적용하기 
# images = bs.find_all('img', {'src':re.compile('\.\.\/img\/gifts/img.*\.jpg')}) # 정규표현식의 패턴과 일치할 경우의 조건을 src키의 value값에 적용
# for image in images: 
#     print(image['src'])
    
    # lambda() 함수를 사용
# TAGS = bs.find_all(lambda tag: len(tag.attrs) == 2)
# for TAG in TAGS :
#     print(TAG)



''''
#URL Link Crawler
'''
# html 소스 상 링크를 탐색 반환

# from urllib.request import urlopen
# from bs4 import BeautifulSoup 

# html = urlopen('https://en.wikipedia.org/wiki/BTS')
# bs = BeautifulSoup(html, 'html.parser')
# for link in bs.find_all('a'):
#     if 'href' in link.attrs:
#         print(link.attrs['href'])
