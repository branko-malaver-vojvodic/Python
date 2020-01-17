#Workers payments
class Worker:
    def __init__(self,name,taux):
        self.name = name
        self.taux = taux
    def changeRate(self,new_taux):
        self.taux = new_taux
    def pay(self,hours=0):
        print('Not implemented')
class HourlyWorker:
    def __init__(self,name,taux):
        self.name = name
        self.taux = taux
    def changeRate(self,new_taux):
        self.taux = new_taux
    def pay(self,hours):
        if hours <= 40 and hours >= 0:
            self.taux*=hours
            return self.taux
        elif hours > 40:
            self.taux*=hours*2
            return self.taux
        else:
            print('Enter positive numbers')
class SalariedWorker:
    def __init__(self,name,taux):
        self.name = name
        self.taux = taux
    def changeRate(self,new_taux):
        self.taux = new_taux
    def pay(self,hours=0):
        return self.taux*40
    
   
    
        
        
