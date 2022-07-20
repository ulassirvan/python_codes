from point_class import point
from bilinmeyen_class import bilinmeyen
class vector:
    def __init__(self,i=0.0,j=0.0,k=0.0,by_ijk=True,start:point=point(0,0,0),end:point=point(0,0,0)):
        """
        :param i: i paramter for vector
        :param j: j paramter for vector
        :param k: k paramter for vector defult 0 for 2d vectors
        :param start: starting point for vector defult:point(0,0,0)
        """
        if by_ijk:
            if isinstance(i,(float,int)):
                self.i=i
                self.i_is_number = True
            else :
                self.i=bilinmeyen(adı=i)
                self.i_is_number = False
            if isinstance(j,(float,int)):
                self.j=j
                self.j_is_number=True
            else :
                self.j=bilinmeyen(adı=j)
                self.j_is_number = False
            if isinstance(k,(float,int)):
                self.k=k
                self.k_is_number=True
            else :
                self.k=bilinmeyen(adı=k)
                self.k_is_number=False
        else :
            if isinstance(end.x,float) and isinstance(start.x,float):
                self.i=end.x-start.x
                self.i_is_number=True
            else :
                self.i=str(end.x)+" - "+str(start.x)
                self.i_is_number=False
            if isinstance(end.y,float) and isinstance(start.y,float):
                self.j=end.y-start.y
                self.j_is_number=True
            else :
                self.j=str(end.y)+" - "+str(start.y)
                self.j_is_number=False
            if isinstance(end.z,float) and isinstance(start.z,float):
                self.k=end.z-start.z
                self.k_is_number=True
            else:
                self.k=str(end.z)+" - "+str(start.z)
                self.k_is_number=False
        self.point=start
        self.unit=self.unit_vector()




    def lenght(self):
        if(self.k_is_number and self.j_is_number and self.i_is_number):
            return  ((self.i) ** 2 + (self.j) ** 2 +(self.k) ** 2) ** (1 / 2)

    def unit_vector(self):
        if(self.k_is_number and self.j_is_number and self.i_is_number):
            lenght=self.lenght()
            return vector((self.i/lenght),(self.j/lenght),(self.k/lenght))
        else:
            pass


