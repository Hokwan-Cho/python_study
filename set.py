s1 = set([1,2,3])   ## list(s1)  이나 tuple(s1) 으로 자료형 변환 간으 
s2 = set("hello")

print(s1)
print(s2)


""" 
set 특징 

1. 중복이 없음. 
2. 순서가 없음 

 """



s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print(s1 & s2) # s1 과 s2 모두 포함하는것 (교집합) 
print(s1 | s2) # s1 이나 s2 중 포함하는 것  (합집합)
print(s2 - s1) # 차집합 

s1.add(7)
s1.update([8,9,10])
print(s1)

s1.remove(10);
print(s1)
