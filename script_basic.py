#print("あいうえお")
#print("かきくけこ")
#print("さしすせそ")

a_price = 1000
text=f"この商品は{a_price}円です。"
print(text)

#print("変数タイプ＝ ") 
#a_price = "斎藤"
#print(a_price)a_price

math = 82
japanese = 74
english = 60
avg_score = (math + japanese + english)/3
print(avg_score)

surname="佐々木"
given_name="まゆ"
full_name=surname+given_name
print(full_name)

#文字列リスト追加・削除
student_names=["斎藤","小林","佐々木","田中","阿部","山田","鈴木","浜田",]
student_names2=["武田","上杉","織田","羽柴","徳川","北条","毛利","長曾我部","島津"]
a=student_names[0]
b=student_names[-2]
print(a)
print(b)

x=student_names[:3]
print(x)
print(len(x))

z=student_names+student_names2
print(z)
print(len(z))

z.append("芦名")
print(z)
print(len(z))

z.remove("田中")
print(z)
print(len(z))

#関数
a=max(z)
print(a)

a=min(z)
print(a)

#a=sum(z)
#print(a)

a=sorted(z)
print(a)

a=sorted(z,reverse=True)
print(a)

#リスト
scores=[82,74,60]

avg_score=sum(scores)/len(scores)
print(avg_score)

scores.append(70)
print(scores)
avg_score=sum(scores)/len(scores)
print(avg_score)

#辞書
scores={"数学":82,
        "国語":74,
        "英語":60,
        "理科":92,
        "社会":70}
science=scores["理科"]
print(science)

score1=scores["理科"]-scores["社会"]

text=f"理科は社会より{score1}点高いです。"
print(text)

avg_score=sum(list(scores.values()))/len(scores)
print(f"平均は{avg_score}点です。")

x=scores.values()
print(f"{x}")


x=list(scores.values())
print(f"リストは{x}です。")

scores["体育"]=82
print(scores)

scores["国語"]=84
print(scores)

x=list(scores.keys())
print(x)

x=list(scores.values())
print(x)

#集合
x={1,2,4}
print(x)

x.add(7)
print(x)

x.remove(2)
print(x)

x={0,1,3,6}
y={0,2,5,6}

#和集合（両集合の全要素を表示）
z=x|y    
print(f"和集合は{z}です。")

#差集合（両集合の全要素の差を表示）
z=x-y    
print(f"差集合は{z}です。")

#積集合（両集合の両方にある要素を表示）
z=x&y    
print(f"積集合は{z}です。")


#タプル


