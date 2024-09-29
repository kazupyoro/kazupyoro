# class
class Student:
    def __init__(self,name, math,japanese,
                 english, science, society):
        self.name = name
        self.math = math
        self.japanese = japanese
        self.english = english
        self.science = science
        self.society = society

    def average_score(self):
        avg = (self.math + self.japanese + self.english
               + self.science + self.society ) / 5
        return avg

student_1 = Student("森川葵",82,74,60,92,72)
x = student_1.name
y=" 平均点:"
s1_avg = student_1.average_score()
print(x+y,s1_avg)
