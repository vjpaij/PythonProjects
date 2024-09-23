import pandas as pd

squirrel_data = pd.read_csv("Squirrel_Data.csv")
fur_list = squirrel_data["Primary Fur Color"].dropna()
fur_colour = fur_list.unique()
print(fur_list)
print(fur_colour)

# count_gray = 0
# count_cinnamon = 0
# count_black = 0
#
# for colour in fur_list:
#     if colour == "Gray":
#         count_gray += 1
#     elif colour == "Cinnamon":
#         count_cinnamon += 1
#     elif colour == "Black":
#         count_black += 1

count_gray = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
count_cinnamon = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
count_black = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])

squirrel_dict = {
    "colour" : fur_colour,
    "count" : [count_gray, count_cinnamon, count_black]
}

squirrel_df = pd.DataFrame(squirrel_dict)
squirrel_df.to_csv("Squirrel_Fur.csv")


