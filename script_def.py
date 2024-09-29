def print_hello():
    print("こんにちは")

print_hello()

def add_numbers(a,b):
    c = a + b
    d = a - b
    return c,d

x,y =add_numbers(2,3)
print(x)
print(y)

def is_leap_yeas(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
    
year = 2023
result = is_leap_yeas(year) 
print(year,result)