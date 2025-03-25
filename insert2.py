import sys

Array = [6, 1, 4, 7, 0]
alt = len(Array)


def troca(Array, a):
    tmp = Array[a]
    Array[a] = Array[a+1]
    Array[a+1] = tmp


def classificação(Array, alt):

    troca_ocorreu = False

    for a in range(alt-1):
        if Array[a] > Array[a+1]:
            troca(Array, a)
            troca_ocorreu = True

    if troca_ocorreu:
        classificação(Array, alt)


classificação(Array, alt)
print(Array)
