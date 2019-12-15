import csv
from datetime import datetime
import pygal

filename = 'activity.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, steps = [], []

    current_date = 0
    stepping = 0
    count = 0

    for row in reader:
        current_dates = datetime.strptime(row[1], "%Y-%m-%d")
        if current_dates == current_date:
            if row[0] != 'NA':
                step = int(row[0])
                stepping += step
                count += 1
        else:
            current_date = datetime.strptime(row[1], "%Y-%m-%d")
            if count != 0:
                average = stepping // count
                steps.append(average)
                stepping = 0
                count = 0
                if row[0] != 'NA':
                    step = int(row[0])
                    stepping += step
                    count += 1


    steps.append(average)

print(steps)
print(len(steps))

hist = pygal.Bar()
hist.add("Steps" , steps)
hist.render_to_file("histogram2.svg")


