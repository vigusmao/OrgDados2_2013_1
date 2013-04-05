##
## Comparativo de algoritmos de busca em listas ordenadas.
##
## As funcoes de busca estao retornando o numero de acessos as estruturas.
## Para retornar de fato o resultado da busca (indice da chave buscada, ou -1
## caso a chave nao se encontre), troque as linhas com 'return' pelas linhas
## comentadas imediatamente acima de cada uma delas.
##
## UFRJ, 2 de abril de 2013.
##


from random import randint
from time import time


TAMANHO = 10000000
MAX = 1000000
MAX_PASSO = 1
N_BUSCAS = 10000


def busca_binaria(valor, lista):

    esquerda = 0
    direita = len(lista) - 1

    acessos = 0

    while esquerda <= direita:
        indice = (esquerda + direita)//2
        
        elemento = lista[indice]
        acessos += 1

        if elemento == valor:
            ##return indice 
            return acessos
        if elemento < valor:
            esquerda = indice + 1
        else:
            direita = indice - 1

    ##return -1
    return acessos
        
        
def busca_interpolada(valor, lista):

    esquerda = 0
    direita = len(lista) - 1

    minimo = lista[esquerda]
    maximo = lista[direita]
    acessos = 2
        
    while minimo <= valor <= maximo:

        if minimo == maximo: # evitando divisao por zero na interpolacao
            indice = esquerda
        else:
            # interpolacao
            indice = esquerda + (valor - minimo)*(direita - esquerda)//(maximo - minimo)
            
        elemento = lista[indice]
        acessos += 1

        if elemento == valor:
            ##return indice
            return acessos
        if elemento < valor:
            esquerda = indice + 1
            minimo = lista[esquerda]
            acessos += 1
        else:
            direita = indice - 1
            maximo = lista[direita]
            acessos += 1

    ##return -1
    return acessos


def avaliar_busca(funcao, nome_funcao, lista):

    total_acessos = 0

    tempo_inicial = time()
    for i in range(N_BUSCAS):
        chave = randint(1,lista[-1])
        # chave = 2000
        total_acessos += funcao(chave, lista)

    media_acessos = total_acessos / N_BUSCAS

    print("\n%s ---> %.2f acessos (%.5f segundos)" % (nome_funcao,
                                                      media_acessos,
                                                      time() - tempo_inicial))

# main
                                                      
tempo_inicial = time()

conjunto = set()
for i in range(TAMANHO):
    x = randint(1,MAX)
    conjunto.add(x)
lista = sorted(list(conjunto))

##ultimo = 1
##lista = [1]
##for i in range(TAMANHO-1):
##    ultimo += randint(1, MAX_PASSO)
##    lista += [ultimo]
##lista += [TAMANHO**2]
print("\nlista gerada em %.5f segundos" % (time() - tempo_inicial))


avaliar_busca(busca_binaria, "busca binaria", lista)
avaliar_busca(busca_interpolada, "busca interpolada", lista)
    
