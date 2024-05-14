# Definição da grid
import numpy as np

class grid:

    def __init__(self,L,Q):
        self.grid= [[[] for i in range(L)] for n in range(L)]       
        self.limit=Q
        self.l=L-1

    ### Verifica se está livre
    def freeQ(self,x,y):
        return len(self.grid[x][y])<self.limit


    ### Adiciona a uma cell          
    def addv(self,v,x,y):
        if self.freeQ(x,y):
            self.grid[x][y].append(v)

    ### Posição de um elemento
    def pos(self,x,y,v):
        resp=False
        for x in range(len(self.grid)):
            for y in range(len(self.grid)):
                for cell in range(len(self.grid[x][y])):
                    if self.grid[x][y][cell]==v:
                        resp=cell
        return resp

    ### Remove um elemento de uma célula        
    def delv(self,v):
        x,y=v.coord()
        self.grid[x][y].remove(v)

    ### Animais que estão dentro da célula
    def get_animals(self,x,y):
        return self.grid[x][y]
    
    def get_rabbits(self,x,y):
        return list(i for i in self.grid[x][y] if i.get_type() in ['CM','CF'])

    def neig(self,x,y,k):
        neighboors=[]
        for x2 in range(x-k,x+k+1):
            for y2 in range(y-k,y+k+1):
                if (-1 < x <= len(self.grid) and -1 < y <= len(self.grid)
                and (x != x2 or y != y2)
                and(0 <= x2 <= len(self.grid)) 
                and (0 <= y2 <= len(self.grid))
                and (abs(x2-x)>=k or abs(y2-y)>=k)):

                    neighboors.append((x2,y2))
        return neighboors

    #Evento de move
    def move(self,v):
        limite=v.get_lim()
        xstep=np.random.randint(-limite-1,limite+1)
        ystep=np.random.randint(-limite-1,limite+1)
        xval=np.sign(xstep)
        yval=np.sign(ystep)
        xdone=0
        ydone=0
        xv,yv=v.coord()
        x=xv;y=yv
        while xdone<abs(xstep):
            if (x==self.l and xval>0) or (x==0 and xval<0):
                xval=xval*(-1)
            x+=xval
            xdone+=1

        while ydone<abs(ystep):
            if (y==self.l and yval>0) or (y==0 and yval<0):
                yval=yval*(-1)
            y+=yval
            ydone+=1

        if self.freeQ(x,y)!=0:
            self.delv(v)
            self.addv(v,x,y)
            v.set_cord(x,y)

    #Evento de reprodução
    def reproduce(self,v,p):
        x,y=v.coord()
        reprod=False
        for i in self.get_rabbits(x,y): #Procurar se há coelhos de outro sexo
            if i.get_sex()+v.get_sex()==1:
                reprod=True
        vb=np.random.binomial(1,p) # calcular a probabilidade de reproduzir através de uma distribuição bernoulli
        if vb==1 and reprod==True:
            if self.freeQ(x,y)!=0:
                return (True,x,y) # Caso reproduza devolve as novas coordenadas do coelho e True
            else:
                return (False,x,y)
        else:
            return (False,x,y)

    #Evento de captura
    def capture(self,v):
        x,y=v.coord()
        bunnies=self.get_rabbits(x,y) # Recolher todos os coelhos na célula
        if bunnies!=[] and \
            np.random.binomial(1,len(bunnies)/(len(bunnies)+1))==1 :
            return np.random.choice(bunnies) # escolher um coelho aleatório
        else:
             return None

    def show_grid(self):
        for i in self.grid: 
            line=''
            for d in i:
                line+='['
                for a in d:
                    line+=str(a.descp())
                line+=']'
            print(line)
