def soma_il(lst):
    soma = 0
    for i in range(len(lst)):
        soma += lst[i]
    return soma

def soma_rl(lista):
        if len(lista )== 0:
            return 0
        else:
            return lista[0] + soma_rl(lista[1:])

def soma_rc(lst):
    def aux(lst, res):
        if len(lst) == 0:
            return res
        else:
            return aux(lst[1:], res + lst[0])

