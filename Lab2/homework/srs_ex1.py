from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from youtube_dl import YoutubeDL

webpage = urlopen('https://www.apple.com/itunes/charts/songs/')
data = webpage.read()
html_content = data.decode('utf8')

soup = BeautifulSoup(html_content, 'html.parser')
section = soup.find('section', 'section chart-grid')
div = section.find('div', 'section-content')
ul = div.find('ul')
li_list = ul.find_all('li')

new_list = []

for li in li_list:
    a_h3 = li.h3.a
    a_h4 = li.h4.a
    songs = a_h4.string
    news = {
        'Name': a_h3.string,
        'Artists': a_h4.string
    }
    new_list.append(news)

# pyexcel.save_as(records = new_list, dest_file_name = "top_songs.xlsx")


loop = True
while loop:
    choice = str(input("Do you want to download 1 song or all? (q to quit) "))
    if choice == '1' or choice == '1 song':
        place_in_chart = int(input("Enter the place in chart of the song(1-100): "))
        top = place_in_chart - 1
        options = {
            'default_search': 'ytsearch',
            'max_downloads': 1,
            'format': 'bestaudio/audio'
        }
        dl = YoutubeDL(options)
        dl.download([new_list[top]['Name'] + ' ' + new_list[top]['Artists']])
    elif choice == 'all':
        options = {
            'default_search': 'ytsearch',
            'max_downloads': len(new_list),
            'format': 'bestaudio/audio'
        }

        dl = YoutubeDL(options)
        for download in new_list:
            dl.download([download['Name'] + ' ' + download['Artists']])
            loop = False
    elif choice == 'q' or choice == 'Q':
        loop = False
    else:
        print("Sorry, try again.")
