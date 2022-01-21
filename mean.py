from collections import Counter
import csv
with open('SOCR-HeightWeight.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

new_data=[]
total =0
x = len(file_data)
for i in file_data:
    total+=float(i[2])
    new_data.append(float(i[2]))
new_data.sort()

def get_mean(x,total):
    mean=total/x
    print("Mean / Average is: " + str(mean))

get_mean(x,total)

def get_median(x,new_data):
    if x%2==0:
        median1=float(new_data[x//2])
        median2=float(new_data[x//2-1])
        median=(median1+median2)/2
    else:
        median=float(new_data[x//2])
    print("Median is:" + str(median))

get_median(x,new_data)

def get_mode(new_data):
    data=Counter(new_data)
    mode_data_for_range={
        "75-85":0,
        "85-95":0,
        "105-115":0,
        "125-135":0,
        "145-155":0,
        "165-175":0,
       
    }
    for weight, occurence in data.items():
        if 75 < weight < 85:
            mode_data_for_range["75-85"] += occurence
        elif 85 < weight < 95:
            mode_data_for_range["85-95"] += occurence
        elif 105 < weight < 115:
            mode_data_for_range["105-115"] += occurence
        elif 125 < weight < 135:
            mode_data_for_range["125-135"] += occurence
        elif 145 < weight < 155:
            mode_data_for_range["145-155"] += occurence
        elif 165 < weight< 175:
            mode_data_for_range["165-175"] += occurence

    mode_range, mode_occurence = 0, 0

    for range, occurence in mode_data_for_range.items():
        if occurence>mode_occurence:
            mode_range,mode_occurence=[int(range.split("-")[0]),int(range.split("-")[1])],occurence
    mode=float(mode_range[0]+mode_range[1])/2
    print("Mode is",mode)


get_mode(new_data)