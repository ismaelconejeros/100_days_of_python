#You are going to write a program that calculates the highest score from a List of scores.

##e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

#Important you are not allowed to use the max or min functions. The output words must match the example. i.e

#Hint
#Think about the logic before writing code. How can you compare numbers against each other to see which one is larger?

# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

student_scores.sort()

print(f'The highest score is {student_scores[len(student_scores)-1]}')

#-----------

maximo = student_scores[0]

for score in student_scores:
	if score > maximo:
		maximo = score

print(f'The highest score is {maximo}')