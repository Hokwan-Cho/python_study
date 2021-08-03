dic = {'name':'조호관', 'phone':'010-4686-7423', 'birth': '920423'} 

print(dic)
print(dic['name'])
print(dic['phone'])
print(dic['birth'])

del dic['name']

print(dic)
print(dic.keys())  # 리스트가 아닌 객체 반환 

dic['name'] = 'Hokwan Cho'

for k in dic.keys():
    v = dic[k]
    print(f"key is {k} , value  is {v}") 



# dic_keys 객체를 리스트 변환 
print(list(dic.keys()));

#dic_values 리스트 변환 
print(list(dic.values())); 

print(dic.get("email", "hokwan92@naver.com"));  # get으로 key의 value값 불러올 수 있음 , 없으면 None 반환, 없을경우 디포틀 지정 가능 

print( 'name' in dic); 
print('email' in dic);