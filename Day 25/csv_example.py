##Old Method
# with open('100_days_of_python\Day 25\weather_data.csv') as file:
#     data = file.readlines()

# print(data)

#CSV METHOD
import csv

with open('100_days_of_python\Day 25\weather_data.csv') as file:
    data = csv.reader(file)
    temperatures = []
    for i in data:
        if i[1].isnumeric():
            temperatures.append(int(i[1]))
    print(temperatures)