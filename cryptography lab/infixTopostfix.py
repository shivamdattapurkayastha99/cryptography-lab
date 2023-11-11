class infixTopostfix:
    def __init__(self,capacity) -> None:
        self.top=-1
        self.capacity=capacity
        self.array=[]
        self.output=[]
        self.precedence={'+':1,'-':1,'*':2,'/':2,'^':3}
    def isEmpty(self):
        return True if self.top==-1 else False
    def peek(self):
        return self.array[-1]
    def pop(self):
        if not self.isEmpty():
            
