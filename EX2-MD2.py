def remover_duplicatas(itens):
    vistos = set()
    resultado = []
    for item in itens:
        if item not in vistos:
            vistos.add(item)
            resultado.append(item)
    return resultado

lista = [3,2,1,12,12,1,2,2,3,2,1]
print(remover_duplicatas(lista))