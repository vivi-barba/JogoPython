import random

print("----------Bem-Vindo(a) ao jogo de adivinhação :)----------")

numero_secreto = random.randint(0, 100)
maiorQueCem = 101
chute_str = input("Digite um número de 0 a 100: ")

chute = int(chute_str)

if chute > maiorQueCem:
   print("Ops. O número precisa ser menor ou igual a 100. ;)")
elif chute < 0:
   print("Ops. O número precisa ser maior ou igual a 0. ;)")
else:
   print("Você digitou:", chute)

print("O número secreto é", numero_secreto)

if numero_secreto == chute:
    print("Você acertou!!!! :))")
else:
    print("Você errou!!! :((((")

print("----------FIM DE JOGO----------")


