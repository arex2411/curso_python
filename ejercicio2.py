def letras_unicas(palabra):
    lista = list(palabra)
    # convertimos la lista a un set para eliminar los duplicados
    s = set(lista)
    lista = list(s)
    lista.sort()
    return lista

palabra = "multidimencional"


print(letras_unicas(palabra))
