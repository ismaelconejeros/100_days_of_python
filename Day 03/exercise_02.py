#Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
#It should tell them the interpretation of their BMI based on the BMI value.
#The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

#Under 18.5 they are underweight
#Over 18.5 but below 25 they have a normal weight
#Over 25 but below 30 they are slightly overweight
#Over 30 but below 35 they are obese
#Above 35 they are clinically obese.

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

BMI = weight / (height**2)

print(BMI)

if BMI < 18.5:
	print(f'UNDERWEIGHT! Your BMI is {BMI:.2f}')
elif BMI < 25:
	print(f'NORMAL WEIGHT! Your BMI is {BMI:.2f}')
elif BMI < 30:
	print(f'SLIGHTLY OVERWIGHT Your BMI is {BMI:.2f}')
elif BMI < 35:
	print(f'OBESE! Your BMI is {BMI:.2f}')
else:
	print(f'CLINICAL OBESE! Your BMI is {BMI:.2f}')