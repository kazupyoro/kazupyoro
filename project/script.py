from my_packeges.my_module import Student
from datetime import datetime

t=datetime.today()
print(t)

student_1 = Student("斉藤そうま",82,74,60,92,72)
s1_avg = student_1.average_score()
print(student_1.name + "さんの平均点：",s1_avg)
