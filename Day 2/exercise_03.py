#Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
#It will take your current age as the input and output a message with our time left in this format:
#You have x days, y weeks, and z months left.

# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

goalyears = 90
age = int(age)

daysyear = 356
weeksyear = 52
monthsyear = 12

goaldays = goalyears*daysyear
goalweeks = goalyears*weeksyear
goalmonths = goalyears*monthsyear

agedays = age*daysyear
ageweeks = age*weeksyear
agemonths = age*monthsyear

print(f'You have {goaldays-agedays} days, {goalweeks-ageweeks} weeks, and {goalmonths-agemonths} months left.')