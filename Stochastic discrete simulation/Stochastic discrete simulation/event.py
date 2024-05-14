class event:
    
    def __init__(self,type,t,animal):
        self.time=t
        self.type=type
        self.animal=animal

    def get_time(self):
        return self.time
        
    def get_type(self):
        return self.type

    def get_animal(self):
        return self.animal
    
    def show(self):
        return [self.type,float(self.time),self.animal.get_type()]
