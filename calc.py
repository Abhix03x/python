class Calculator:
    op1=0
    op2=0
    def add(self):
        print("sum is:",self.op1+self.op2)
    def sub(self):
        print("difference is:",self.op1-self.op2)
    def mul(self):
        print("product is:",self.op1*self.op2)
    def div(self):
        print("Quotient is:",self.op1/self.op2)
    def run(self):
        self.op1=int(input("enter the 1st operator"))
        self.op2=int(input("enter the 2st operator"))
        op = input("enter the operation")
        if op =='+':
            self.add()
        elif op =='-':
            self.sub()
        elif op =='*':
            self.mul()
        elif op =='/':
            self.div()

s = Calculator()
while True:
    s.run()

