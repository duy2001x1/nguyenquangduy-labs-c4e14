from urllib.request import urlopen
from bs4 import *
import pyexcel
webpage = urlopen('https://www.nhaccuatui.com/') #Open connection
data = webpage.read()
html_content = data.decode('utf8')

soup = BeautifulSoup(html_content, 'html.parser')
div = soup.find('div',"list_chart_music") # find one
ul = div.find('ul')
_li_list = ul.find_all('li')
news_list = []
for li in _li_list:
    a = li.h3.a
    b = li.h4
    h4 = b.find_all('a')
    artist_list = []
    for i in h4:
        artist_list.append(i.string)
    news = {
        'name':a.string,
        'artist':artist_list
    }
    news_list.append(news)
print(news_list)
# pyexcel.save_as(records=news_list, dest_file_name="list.xls")
