from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

webpage = urlopen('https://www.nhaccuatui.com')
data = webpage.read()
html_content = data.decode('utf8')

soup = BeautifulSoup(html_content, 'html.parser')
div = soup.find('div', 'list_chart_music')
ul = div.find('ul')
li_list = ul.find_all('li')

new_list = []

for li in li_list:
    a1 = li.h3.a
    h4 = li.h4
    a_list = h4.find_all('a')
    artist_list = []
    for a in a_list:
        artist_list.append(a.string)
        artists = ', '.join(artist_list)
    news = {
        'title' : a1.string,
        'artist' : artists
    }
    new_list.append(news)

print(new_list)

pyexcel.save_as(records = new_list, dest_file_name = "nhaccuatui.xlsx")
