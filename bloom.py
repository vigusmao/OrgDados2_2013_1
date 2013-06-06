from random import randint

min_chave = 10**6
max_chave = 10**7 - 1

n = 1000
m = 30000
t = 21
n_consultas = 5000


def h(i, chave): 
    return chave**i % m

def obtem_assinatura(chave):
    assinatura = [0] * m
    for i in range(1, t+1):
        indice_bit = h(i, chave)
        assinatura[indice_bit] = 1
    return assinatura

def or_listas(target, source):
    for i in range(len(source)):
        target[i] = target[i] or source[i]      

def verifica_chave_bloom(chave, filtro):
    assinatura_chave = obtem_assinatura(chave)
    for i in range(m):
        if assinatura_chave[i] and not filtro[i]:
            return False
    return True
        



listanegra = set()

bloom_filter = [0] * m

while len(listanegra) < n:
    nova_chave = randint(min_chave, max_chave)
    listanegra.add(nova_chave)
    assinatura = obtem_assinatura(nova_chave)
    or_listas(bloom_filter, assinatura)
    

cont_1s = 0
for bit in bloom_filter:
    cont_1s += bit
print("cont1s = %d" % cont_1s)


n_buscas_lentas = 0
n_falsos_positivos = 0

for i in range(n_consultas):
    chave_busca = randint(min_chave, max_chave)
    if verifica_chave_bloom(chave_busca, bloom_filter):
        n_buscas_lentas += 1
        if chave_busca not in listanegra:
            n_falsos_positivos += 1


print("n_consultas = %d" % n_consultas)
print("n_buscas_lentas = %d" % n_buscas_lentas)
print("n_falsos_positivos = %d" % n_falsos_positivos)

            
            




    
    
