def contar_primos(numero):
    cont = 0
    for i in range(numero):
        if es_primo(i+1):
            cont = cont + 1
    return cont


def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True




        

numero = 11
print(contar_primos(numero))



