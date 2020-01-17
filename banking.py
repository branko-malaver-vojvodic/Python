#Simple banking functions
class BankAccount:
    def __init__(self,balance):
        self.x=balance
    def withdraw(self,less):
        self.x-=less
    def deposit(self,plus):
        self.x+=plus
    def balance(self):
        return(float(self.x))

        
    

        
        
            
            
        
