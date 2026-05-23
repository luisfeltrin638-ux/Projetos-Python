# Não adaptado para classificar adequadamente strings ou retornar a lista em classficação invertida
def insercao(lista):
    valor_atual = 0

    for i in range(1, len(lista)):
        valor_atual = lista[i]
        j = i - 1
        
        while j >= 0 and lista[j] > valor_atual:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = valor_atual
        
    return lista