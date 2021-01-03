#write a program that tests the compatibility between two people.

#To work out the love score between two people:

#Take both people's names and check for the number of times the letters in the word TRUE occurs. 
# Then check for the number of times the letters in the word LOVE occurs. 
# Then combine these numbers to make a 2 digit number.

#For Love Scores less than 10 or greater than 90, the message should be:
#"Your score is **x**, you go together like coke and mentos."

#For Love Scores between 40 and 50, the message should be:
#"Your score is **y**, you are alright together."

#Otherwise, the message will just be their score. e.g.:
#"Your score is **z**."

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

true = ['t','r','u','e','T','R','U','E']
love = ['l','o','v','e','L','O','V','E']

names = name1 + name2

true_num = 0
love_num = 0

for letter in names:
	if letter in true:
		true_num += 1
	if letter in love:
		love_num += 1

score = int(str(true_num) + str(love_num))

if score < 10 or score > 90:
	print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
	print(f"Your score is {score}, you are alright together.")
else:
	print(f"Your score is {score}.")


#-------------Other way

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

names = name1.lower() + name2.lower()

t = names.count('t')
r = names.count('r')
u = names.count('u')
e = names.count('e')
l = names.count('l')
o = names.count('o')
v = names.count('v')
e = names.count('e')

true = str(t+r+u+e)
love = str(l+o+v+e)

score = int(true+love)

if score < 10 or score > 90:
	print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
	print(f"Your score is {score}, you are alright together.")
else:
	print(f"Your score is {score}.")