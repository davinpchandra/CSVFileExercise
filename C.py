import csv
from datetime import datetime
import pygal

filename = 'activity.csv'

print("Fill in the missing values(NA) in the Dataset! ")

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    count = 0

    steps = []
    current_date = 0
    stepping = 0

    for row in reader:
        current_dates = datetime.strptime(row[1], "%Y-%m-%d")
        if current_dates == current_date:
            if row[0] == 'NA':
                interval = row[2]
                date = row[1]
                print("No Data is Available at interval",interval,"on",date)
                new = int(input("Enter the Steps : "))
                stepping += new
                count += 1
            else:
                stepping += row[0]

        else:
            current_date = datetime.strptime(row[1], "%Y-%m-%d")
            steps.append(stepping)
            stepping = 0
            if row[0] == 'NA':
                interval = row[2]
                date = row[1]
                print("No Data is Available at interval", interval, "on", date)
                new = int(input("Enter the Steps : "))
                stepping += new
                count += 1
            else:
                stepping += row[0]

    steps.append(stepping)

print(count , "rows with NAs")
print(steps)
mean = sum(steps) // len(steps)
print("Mean : ",mean)
sortedSteps = sorted(steps)
x = len(steps) // 2
print("Median : ",sortedSteps[x])

hist = pygal.Bar()
hist.add("Steps" , steps)
hist.render_to_file("histogram3.svg")