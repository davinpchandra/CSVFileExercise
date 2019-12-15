import csv
from datetime import datetime
import pygal

filename = 'activity.csv'

with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        data = {}
        steps = []

        for row in reader:
            row.append("days")

            for i in range(9):
                for j in range(5):
                    x = "weekday"
                    row[3]=x
                for k in range(2):
                    y = "weekend"
                    row[3]=y

            if row[3] == "weekend":
                if row[2] not in data:
                    data.update({row[2]:0})
                    for v in data.values():
                        if row[0] != 'NA':
                            v += int(row[0])
                else:
                    for p in data.keys():
                        for v in data.values():
                            if row[0] != 'NA':
                                v += int(row[0])

        for u in data.values():
            average =int( u / 31 )
            steps.append(average)

hist = pygal.Bar()
hist.add("Steps" , steps)
print(steps)
hist.render_to_file("histogram4.svg")











