#class including __repr__ and __str__
class Country:
    def __init__(self,name,population,area):
        self.name = name
        self.population = population
        self.area = area
    def name(self):
        return (self.name)
    def population(self):
        return(self.population)
    def area(self):
        return(self.area)
    def is_larger(self,country):
        if self.area > country.area:
            return True
        else:
            return False
    def population_density(self):
        return float(self.population)/float(self.area)
    def __repr__(self):
        return 'Country(\'{}\',{},{})'.format(self.name,self.population,self.area)
    def __str__(self):
        return '{} has a population of {} and is {} square km.'.format(self.name,self.population,self.area)