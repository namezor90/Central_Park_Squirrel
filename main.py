import pandas

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250113.csv')
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
data_dict = {
    "students" : ["Gray", "Cinnamon", "Black"],
    "scores" : [grey_squirrels_count, cinnamon_squirrels_count, black_squirrels_count],
}
data = pandas.DataFrame(data_dict)
data.to_csv('squirrels_color.csv')
