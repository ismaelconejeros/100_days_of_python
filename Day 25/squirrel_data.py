import pandas as pd

data = pd.read_csv('100_days_of_python\Day 25\Squirrel_Data.csv')
df = pd.DataFrame(data['Primary Fur Color'].value_counts())
df.to_csv('100_days_of_python\Day 25\Squirrel_Data_fur_color.csv')
