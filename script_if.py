
#関数
numbers=[1,4,19,40,63]
print(numbers)

for n in numbers:
    if n > 10:
        print("xは10以上です")
y=10
z=max(numbers)+y

#年齢確認
age=17
if age >= 20:
    print("成人です")
elif age >= 18:
    print("成人ですが飲酒はできません")
elif age >= 6:
    print("こどもです")
else:
    print("乳児・幼児です")

