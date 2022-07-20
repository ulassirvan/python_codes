from bilinmeyen_class import bilinmeyen

class point:
    def __init__(self,x,y,z):
        if isinstance(x,(int,float)):
            x=float(x)
        else:
            x=bilinmeyen(x)
        if isinstance(y,(int,float)):
            y=float(y)
        else:
            y=bilinmeyen(y)
        if isinstance(z,(int,float)):
            z=float(z)
        else:
            z=bilinmeyen(z)

        self.x=x
        self.y=y
        self.z=z

