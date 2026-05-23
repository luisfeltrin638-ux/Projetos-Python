def insercao(lista):
    valor_atual = 0
    for i in range(1, len(lista)):
        valor_atual = lista[i]
        decremento = i - 1
        
        while decremento >= 0 and lista[decremento] > valor_atual:
            lista[decremento + 1] = lista[decremento]
            decremento -= 1
        lista[decremento + 1] = valor_atual
        
    return lista