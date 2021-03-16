print ("----------Bem-Vindo(a) ao jogo de adivinhação:)----------")

numero_secreto = 666

chute_str = input("Digite um numero: ")

print("Voce digitou: " , chute_str)

chute = int(chute_str)


if(numero_secreto == chute):
     print("voce acertoou!!!! :))")
else:

     print("Voce errou!!! :((((")

print("----------FIM DE JOGO----------")


