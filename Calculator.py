# Assignment by Ashwin P M
# Submitted on 23 June 2019
"""
The Calculator class consists of methods:
        sum(a,b): returns sum
        difference(a,b): returns difference
        product(a,b): returns product
        quotient(a,b): returns quotient
        remainder(a,b): returns remainder
        divide(a,b): returns the floating point division result
        power(a,b): returns power
        evaluate(s): returns the result of the expression:(s is an expression string)
                a operator b
                        Eg: 4 * 5
                                returns 20
                operators used are +,-,*,//,%,/,**
"""



class Calculator:
        
        def __init__(self):
                self.num1 = 0
                self.num2 = 0
                self.result = 0
                self.li = []
                
        def sum(self, a, b):
                return a+b
        
        def difference(self, a, b):
                return a-b
        
        def product(self, a, b):
                return a*b
        
        def quotient(self, a, b):
                return a//b
        
        def remainder(self, a, b):
                return a%b
        
        def divide(self, a, b):
                return a/b
        
        def power(self, a, b):
                return a**b
        
        def hasNum(self, ns):
                for i in ns:
                        if i.isdigit():
                                return True
                return False
        
        def evaluate(self, exp):
                if '+' in exp and len(exp.split('+')) == 2:
                        li = exp.split('+')
                        self.num1 = eval(li[0])
                        self.num2 = eval(li[1])
                        self.result = self.sum(self.num1, self.num2)
                elif '-' in exp and len(exp.split('-')) == 2:
                        li = exp.split('-')
                        self.num1 = eval(li[0])
                        self.num2 = eval(li[1])
                        self.result = self.difference(self.num1, self.num2)
                elif '*' in exp and len(exp.split('*')) == 2:
                        li = exp.split('*')
                        self.num1 = eval(li[0])
                        self.num2 = eval(li[1])
                        self.result = self.product(self.num1, self.num2)
                elif '//' in exp and len(exp.split('//')) == 2:
                        li = exp.split('//')
                        self.num1 = eval(li[0])
                        self.num2 = eval(li[1])
                        self.result = self.quotient(self.num1, self.num2)
                elif '%' in exp and len(exp.split('%')) == 2:
                        li = exp.split('%')
                        self.num1 = eval(li[0])
                        self.num2 = eval(li[1])
                        self.result = self.remainder(self.num1, self.num2)
                elif '/' in exp and len(exp.split('/')) == 2:
                        li = exp.split('/')
                        self.num1 = eval(li[0])
                        self.num2 = eval(li[1])
                        self.result = self.divide(self.num1, self.num2)
                elif '**' in exp and len(exp.split('**')) == 2:
                        li = exp.split('**')
                        self.num1 = eval(li[0])
                        self.num2 = eval(li[1])
                        self.result = self.power(self.num1, self.num2)
                elif '-' in exp and len(exp.split('-')) == 3:
                        li = exp.split('-')
                        if not self.hasNum(li[0]) and self.hasNum(li[1]) and self.hasNum(li[2]):
                                self.num1 = -eval(li[1])
                                self.num2 = eval(li[2])
                                self.result = self.difference(self.num1, self.num2)
                        if self.hasNum(li[0]) and not self.hasNum(li[1]) and self.hasNum(li[2]):
                                self.num1 = eval(li[0])
                                self.num2 = -eval(li[2])
                                self.result = self.difference(self.num1, self.num2)
                elif '-' in exp and len(exp.split('-')) == 4:
                        li = exp.split('-')
                        if not self.hasNum(li[0]) and self.hasNum(li[1]) and not self.hasNum(li[2]) and self.hasNum(li[3]):
                                self.num1 = -eval(li[1])
                                self.num2 = -eval(li[3])
                                self.result = self.difference(self.num1, self.num2)
                else:
                        print("Invalid Expression")
                        input("Press any key")
                        exit()
                return self.result
