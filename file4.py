import csv
with open("dsp.csv" ,newline='') as csvfile:
    d=csv.DictReader(csvfile)
    print("period     subject")
    print("___________________")
    for i in d:
        print(i['Period'],i['Subject'])