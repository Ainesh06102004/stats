import csv
with open('SOCR-HeightWeight.csv', newline = '') as d:
    data = csv.reader(d)
    list1 = list(data)

list1.pop(0)

heightlist = []

listlength = len(list1)

for items in list1:
    height = items[1]
    heightlist.append(float(height))

increase = heightlist.sort()

if(listlength%2 == 0):
    firstno = float(heightlist[listlength/2])
    secondno = float(heightlist[(listlength/2) + 1])

    median = (firstno + secondno) / 2
else:
    median = heightlist[(listlength + 1)/2]

print(median)