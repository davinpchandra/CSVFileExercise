import csv
from datetime import datetime
import pygal

filename = 'activity.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates , steps = [] , []
    current_date = 0
    stepping = 0
    date = 1

    for row in reader:
            current_dates = datetime.strptime(row[1], "%Y-%m-%d")
            if current_dates == current_date:
                if row[0] != 'NA':
                    step = int(row[0])
                    stepping += step

            else:
                current_date = datetime.strptime(row[1], "%Y-%m-%d")
                dates.append(date)
                steps.append(stepping)
                stepping = 0
                date += 1
                if row[0] != 'NA':
                    step = int(row[0])
                    stepping += step

    steps.append(stepping)

mean = sum(steps) // len(dates)
print("Mean : ",mean)
sortedSteps = sorted(steps)
print("Median : ",sortedSteps[31])
del steps[0]
del dates[0]
print(steps)
print(dates)


hist = pygal.Bar()
hist.add("Steps" , steps)
hist.render_to_file("histogram.svg")