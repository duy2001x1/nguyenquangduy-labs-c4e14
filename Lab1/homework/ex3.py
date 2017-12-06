from pymongo import MongoClient
from matplotlib import pyplot

client = MongoClient("mongodb://admin:admin@ds021182.mlab.com:21182/c4e")

db = client.get_default_database()

data = db['customers']

events = data.find({'ref': "events"}).count()
wom = data.find({'ref': "wom"}).count()
ads = data.find({'ref': "ads"}).count()

print("Events:", events)
print("Word of mouth:", wom)
print("Advertisements:", ads)

labels = ['Events', 'Word of mouth', 'Advertisements']
colors = ['lightskyblue', 'gold', 'violet']
data = [events, wom, ads]

pyplot.pie(data, labels = labels, colors = colors, shadow = True)
pyplot.axis('equal')
pyplot.show()
