import numpy as np
class Animal:
    def __init__(self,type,ID,x,y,TD,Lim,TM):
        self.id=ID
        self.type=type
        self.x=x
        self.y=y
        self.td=TD
        self.lim=Lim
        self.tm=TM
        self.death_time=None
        self.move_time=None
        if self.type=='CM':
            self.sex=1
        else:
            self.sex=0

    def get_type(self):
        return self.type

    def get_td(self):
        return self.td

    def get_id(self):
        return self.id

    def get_lim(self):
        return self.lim

    def coord(self):
        return self.x,self.y

    def set_cord(self,x,y):
        self.x=x
        self.y=y
        
    def death(self,t):
        self.death_time=t+np.random.exponential(self.tm)
        return self.death_time

    def move(self,t):
        self.move_time=t+np.random.exponential(self.td)
        return self.move_time
        
    def descp(self):
        return (self.id,self.type)

    def get_sex(self):
        return self.sex

class Rabbit(Animal):
    def __init__(self,type,ID,x,y,TD,Lim,TR,TM):
        Animal.__init__(self,type,ID,x,y,TD,Lim,TM)
        self.tr=TR
        self.reproduce_time=None
        

    def reproduce(self,t):
        self.reproduce_time=t+np.random.exponential(self.tr)
        return self.reproduce_time


class Fox(Animal):
    def __init__(self,type,ID,x,y,TD,Lim,TM,TC):
        Animal.__init__(self,type,ID,x,y,TD,Lim,TM)
        self.tc=TC
        self.capture_time=None
        
    def capture(self,t):
        self.capture_time=t+np.random.exponential(self.tc)
        return self.capture_time
