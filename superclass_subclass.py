#Super Classes and SubClasses
class Employee:
    def __init__(self):
        pass
    def show(self):
        print('In employee.show')
class EmplyRef(Employee):
    def show(self):
        print('Overriding and in emplyRef.show')
class EmplyExtnd(Employee):
    def show(self):
        print('extending employee class')
        print('In EmplyExtnd.show')
        Employee.show(self)
