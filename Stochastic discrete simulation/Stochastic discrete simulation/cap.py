class cap:
    def __init__(self):
        self.events=[]

    def get_events(self):
        return self.events

    def addE(self,e):

        self.events=[e1 for e1 in self.events if e1.get_time()<e.get_time()]+[e]+\
             [e1 for e1 in self.events if e1.get_time()>e.get_time()]

    def delE(self):
        if len(self.events)>0:
            self.events=self.events[1:]
        else:
            print("Erro de delE! A cap está vazia")

    def nextE(self):
        if len(self.events)>0:
            return self.events[0]
        else:
            print("Erro de nextE! A cap está vazia")
            
    def showE(self):
        return [e.show() for e in self.events] 
    
    def delEIndiv(self,v):
        self.events=list(filter(lambda a: a.get_animal() != v, self.events))
