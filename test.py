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
    

datamean = sum(heightlist)/listlength
print(datamean)

