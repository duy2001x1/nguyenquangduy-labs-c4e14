from matplotlib import pyplot

labels = ['MAC', 'PC', 'LINUX']
colors = ['lightskyblue', 'lightcoral', 'gold']
data = [2, 20, 1]

pyplot.pie(data, labels = labels, colors = colors, shadow = True)
pyplot.axis('equal')
pyplot.show()
