import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(temp))
# data_dict = data.to_dict()
# print(data_dict["temp"])

temp_list = data["temp"].to_list()

average_temp = data["temp"].mean()
max_temp = data["temp"].max()

# print(data[data["temp"] == max_temp])

monday = data[data.day == "Monday"]
monday_temp_f = (int(monday.temp) * 9/5) + 32
# print(monday_temp_f)





