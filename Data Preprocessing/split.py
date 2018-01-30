# 100% working 
import csv
csvfile = open('forestfires.csv', 'r').readlines()
filename = 1
for i in range(len(csvfile)):
    if i % 360 == 0:
        open(str(filename) + '.csv', 'w+').writelines(csvfile[i:i+360])
        filename += 1
