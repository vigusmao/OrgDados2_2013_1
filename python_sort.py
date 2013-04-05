from time import time

tamanho = 8
lista = [None]*10**tamanho
print("lista alocada")

for i in range(10**tamanho):
    lista[i] = i
print("lista criada")

inicio = time()
x = sorted(lista)
fim = time()

print("tamanho = %d" % tamanho)
print(x[0])
print("%.5f segundos" % (fim - inicio))




