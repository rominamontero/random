import random


num=random.randint(1,100)
g=int(input("Adivina el numero: "))



while num != g:
    if g>num:
        print("Te pasaste")
    else:
        print("El numero a adivinar es mayor")
    g=int(input("Adivina el numero: "))
print("Has adivinado")