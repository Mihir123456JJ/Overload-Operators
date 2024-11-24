class x:
    def __init__(self,a):
        self.a=a
    def __lt__(self,other):
        if (self.a<other.a):
            return "Num1 is Less then Num2"
        else:
            return "Num2 is Less than Num1"
    def __eq__(self,other):
        if (self.a==other.a):
            return "Both Num1 and Num2 are equal"
        else:
            return "They are Not equal"
num1=x(2)
num2=x(4)        
print(num1==num2)                