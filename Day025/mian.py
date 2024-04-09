# import csv
# with open("weather_data.csv")as w_file:
#     data = csv.reader(w_file)
#     temp = []
#     for row in data:
#         print(row)
#         if row[1] != 'temp':
#             row[1] =  int(row[1])

import pandas as pd

# data = pd.read_csv("weather_data.csv")
# temp_list = data['temp'].to_list()

# hell no 
# temp_len = len(temp_list)
# total_temp = 0
# for temp in temp_list:
#     total_temp += tem
# avg_temp = total_temp/temp_len
# print(avg_temp)

# avg_temp = sum(temp_list)/len(temp_list)
# print(avg_temp)
# print(data['temp'].mean())
# print(data['temp'].max())

# print(data[data.temp == data.temp.max()])

# monday = data[data.day == 'Monday']
# monday_temp = int(monday.temp.iloc[0])
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)

# # Create a dataframe from scratch
# data_dict = {
#     'students': ['Amy', 'James', 'Angela'],
#     'scores': [76, 56, 65]
# }
# data = pd.DataFrame(data_dict)
# data.to_csv("new_data.csv")

sdata = pd.read_csv("004201~1.CSV")
Gray_sq_count = (len(sdata[sdata["Primary Fur Color"] == "Gray"]))
Black_sq_count = (len(sdata[sdata["Primary Fur Color"] == "Black"]))
Cinnamon_sq_count = (len(sdata[sdata["Primary Fur Color"] == "Cinnamon"]))
data_dict = {
    'Fur_Color': ['Gray', 'Black', 'Cinnamon'],
    'Count': [Gray_sq_count, Black_sq_count, Cinnamon_sq_count]
}
df = pd.DataFrame(data_dict)
df.to_csv("squirrel_color_count.csv")