#Dictionary comprehension

import random
names = ["isma", "domi", "vicente"]
student_scores = {name:random.randint(10,70) for name in names}
print(student_scores)

passed_students = {name:"Approved" for name in names if student_scores[name] >= 40}
print(passed_students)
