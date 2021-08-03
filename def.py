def add(a, b):
    return a+b

print(add(3,4))


#여러개의 입력값을 받는 함수 

def add_many(*args): 
    result = 0 
    for i in args: 
        result = result + i 
    return result 

print(add_many(1,2,3,4,5,6,7,8,9,10));


#응용 
def add_mul(choice, *args): 
    if choice == "add": 
        result = 0 
        for i in args: 
            result = result + i 
    elif choice == "mul": 
        result = 1 
        for i in args: 
            result = result * i 
    return result

print(add_mul('add', 1,2,3,4,5))
print(add_mul('mul', 1,2,3,4,5))



def print_kwargs(**kwargs): 
    print(kwargs)

print_kwargs(name="조호관", birhdy ="920423", email ="hokwan92@naver.com");

# **kwargs처럼 매개변수 이름 앞에 **을 붙이면 매개변수 kwargs는 딕셔너리가 되고 모든 key=value 형태의 결괏값이 그 딕셔너리에 저장된다.



a = 1 
def vartest(): 
    global a  #전역변수 설정  
    a = a+1

vartest() 
print(a)

# 람다식 함수 선언 
add = lambda a, b: a+b 
print(add(3,4))


