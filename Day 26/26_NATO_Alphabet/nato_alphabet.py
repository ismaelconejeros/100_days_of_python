import pandas as pd

data = pd.read_csv('100_days_of_python\Day 26\\26_NATO_Alphabet\\nato_phonetic_alphabet.csv')
df = pd.DataFrame(data)
df2 = df.to_dict()

nato_dict = {df2['letter'][i]:df2['code'][i] for i in range(len(df2['letter']))}

while True:
    name = input("Enter a word: ").upper()
    nato_name = [nato_dict[i] for i in list(name)]
    print(nato_name)