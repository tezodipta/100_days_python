import csv
with open("weather_data.csv")as w_file:
    data = csv.reader(w_file)
    temp = []
    for row in data:
        print(row)

    