import os
os.system('cls')
import numpy as lista

repetir=True
rut=lista.empty(5,dtype='U8')
tipodepto=lista.empty(5,dtype='str')
piso=lista.empty(5,dtype='int')
indice=0
recargo=100
deptoA=3800
deptoB=3000
deptoC=2800
deptoD=3500
totaldeptoA=0
totaldeptoB=0
totaldeptoC=0
totaldeptoD=0
cantidaddeptoA=0
cantidaddeptoB=0
cantidaddeptoC=0
cantidaddeptoD=0
recargodeptoA=0
recargodeptoB=0
recargodeptoC=0
recargodeptoD=0
cantidadtotaldeptos=0
totaldeptos=0
totalrecargos=0



piso10=[' ',' ',' ',' ']
piso9=[' ',' ',' ',' ']
piso8=[' ',' ',' ',' ']
piso7=[' ',' ',' ',' ']
piso6=[' ',' ',' ',' ']
piso5=[' ',' ',' ',' ']
piso4=[' ',' ',' ',' ']
piso3=[' ',' ',' ',' ']
piso2=[' ',' ',' ',' ']
piso1=[' ',' ',' ',' ']


def Buscar_Rut(numero):
    encontrado=True
    for i in range(0,5):
        if rut[i]==numero:
            print("Rut encontrado:",rut[i])
            encontrado=False
    if encontrado==True:
        print("Rut No encontrado.")

def Reasignar_Compra(numero):
    encontrado=True
    for i in range(0,5):
        if rut[i]==numero:
            print("Rut encontrado:",rut[i])
            print("Departamento asociado: ")
            print("Piso: ",piso[i])
            print("Tipo Depto: ",tipodepto[i])
            print("")
            rut[i]=input("Ingrese rut para Reasignación: ")
            encontrado=False
    if encontrado==True:
        print("Rut no encontrado.")


