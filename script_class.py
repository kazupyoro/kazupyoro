# class
class User:
    def __init__(self,name,mail_address,point):
        self.name = name
        self.mail_address = mail_address
        self.point = point
    def add_point(self,point):
        self.point += point

user_1 = User("佐藤葵","sato@example.com",500)
user_2 = User("小林ゆい","kobayashi@example.com",1000)
x = user_1.name
y = user_2.name
print(x,user_1.point)
print(y,user_2.point)

z = user_2.add_point=200
print(z)
