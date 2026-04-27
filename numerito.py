import random


num=random.randint(1,100)
g=int(input("Adivina el numero: "))
pos=1


while pos <5 and g!=num:
    print(f"Turno {pos}")
    if g>num:
        print("Te pasaste")
    else:
        print("El numero a adivinar es mayor")
    g=int(input("Adivina el numero: "))
    pos+=1
if g==num:
    print("Gano")
else:
    print("Peldio. Se te acabaron las oportunidades, el numero a adivinar era: ",num)