try:
    4/0
except Exception :
    print("오류 발생"); 



try:
    4 / 0
except ZeroDivisionError :
    print("오류 발생 ")



try:
    4 / 0
except ZeroDivisionError as e:
    print(e)

    
try:
    4 / 0
except Exception as e:
    print(e)


try:
    age=int(input('나이를 입력하세요: '))
except:
    pass #오류 회피하기. 
    print('입력이 정확하지 않습니다.')
else:
    if age <= 18:
        print('미성년자는 출입금지입니다.')
    else:
        print('환영합니다.')
finally:
    print("프로그램 종료")