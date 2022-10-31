import pandas

data = pandas.read_csv("Squirrel_Data.csv")
# print(type(data[data["Primary Fur Color"] == "Black"]))
# grey = (data["Primary Fur Color"] == "Gray")
# black = (data["Primary Fur Color"] == "Black")
# cinnamon = (data["Primary Fur Color"] == "Cinnamon")
# sum_grey = grey.sum()
# sum_black = black.sum()
# sum_cinnamon = cinnamon.sum()

all_colors = data.groupby("Primary Fur Color")["Primary Fur Color"].agg(["count"])
all_colors.to_csv("all_squirrel_colors_list.csv")



