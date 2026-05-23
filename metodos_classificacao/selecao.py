# Não adaptado para classificar adequadamente strings ou retornar a lista em classficação invertida
def selecao(lista):
    
    for i in range(len(lista)):
        j = i + 1

        while j < len(lista):

            if lista[i] > lista[j]:
                
                menor = lista[j]

                lista[j] = lista[i]
                lista[i] = menor
            j += 1

    return lista