# import csv

# temp = []
# with open('weather_data.csv') as f:
#     data = csv.reader(f)
#     for idx, row in enumerate(data):
#         if idx > 0:
#             temp.append(int(row[1]))
#     print(temp)

# import pandas

# data = pandas.read_csv('weather_data.csv')
# # print(data['temp'])

# # dictionary
# data_dict = data.to_dict()
# print(data_dict)

# # list
# temp_list = data['temp'].to_list()
# print(temp_list)

# # average and max
# print(data['temp'].mean())
# print(data['temp'].max())

# # get data in row
# print( data[data['day'] == 'Monday'])
# print( data[data['temp'] == data['temp'].max()])

# # create dataframe from scratch
# data_dict = {
#     'students': ['Amy', 'James', 'Angela'],
#     'scores': [76, 34, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv('new_data.csv')

import pandas
data = pandas.read_csv('Central_Park_Squirrel_Census.csv')
grey = len(data[data['Primary Fur Color'] == 'Gray'])
red = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black = len(data[data['Primary Fur Color'] == 'Black'])

new_file = {
    'Fur Color': ['grey', 'red', 'black'],
    'Count': [grey, red, black],
}
data = pandas.DataFrame(new_file)
data.to_csv('new_file.csv')