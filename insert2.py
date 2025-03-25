import sys
# Array exemplo
Array = [6, 1, 4, 7, 0]
# encontrando o tamanho
alt = len(Array)

# função de troca


def troca(Array, a):
    # tmp é uma variavel temporaria para permitir a troca
    tmp = Array[a]
    Array[a] = Array[a+1]
    Array[a+1] = tmp


def classificação(Array, alt):
    # verifica se troca ocorreu
    troca_ocorreu = False
    # loop de a em todo o array medido por alt
    for a in range(alt-1):
        # se um elemento é maior que o seu posterior
        if Array[a] > Array[a+1]:
            # efetua a troca
            troca(Array, a)
            # marque verdadeiro para troca_ocorreu
            troca_ocorreu = True
    # se troca ocorreu continue recursão até a troca não mais ocorrer
    if troca_ocorreu:
        classificação(Array, alt)


classificação(Array, alt)
print(Array)
