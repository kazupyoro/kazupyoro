
scores=[90,30,49]

for x in scores:
    print(x)

fruits={"apple":130,"banana":350,"lemon":100}
for name,price in fruits.items():
    print(name,price)

for x in range(5):
    print(x) 

numbers=[10,21,100,18,2]
for n in numbers:
    if n >= 100:
        break
    print(f"{n}:繰り返し")
print("for文の外")

numbers=[10,21,32,65]
for n in numbers:
    print(f"{n}:前処理")
    if n % 2 == 0:
        continue
    print(f"{n}:後処理")

scores={"数学":82,
        "国語":74,
        "英語":60,
        "理科":92,
        "社会":70}
for k,v in scores.items():
    print(f"{k}は{v}点です")

# + 足す
# - 引く
# / 割る
# * かける
# ** 乗算
# // 床除算(floor division)演算子 除算の整数部分
# % 除算の余り
years=[1996,1997,1998,1999,2000,2003,2004,2005,2006,2007,2008,2009,2010,2011]
for year in years:
    if year % 400 == 0:
        print(year,":うるう年です")
    elif year % 100 == 0:
        print(year,":うるう年です")
    elif year % 4 == 0:
        print(year,":うるう年です")
    else:
        print(year,":平年です")

for n in range(1,101):
    if n % 15 == 0:
        print(n,":FizzBuzz")
    elif n % 5 == 0:
        print(n,":Buzz")
    elif n % 3 == 0:
        print(n,":Fizz")
    else:
        print(n)

