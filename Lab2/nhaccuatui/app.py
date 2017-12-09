from urllib.request import urlopen

raw_data = urlopen('https://www.nhaccuatui.com/').read()

file = open('nct.html', 'wb') # w = write, b = binary
file.write(raw_data)
file.close()
