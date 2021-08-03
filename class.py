class Calculator:
    def __init__(self):    # 클래스 선언할때 실행 됨 
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))


print("");

class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result


fourCal1  = FourCal(1,2)
print(fourCal1.add())
print()

#  클래스 상속  (오버라이딩 가능 )
class MoreFourCal(FourCal):
    pass

moreFourCal1 = MoreFourCal(3,2)
print(moreFourCal1.add())