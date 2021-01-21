import csv, json


coordinates = []
datetime = []
data = {}

# f = open("travels.json", "w")
with open('20210112-235627.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    for row in csv_reader:
        if('lat' in row[2]):
            continue
        coordinates.append([row[2], row[3]])
        datetime.append(row[1])

data["coordinates"] = coordinates
data["date-time"] = datetime

with open("CSV_to_JSON_coordinateOutput.json", "w") as file:
    json.dump(data,file)
