import random


num=random.randint(1,100)
g=int(input("Adivina el numero: "))
pos=1

while g<1 or g >100:
    print("Numero fuera de rango, intente nuevamente")

    while pos <5 and g!=num:
        g=int(input("Adivina el numero: "))
        print(f"Turno {pos}")
        if g>num:
            print("Te pasaste")
        else:
            print("El numero a adivinar es mayor")
        g=int(input("Adivina el numero: "))
        while g<=1 and g >=100:
            print("Numero fuera de rango, intente nuevamente")
        pos+=1
    if g==num:
        print("Gano")
    else:
        print("Peldio. Se te acabaron las oportunidades, el numero a adivinar era: ",num)