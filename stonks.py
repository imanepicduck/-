import csv
from re import s #i don't know where this came from
from this import s
from typing import Counter #i don't know where this came from
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

for i in range (len(new_data)):
    num=file_data [i][1]
    new_data.append(float(num))

data= Counter (new_data)
mode_range={
    "100-1000":0,
    "1000-10000":0,
    "10000-10000000":0
}

dollars = (9)

for income, occurence in data.items():
    if 100<float(dollars)<1000:
        mode_range("100-1000") +-occurence
    elif 1000<float(dollars)<10000:
        mode_range("1000-10000") +-occurence
    elif 10000<float(dollars)<10000000:
        mode_range("10000-10000000") +-occurence

mode_range1,mode_occurence=0,0
for range, occurence in mode_range.items():
    if occurence>mode_occurence:
        mode_range1,mode_occurence=[int(range.split("-")[0]),int(range.split("-")[1])], occurence

mode=float((mode_range1[0]+mode_range1[1])/2)
print("mode = ", str(mode))