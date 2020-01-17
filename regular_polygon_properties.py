#Properties of a regular polygon with n sides with length s
import math
class Polygon:
    def __init__(self,n,s):
        self.n = n
        self.s = s
    def perimeter(self):
        return(self.n*self.s)
    def area(self):
        return(((self.s**2)*self.n)/(4*math.tan((math.pi)/self.n)))
