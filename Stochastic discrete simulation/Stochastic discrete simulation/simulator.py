import modules
import cap
import event
import grid
import numpy as np
import matplotlib.pyplot as plt

# definição de parametros para a função
L=18
NCM=30
NCF=15
NR=8
Q=4
TS=250
KC=12
KR=18
TD=4.5
TR=5
PR=0.8
TC=12
TMC=13
TMR=30


def simulation(L,NCF,NR,Q,TS,KC,KR,TD,TR,PR,TC,TMC,TMR):

    T=0
    IDV=0
    ### Inicializar CAP
    caps=cap.cap()
    ###Inicializar grid
    grids=grid.grid(L,Q)
    ### Adicionar elementos
    population=[]
    #COELHOS MACHOS
    for i in range(NCM):
        R=modules.Rabbit('CM',IDV,0,0,TD,KC,TR,TMC)
        population.append(R)
        ev=event.event('death',R.death(T),R)
        caps.addE(ev)
        caps.addE(event.event('move',R.move(T),R))
        caps.addE(event.event('reproduce',R.reproduce(T),R))
        IDV+=1
    #COELHOS FEMEAS
    for i in range(NCF):
        R=modules.Rabbit('CF',IDV,0,0,TD,KC,TR,TMC)
        population.append(R)
        caps.addE(event.event('death',R.death(T),R))
        caps.addE(event.event('move',R.move(T),R))
        caps.addE(event.event('reproduce',R.reproduce(T),R))
        IDV+=1
    #RAPOSAS
    for i in range(NR):
        R=modules.Fox('R',IDV,0,0,TD,KR,TMR,TC)
        population.append(R)
        caps.addE(event.event('death',R.death(T),R))
        caps.addE(event.event('move',R.move(T),R))
        caps.addE(event.event('capture',R.capture(T),R))
        IDV+=1

    ### Adicionar os animais a uma celula random:
    pop_n=population[::]
    coordeandas=[]
    while pop_n!=[]:
        x=np.random.randint(0,L)
        y=np.random.randint(0,L)
        if grids.freeQ(x,y):
            grids.addv(pop_n[0],x,y)
            An=pop_n[0]
            An.set_cord(x,y)
            pop_n.pop(0)
            coordeandas.append([An.descp(),(x,y)])

    #######################################################################
    ### Começar ciclo
    MRaxis=[]
    FRaxis=[]
    Faxis=[]
    Taxis=[]
    Numeros={'CM':NCM,'CF':NCF,'R':NR}
    IDV-=1
    while T<= TS and len(caps.get_events())>0:
        evento=caps.nextE()
        tipo=evento.get_type()
        print(tipo.upper()*4)
        animal=evento.get_animal()
        value=0
        if tipo=='death':
            grids.delv(animal)
            caps.delEIndiv(animal)
            value=-1

        elif tipo=='move':
            grids.move(animal)
            caps.addE(event.event('move',animal.move(T),animal))

        elif tipo=='capture':
            if grids.capture(animal)!=None:
                caps.addE(event.event('death',T,grids.capture(animal)))
                caps.addE(event.event('capture',animal.capture(T),animal))

        elif tipo=='reproduce':
            resp=grids.reproduce(animal,PR)
            if resp[0]==True:
                IDV+=1
                print('************* Reprodução *************')
                x=resp[1]
                y=resp[2]
                sexo=np.random.choice(['CF','CM'])
                if sexo=='CF':
                    R=modules.Rabbit('CF',IDV,x,y,TD,KC,TR,TMC)
                else:
                    R=modules.Rabbit('CM',IDV,x,y,TD,KC,TR,TMC)
                grids.addv(R,x,y)
                population.append(R)
                caps.addE(event.event('death',R.death(T),R))
                caps.addE(event.event('move',R.move(T),R))
                caps.addE(event.event('reproduce',R.reproduce(T),R))
                value=1
                Numeros[R.get_type()]=Numeros[R.get_type()]+value
                
            caps.addE(event.event('reproduce',animal.reproduce(T),animal))

        if tipo!='reproduce':
            Numeros[animal.get_type()]=Numeros[animal.get_type()]+value

        MRaxis.append(Numeros['CM'])
        FRaxis.append(Numeros['CF'])
        Faxis.append(Numeros['R'])
        Taxis.append(T)
        #mudar o tempo
        T=evento.get_time()
        
        #apagar a tarefa feita
        if tipo!='death':
            caps.delE()

    plt.title("Simulação")
    plt.xlabel("Tempo")
    plt.ylabel("Nr de animais")
    plt.step(Taxis,MRaxis,label='male rabbits')
    plt.step(Taxis,FRaxis,label='female rabbits')
    plt.step(Taxis,Faxis,label='foxes')
    plt.legend(loc="upper center")
    plt.show()


simulation(L,NCF,NR,Q,TS,KC,KR,TD,TR,PR,TC,TMC,TMR)