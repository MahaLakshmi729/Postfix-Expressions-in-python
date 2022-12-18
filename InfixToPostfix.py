from Stack import Stack
from string import  ascii_letters

SYMBOLS="^*/+-"

class Expression:
    def __init__(self,exp:str) -> None:
        self.exp=exp.replace(" ","")
        self.out=""
        self.stack=Stack()
        self.priority={"^":3,"*":2,"/":2,"+":1,"-":1}

    def evaluate(self)-> str:
        for i in self.exp:
            if i in ascii_letters:
                self.out+=i.upper()
            elif i== "(":
                self.stack.push("(")
            elif i in SYMBOLS:
                self.evaluate_symbols(i)
            elif i ==")":
                while self.stack.show_top() != "(":
                    self.out+=self.stack.pop()
                self.stack.pop()            
        if not self.stack.is_empty():
            while not self.stack.is_empty():
                self.out+=self.stack.pop()

        return self.out


    def evaluate_symbols(self,symbol):
        top_priority=self.get_priotity(self.stack.show_top())
        if self.stack.is_empty() or self.stack.show_top() == "(":
            self.stack.push(symbol)
        
        elif  top_priority< self.get_priotity(symbol):
            self.stack.push(symbol)
        
        elif top_priority == self.get_priotity(symbol) or top_priority > self.get_priotity(symbol):
            self.out+=self.stack.pop()
            self.evaluate_symbols(symbol)
            

    def get_priotity(self,val):
        return self.priority.get(val)