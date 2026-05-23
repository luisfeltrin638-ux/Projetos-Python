# Não adaptado para classificar adequadamente strings ou retornar a lista em classficação invertida
def bolha(lista):
    nao_classificados = len(lista)
    i = 0
    i_antigo = i
    verificacao_organizado = 0

    while i < nao_classificados:

        verificacao_organizado = 0
        j = i + 1 

        while j < nao_classificados:
            
            if lista[i] <= lista[j]:
                i = j # o índice "i" é sempre o anterior do índice "j"

            else:
                menor = lista[j]

                lista[j] = lista[i]
                lista[i] = menor

                i = j

                verificacao_organizado += 1
            j += 1
 
        i = i_antigo # correção da variável "i" pelo backup "i_antigo".
        nao_classificados -= 1 # quantia de não classificados decresce em 1.

        if verificacao_organizado == 0: # verificação se houve troca de elementos na lista, pois o método consegue identificar se a lista já está classificada.
            i = nao_classificados

    return lista