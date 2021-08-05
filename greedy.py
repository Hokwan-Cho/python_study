""" 
타로는 자주 JOI잡화점에서 물건을 산다. 
JOI잡화점에는 잔돈으로 500엔, 100엔, 50엔, 10엔, 5엔, 1엔이 충분히 있고, 언제나 거스름돈 갯수가 가장 적게 잔돈을 준다. 
타로가 JOI잡화점에서 물건을 사고 카운터에서 1000엔 지폐를 한장 냈을 때, 받을 잔돈에 포함된 잔돈의 갯수를 구하는 프로그램을 작성하시오.
 """

coin = (500, 100, 50, 10, 1 );
change =  1000 -  int(input("물건 값을 입력해주세요: "))  
index = -1 
answer = dict() 

if change < 0 :
    print( "1000엔 보다 비싸서 살 수 없습니다. "); 
else : 
    while (change != 0 ):
        index = index +1 
        coinCount =  change // coin[index] 
        change = change - coinCount * coin[index] 
        answer[ coin[index] ] = coinCount

if len(answer) > 0 :
    print(answer)



"""
[강의번호, 강의시작시간, 강의 종료시간] 인 집합이 있음. 
여러개의 수업을 진행할때, 한번에 가장 많은 수업을 할 수 있는 경우

예제 : [1,1,3], [2,2,5], [3,4,7], [4,1,8], [5,5,9], [6,8,10], [7,9,11], [8,11,14], [9,13,16] 

"""
lecture= [[1,1,3], [2,2,5], [3,4,7], [4,1,8], [5,5,9], [6,8,10], [7,9,11], [8,11,14], [9,13,16]]



""" 
def selectLectureCount(args) : 
    
    lecture = list(args)
    
    for item in lecture : 
        item[2] -item[1] 
         """




