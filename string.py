def add(a,b):
    return a+b 
print( add(3,4))

num = 3
if num > 1  : 
    print("num is greater than 1")


for a in [1,2,3] :
    print(a)

a = 1E9
print(a)


a =  '=' * 50 
print(a)
print("test test")
print(a)

a = "Life is too short"
print(len(a))
print(a[3])
print(a[0] + a[1]+ a[2] + a[3])
print(a[0:4]) 
print(a[0:-13])


print ("I eat %d apples" % 3)
print ("I eat %s apples" % "three")


print ("I eat %d apples. so i was sick for %s day" % (3, "three"))
print ("Error is %d%%." % 98)

number = 10
day = "three"
print ("I ate {0} apples. so I was sick for {1} days.".format(number, day))
print("I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3))

print(f'I ate {number} apples. so I was sick for {day} days.')

d = {'name':'홍길동', 'age':30}
print (f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.')


print("life"+"is"+"too short")

print("life", "is", "too short")

# 한줄에 결과값 출력 
for i in range(10):
    print(i, end=' ')