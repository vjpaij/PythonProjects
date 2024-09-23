# import csv
#
# with open("weather_data.csv") as data_file:
#     # creates an csv object
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         print(row)
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)

# as we could see above, for fetching a single column data, we had to write an extensive code
# this is where panda helps

import pandas as pd

data = pd.read_csv("weather_data.csv")
print(data)
print(data["temp"])
# data["temp"] can also be written as data.temp
print(data.temp)

data_dict = data.to_dict()
print(data_dict)

data_temp_list = data["temp"].to_list()
print(data_temp_list)

total_temp = 0
avg_temp = 0
for temp in data_temp_list:
    total_temp += temp
avg_temp = round(total_temp/len(data_temp_list),2)
print(f"Average temparature is {avg_temp}")
#or avg_temp = round(sum(data["temp"]/len(data_temp_list),2)

#simpler method using pandas

panda_avg_temp = round(data["temp"].mean(),2)
print(f"Average temp using panda is {panda_avg_temp}")

#get entire row
monday_row =(data[data.day == "Monday"])
print(monday_row)
#get a value from that row
print(monday_row.temp)
#do some calculation with that row
monday_fah = (monday_row.temp * (9/5)) + 32
print(monday_fah)
# panda always display results with index. if you want the terminal display only the value without index.
#monday_fah_noind = (monday_row.temp[0] * (9/5)) + 32
#better way to write is as below. item() gives us the raw data
monday_fah_noind = (monday_row.temp.item() * (9/5)) + 32
print(monday_fah_noind)

#get the row with max temperature
print(data[data.temp == data.temp.max()])

#creating a dataframe from scratch
data_dict_new = {
    "students" : ["Anant", "Bala", "Charlie"],
    "scores" : [98, 58, 70]
}
data_new = pd.DataFrame(data_dict_new)
print(data_new)
#we can convert it to csv file
data_new.to_csv("new_data.csv")




