# 선언방법 
t1 = ()
t2 = (1,) #한개만 선언할시에 , 붙여줌 
t3 = (1, 2, 3)
t4 = 1, 2, 3
t5 = ('a', 'b', ('ab', 'cd'))
# 차이점 : 튜플과 리스트의 가장 큰 차이는 값을 변화시킬 수 있는가 여부이다. 즉 리스트의 항목 값은 변화가 가능하고 튜플의 항목 값은 변화가 불가능하다.



t1 = (1, 2, 'a', 'b')
print(t1[0])
print(t1[3])

t1 = (1, 2, 'a', 'b')
print(t1[1:])