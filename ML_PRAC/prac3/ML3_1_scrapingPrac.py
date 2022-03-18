

########### Data collection with python ###################

''''''
# 1. Basic 
''''''

'''
1.1 ssl : secure socket layer : 보안 소켓 계층
        : 웹사이트와 브라우저 사이에 전송되는 데이터를 암호화하여 인터넷 보안을 유지하는데 사용된다
'''
import ssl # ssl 사이트를 다루기 위해서 ssl 사용
from urllib.request import urlopen

ssl._create_default_default_https_context = ssl._create_unverified_context  

html = urlopen('http://pythonscraping.com/pages/page1.html')
print(html.read())


'''
'''
import ssl
ssl._create_default_default_https_context = ssl._create_unverified_context
from urllib.request import urlopen
from bs4 import BeautifulSoup as BS

html = urlopen('http://pythonscraping.com/pages/page1.html')
bs = BS(html.read(), 'html.parser')
print(bs.h1)

'''
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

#     #
# nameList = bs.findAll('span', {'class': 'green'})
# for name in nameList:
#     print(name.get_text())
 
#     #
# titles = bs.find_all(['h1', 'h2','h3','h4','h5','h6'])
# print([title for title in titles])

#     #
# allText = bs.find_all('span', {'class':{'green', 'red'}})
# print([text for text in allText])

#     #
# nameList = bs.find_all(text='the prince')
# print(nameList)
# print(len(nameList))

#     #
# title = bs.find_all(id='title', class_='text')
# print([text for text in allText])


'''
'''
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context
# from urllib.request import urlopen
# from bs4 import BeautifulSoup

# html = urlopen('http://www.pythonscraping.com/pages/page3.html')
# bs = BeautifulSoup(html, 'html.parser')

# for child in bs.find('table',{'id':'giftList'}).children:
#     print(child)
    

'''
'''
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context
# from urllib.request import urlopen
# from bs4 import BeautifulSoup

# html = urlopen('http://www.pythonscraping.com/pages/page3.html')
# bs = BeautifulSoup(html, 'html.parser')

# for sibling in bs.find('table', {'id':'giftList'}).tr.next_siblings:
#     print(sibling) 
    
'''
'''
# from urllib.request import urlopen
# from bs4 import BeautifulSoup

# html = urlopen('http://www.pythonscraping.com/pages/page3.html')
# bs = BeautifulSoup(html, 'html.parser')
# print(bs.find('img',
#               {'src':'../img/gifts/img1.jpg'})
#       .parent.previous_sibling.get_text())

'''
'''
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import re

# html = urlopen('http://www.pythonscraping.com/pages/page3.html')
# bs = BeautifulSoup(html, 'html.parser')
# images = bs.find_all('img', {'src':re.compile('\.\.\/img\/gifts/img.*\.jpg')})
# for image in images: 
#     print(image['src'])
    
#     #
# bs.find_all(lambda tag: len(tag.attrs) == 2)

#     #
# bs.find_all('', text='Or maybe he\'s only resting?')


''''''
 #3. Webpage Crawler
''''''

'''
'''
# from urllib.request import urlopen
# from bs4 import BeautifulSoup 

# html = urlopen('https://en.wikipedia.org/wiki/BTS')
# bs = BeautifulSoup(html, 'html.parser')
# for link in bs.find_all('a'):
#     if 'href' in link.attrs:
#         print(link.attrs['href'])
