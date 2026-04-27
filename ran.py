import random
import time

p1=input("Ingrese el nombre del primer peleador: ")
p2=input("Ingrese el nombre del segundo peleador: ")

v1=100
v2=100
turno=random.randint(1,2)
 
while v1>0 and v2>0:
    if turno %2==0:                            #Turno entre dos jugadores
        print("Turno de: ",p1)
        atk=random.randint(7,18)
        print(f"El {p1} ataca con: {atk}")
        v2-=atk
        print(f"El hp de {p2} es {v2}")
        time.sleep(1)
    else:                                          
        print(f"Turno de : {p2}")
        atk=random.randint(7,18)
        print(f"El {p2} ataca con: {atk}")
        v1-=atk
        print(f"El hp de {p1} es {v1}")
        time.sleep(1)
    turno+=1
    print(p1, "█"*v1)
    print(p2, "█"*v2)
    time.sleep(2)

if v1 > v2:
    print(f"Ha ganado {p1}")
else:
    print(f"Ha ganado {p2}")

    

    
