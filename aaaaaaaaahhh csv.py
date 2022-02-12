import csv
from re import s #i don't know where this came from
from this import s #i don't know where this came from
from numpy import append #i don't know where this came from

from tenacity import t #i don't know where this came from
data = (3)
with open (data.csv, newline= '') as s: 
    reader = csv.reader(s)
    file_data = list (reader)

file_data = (0)

new_data = []
for i in range (len(file_data)):
    num = file_data [i][1]
    new_data.append(float(num))

n=len(new_data)
total=0
for x in new_data:
    total+=x

mean= total/n

print("the arithmetic mean is *drumroll plays* " +str(mean))

