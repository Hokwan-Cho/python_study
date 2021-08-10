# 현재 날짜의 요일 구하기  

def getToday() : 
    from datetime import datetime
    dayList = ['얼', '화', '수','목','금','토','일']
    day = dayList[datetime.today().weekday()]
    return day 

print(getToday())


# 같은 숫자 중복제거 
numList = [1,1,3,3,0,1,1] 

def except_duplication(numList):      
    answer = []
    for i in numList:
        if answer[-1:] == [i]: continue   #answer[-1] 하면 빈 리스트라서 out of index , 리스트 슬라이스하고, 리스트형식으로 만들어서 비교
        answer.append(i)
    return answer

print(except_duplication(numList))




#   두 정수 사이의 모든 합 
def sum_num(num1, num2): 
    if (num1 > num2) :     
        return  sum(range(num2, num1+1))
    else :
        return sum(range(num1, num2+1))
    
print(sum_num(1,10))