from Stack import Stack

NUMBERS="0123456789"
SYMBOLS="+*-/^"

class Expression:
    def __init__(self,exp:str) -> None:
        self.exp=exp.replace(" ","")
        self.stack=Stack()
        
    def evaluate(self):
        for i in self.exp:
            if(i in NUMBERS):
                self.stack.push(i)
            if(i in SYMBOLS):
                exp1=self.stack.pop()
                exp2=self.stack.pop()
                self.stack.push(eval(f"{exp2}{ i if i!='^' else '**'}{exp1}"))
        return self.stack.pop()
            