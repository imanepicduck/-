import csv
from re import s #i don't know where this came from
from this import s
from cv2 import sort #i don't know where this came from
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
new_data = sort

if n %2 ==0:
    median1=float(new_data[n//2])
    median2=float(new_data[n//2-1])
    median=(median1+median2)/2

else: 
    median=new_data[n//2]

print("hopefully the median lol:"+str(median))