# Faça um Programa que leia um lista de 10 números reais e mostre-os na ordem inversa.

lista = []

for i in range (10):
    num = float(input("Digite um número: "))
    lista.append(num)
lista.sort(reverse= True)
print(lista)