while repetir:
    print("")
    print("   Inmobiliaria 'MURITO' ")
    print("")
    print("1) Comprar Departamento ")
    print("2) Mostrar Departamentos Disponibles ")
    print("3) Ver listado de Compradores ")
    print("4) Buscar Comprador ")
    print("5) Reasignar Comprar ")
    print("6) Mostrar Ganancias Totales ")
    print("7) Salir ")

    print("Ingrese Opción: ")
    opc=int(input("> "))

    if opc==1:

        rut[indice] = input("Rut del cliente (Sin puntos, ni DV): ")
                
        print("Lista de Departamentos")
        print("")
        print("Piso        Tipo     ")
        print("      A    B    C    D  ")
        print(" 10",piso10)
        print(" 9 ",piso9)
        print(" 8 ",piso8)
        print(" 7 ",piso7)
        print(" 6 ",piso6)
        print(" 5 ",piso5)
        print(" 4 ",piso4)
        print(" 3 ",piso3)
        print(" 2 ",piso2)
        print(" 1 ",piso1)

        print("Que departamento comprará: ")
        piso[indice]= input("Piso:")
        tipodepto[indice]= input("Tipo de depto: ")
        if piso[indice]==1 and tipodepto[indice]=='a' or tipodepto[indice]=='A':
            piso1.insert(0,"X")
            cantidaddeptoA+=1
            totaldeptoA= totaldeptoA + deptoA
        elif piso[indice]==1 and tipodepto[indice]=='b' or tipodepto[indice]=='B':
            piso1.insert(1,"X")
            cantidaddeptoB+=1
            totaldeptoB= totaldeptoB + deptoB
        elif piso[indice]==1 and tipodepto[indice]=='c' or tipodepto[indice]=='C':
            piso1.insert(2,"X")
            cantidaddeptoC+=1
            totaldeptoC= totaldeptoC + deptoC
        elif piso[indice]==1 and tipodepto[indice]=='d' or tipodepto[indice]=='D':
            piso1.insert(3,"X")
            cantidaddeptoD+=1
            totaldeptoD= totaldeptoD + deptoD
        elif piso[indice]==2 and tipodepto[indice]=='a' or tipodepto[indice]=='A':
            piso2.insert(0,"X")
            cantidaddeptoA+=1
            totaldeptoA= totaldeptoA + deptoA
        elif piso[indice]==2 and tipodepto[indice]=='b' or tipodepto[indice]=='B':
            piso2.insert(1,"X")
            cantidaddeptoB+=1
            totaldeptoB= totaldeptoB + deptoB
        elif piso[indice]==2 and tipodepto[indice]=='c' or tipodepto[indice]=='C':
            piso2.insert(2,"X")
            cantidaddeptoC+=1
            totaldeptoA+= deptoC
        elif piso[indice]==2 and tipodepto[indice]=='d' or tipodepto[indice]=='D':
            piso2.insert(3,"X")
            cantidaddeptoD+=1
            totaldeptoC +=deptoD
        elif piso[indice]==3 and tipodepto[indice]=='a' or tipodepto[indice]=='A':
            piso3.insert(0,"X")
            cantidaddeptoA+=1
            totaldeptoA += deptoA
            recargodeptoA= recargodeptoA + recargo
        elif piso[indice]==3 and tipodepto[indice]=='b' or tipodepto[indice]=='B':
            piso3.insert(1,"X")
            cantidaddeptoB+=1
            totaldeptoB += deptoB
            recargodeptoB += recargo
        elif piso[indice]==3 and tipodepto[indice]=='c' or tipodepto[indice]=='C':
            piso3.insert(2,"X")
            cantidaddeptoC+=1
            totaldeptoC += deptoC
            recargodeptoC += recargo
        elif piso[indice]==3 and tipodepto[indice]=='d' or tipodepto[indice]=='D':
            piso3.insert(3,"X")
            cantidaddeptoD+=1
            totaldeptoD += deptoD
            recargodeptoD += recargo
        elif piso[indice]==4 and tipodepto[indice]=='a' or tipodepto[indice]=='A':
            piso4.insert(0,"X")
            cantidaddeptoA+=1
            recargodeptoA= recargodeptoA + recargo
            totaldeptoA += deptoA
        elif piso[indice]==4 and tipodepto[indice]=='b' or tipodepto[indice]=='B':
            piso4.insert(1,"X")
            cantidaddeptoB+=1
            totaldeptoB += deptoB
            recargodeptoB += recargo
        elif piso[indice]==4 and tipodepto[indice]=='c' or tipodepto[indice]=='C':
            piso4.insert(2,"X")
            cantidaddeptoC+=1
            totaldeptoC += deptoC
            recargodeptoC += recargo
        elif piso[indice]==4 and tipodepto[indice]=='d' or tipodepto[indice]=='D':
            piso4.insert(3,"X")
            cantidaddeptoD+=1
            totaldeptoD += deptoD
            recargodeptoD += recargo
        elif piso[indice]==5 and tipodepto[indice]=='a' or tipodepto[indice]=='A':
            piso5.insert(0,"X")
            cantidaddeptoA+=1
            totaldeptoA += deptoA
            recargodeptoA= recargodeptoA + recargo
        elif piso[indice]==5 and tipodepto[indice]=='b' or tipodepto[indice]=='B':
            piso5.insert(1,"X")
            cantidaddeptoB+=1
            totaldeptoB += deptoB
            recargodeptoB += recargo  
        elif piso[indice]==5 and tipodepto[indice]=='c' or tipodepto[indice]=='C':
            piso5.insert(2,"X")
            cantidaddeptoC+=1
            totaldeptoC += deptoC
            recargodeptoC += recargo
        elif piso[indice]==5 and tipodepto[indice]=='d' or tipodepto[indice]=='D':
            piso5.insert(3,"X")
            cantidaddeptoD+=1
            totaldeptoD += deptoD
            recargodeptoD += recargo
        elif piso[indice]==6 and tipodepto[indice]=='a' or tipodepto[indice]=='A':
            piso6.insert(0,"X")
            cantidaddeptoA+=1
            totaldeptoA += deptoA
            recargodeptoA= recargodeptoA + recargo
        elif piso[indice]==6 and tipodepto[indice]=='b' or tipodepto[indice]=='B':
            piso6.insert(1,"X")
            cantidaddeptoB+=1 
            totaldeptoB += deptoB
            recargodeptoB += recargo
        elif piso[indice]==6 and tipodepto[indice]=='c' or tipodepto[indice]=='C':
            piso6.insert(2,"X")
            cantidaddeptoC+=1
            totaldeptoC += deptoC
            recargodeptoC += recargo
        elif piso[indice]==6 and tipodepto[indice]=='d' or tipodepto[indice]=='D':
            piso6.insert(3,"X")
            cantidaddeptoD+=1
            totaldeptoD += deptoD
            recargodeptoD += recargo
        elif piso[indice]==7 and tipodepto[indice]=='a' or tipodepto[indice]=='A':
            piso7.insert(0,"X")
            cantidaddeptoA+=1
            totaldeptoA += deptoA
            recargodeptoA= recargodeptoA + recargo
        elif piso[indice]==7 and tipodepto[indice]=='b' or tipodepto[indice]=='B':
            piso7.insert(1,"X")
            cantidaddeptoB+=1
            totaldeptoB += deptoB
            recargodeptoB += recargo 
        elif piso[indice]==7 and tipodepto[indice]=='c' or tipodepto[indice]=='C':
            piso7.insert(2,"X")
            cantidaddeptoC+=1
            totaldeptoC += deptoC
            recargodeptoC += recargo
        elif piso[indice]==7 and tipodepto[indice]=='d' or tipodepto[indice]=='D':
            piso7.insert(3,"X")
            cantidaddeptoD+=1
            totaldeptoD += deptoD
            recargodeptoD += recargo
        elif piso[indice]==8 and tipodepto[indice]=='a' or tipodepto[indice]=='A':
            piso8.insert(0,"X")
            cantidaddeptoA+=1
            totaldeptoA += deptoA
            recargodeptoA= recargodeptoA + recargo
        elif piso[indice]==8 and tipodepto[indice]=='b' or tipodepto[indice]=='B':
            piso8.insert(1,"X")
            cantidaddeptoB+=1
            totaldeptoB += deptoB
            recargodeptoB += recargo
        elif piso[indice]==8 and tipodepto[indice]=='c' or tipodepto[indice]=='C':
            piso8.insert(2,"X")
            cantidaddeptoC+=1
            totaldeptoC += deptoC
            recargodeptoC += recargo
        elif piso[indice]==8 and tipodepto[indice]=='d' or tipodepto[indice]=='D':
            piso8.insert(3,"X")
            cantidaddeptoD+=1
            totaldeptoD += deptoD
            recargodeptoD += recargo
        elif piso[indice]==9 and tipodepto[indice]=='a' or tipodepto[indice]=='A':
            piso9.insert(0,"X")
            cantidaddeptoA+=1
            totaldeptoA += deptoA
            recargodeptoA= recargodeptoA + recargo
        elif piso[indice]==9 and tipodepto[indice]=='b' or tipodepto[indice]=='B':
            piso9.insert(1,"X")
            cantidaddeptoB+=1 
            totaldeptoB += deptoB
            recargodeptoB += recargo 
        elif piso[indice]==9 and tipodepto[indice]=='c' or tipodepto[indice]=='C':
            piso9.insert(2,"X")
            cantidaddeptoC+=1
            totaldeptoC += deptoC
            recargodeptoC += recargo
        elif piso[indice]==9 and tipodepto[indice]=='d' or tipodepto[indice]=='D':
            piso9.insert(3,"X")
            cantidaddeptoD+=1
            totaldeptoD += deptoD
            recargodeptoD += recargo
        elif piso[indice]==10 and tipodepto[indice]=='a' or tipodepto[indice]=='A':
            piso10.insert(0,"X")
            cantidaddeptoA+=1
            totaldeptoA += deptoA
            recargodeptoA= recargodeptoA + recargo
        elif piso[indice]==10 and tipodepto[indice]=='b' or tipodepto[indice]=='B':
            piso10.insert(1,"X")
            cantidaddeptoB+=1
            totaldeptoB += deptoB
            recargodeptoB += recargo  
        elif piso[indice]==10 and tipodepto[indice]=='c' or tipodepto[indice]=='C':
            piso10.insert(2,"X")
            cantidaddeptoC+=1
            totaldeptoC += deptoC
            recargodeptoC += recargo
        elif piso[indice]==10 and tipodepto[indice]=='d' or tipodepto[indice]=='D':
            piso10.insert(3,"X")
            cantidaddeptoD+=1
            totaldeptoD += deptoD
            recargodeptoD += recargo
        indice += 1
    elif opc==2:
        print("Lista de Departamentos")
        print("")
        print("Los departamentos que estan marcados con una X estan vendidos.")
        print("Piso        Tipo     ")
        print("      A    B    C    D  ")
        print(" 10",piso10)
        print(" 9 ",piso9)
        print(" 8 ",piso8)
        print(" 7 ",piso7)
        print(" 6 ",piso6)
        print(" 5 ",piso5)
        print(" 4 ",piso4)
        print(" 3 ",piso3)
        print(" 2 ",piso2)
        print(" 1 ",piso1)
    elif opc==3:
        print("Lista de compradores por RUT: ")
        print(rut)
    elif opc==4:
        print("Buscando rut...")
        b_rut = input("Ingrese rut a buscar: ")
        Buscar_Rut(b_rut)
    elif opc==5:
        print("Buscando rut...")
        reasignacion_rut = input("Ingrese Rut a buscar")
        Reasignar_Compra(reasignacion_rut)
    elif opc==6:
        repetir=False
        cantidadtotaldeptos= cantidaddeptoA + cantidaddeptoB + cantidaddeptoC + cantidaddeptoD
        totaldeptos= totaldeptoA + totaldeptoB + totaldeptoC + totaldeptoD
        totalrecargos= recargodeptoA + recargodeptoB + recargodeptoC + recargodeptoD
        totaldelostotales= totaldeptos + totalrecargos
        print("")
        print("Tipo de departamento     Cantidad     Total     Recargo por Piso")
        print("Tipo A",deptoA,"UF",cantidaddeptoA,totaldeptoA,"UF",recargodeptoA)
        print("Tipo B",deptoB,"UF",cantidaddeptoB,totaldeptoB,"UF",recargodeptoB)
        print("Tipo C",deptoC,"UF",cantidaddeptoC,totaldeptoC,"UF",recargodeptoC)
        print("Tipo D",deptoD,"UF",cantidaddeptoD,totaldeptoD,"UF",recargodeptoD)
        print("TOTAL             ",cantidadtotaldeptos,totaldeptos,"+",totalrecargos,"=",totaldelostotales)
    


    




        
        

        
