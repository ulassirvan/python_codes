from vector_class import vector
from point_class import point
class scene:
    def __init__(self,force_vectors:dict):
        self.force_vectors=force_vectors
    #def calculat_force_equilibrium(self):

    def cacluat_angle(self,vector1_name,vector2_name):
        pass


vector_ac=vector(by_ijk=False,start=point(2.4,5,0),end=point(2,2.6,4))
vector_ad=vector(by_ijk=False,start=point(1,1.8,5),end=point(0,3,2))
#vectors={vector_ad:vector_ad,vector_ac:vector_ac}
#sahne=scene(vectors)
#sahne.cacluat_angle(vector_ad,vector_ac)



print(vector_ac.i)
print(vector_ac.j)
print(vector_ac.k)


print(vector_ad.i)
print(vector_ad.j)
print(vector_ad.k)


