import pandas as pd

data = pd.read_csv('100_days_of_python\Day 25\weather_data.csv')

# temps = data['temp'].mean()
# print(temps)

# temps = data['temp'].max()
# print(temps)

# print(data[data['temp'] == data['temp'].max()])

data_dict = {
    "students": ["isma", "domi", "vicente"],
    "scores": [7.0, 3.95, 1.8]
}

data = pd.DataFrame(data_dict)
data.to_csv('100_days_of_python\Day 25\\new_data.csv')