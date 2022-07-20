
class bilinmeyen:
    def __init__(self,adı,katsayı=1.0):
        self.adı=adı
        self.katsayı=katsayı



    def __add__(self, other):
        if isinstance(other,bilinmeyen):
            if self.adı==other.adı:
                return bilinmeyen(adı=self.adı,katsayı=(self.katsayı+other.katsayı))
            else :
                return str(self)+str("+")+str(other)
        if isinstance(other,(float,int)):
            if other>=0:
                return str(self)+str("+")+str(other)
            else:
                return str(self)  + str(other)


    def __sub__(self, other):
        if isinstance(other,bilinmeyen):
            if self.adı==other.adı:
                return bilinmeyen(adı=self.adı,katsayı=self.katsayı-other.katsayı)
            else :
                return str(self)+str("-")+str(other)
        if isinstance(other,(float,int)):
            if other>=0:
                return str(self)+str("-")+str(other)
            else:
                return str(self)+ str("+")+ str(abs(other))

    def __pow__(self, power, modulo=None):
        return str(self.adı+"**"+str(power))


    def __str__(self):
        if self.katsayı!=1:
            return str(self.katsayı)+str(self.adı)
        else:
            return str(self.adı)

    def solve_for(self,value):
        pass



x=bilinmeyen(adı="x")
print(x**2)