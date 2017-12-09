from urllib.request import urlopen
from bs4 import BeautifulSoup #Camel Case
import pyexcel

# 1. Download dantri home page
webpage = urlopen('http://dantri.com.vn') #open connection
data = webpage.read()
html_content = data.decode('utf8')
print(html_content)

# 2. Analyze ROI(Region Of Interest)
# 2.1 Create BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')
ul = soup.find('ul', 'ul1 ulnew') #find 1
li_list = ul.find_all('li')
# print(li_list[0].prettify())

# for li in li_list:
#     print(li.prettify())
#     print("* " * 20)


new_list = []

for li in li_list:
    # h4 = li.h4 #find('h4')
    # a = h4.a #find('a')
    a = li.h4.a
    news = {
        'title': a.string,
        'link': 'http://dantri.com.vn' + a['href']
    }
    new_list.append(news)

pyexcel.save_as(records = new_list, dest_file_name = "dantri.xlsx")

# 3. Extract data from ROI
