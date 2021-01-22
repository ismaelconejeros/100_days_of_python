with open('C:/Users/isma/Desktop/VSC/100_days_of_python/100_days_of_python/Day 24/24_mail_merge/invited_list/invited_names.txt') as file:
    invited_list = file.readlines()

with open('C:/Users/isma/Desktop/VSC/100_days_of_python/100_days_of_python/Day 24/24_mail_merge/letters/starting_letter.txt') as file:
    letter = file.read()

for i in invited_list:
    name = i.replace("\n", "")
    new_letter = letter.replace("Name", name)
    filename = f'C:/Users/isma/Desktop/VSC/100_days_of_python/100_days_of_python/Day 24/24_mail_merge/ready_to_send/letter_for_{name}.txt'
    with open(filename, mode='w') as file:
        x = file.write(new_letter)