def limpa_texto(cad_caracteres):
    """
    Esta função recebe os seguintes parâmetros, e retorna-os
    da seguinte forma:

    cad_caracteres = str
    
    cad_caracteres -> str

    Esta função é utilizada na resolução dos exercícios: 
    1.2.1 e 1.2.3.

    Serve o único propósito de limpar espaços a mais ou 
    afixos como \n. 
    A função assume que todos os argumentos são válidos.
    """
    
    #Separar e juntar novamente com .split() e ' '.join() é o suficiente para 
    #cumprir o objetivo definido.
    cad_caracteres = ' '.join(cad_caracteres.split()) 
    return cad_caracteres

def corta_texto(cad_caracteres, inteiro):
    """
    Esta função recebe os seguintes parâmetros, e retorna-os
    da seguinte forma:

        cad_caracteres = str
        inteiro = int
    
        corta_texto(cad_caracteres, inteiro) -> tuple

    Esta função é utilizada na resolução dos exercícios: 
        1.2.2 e 1.2.4.

    A função recebe uma cadeia de caracteres e um inteiro,
    que representa a largura de coluna desejada. Depois,
    procura uma forma de cortar a cadeia de caracteres
    recebida à largura desejada. Devolve dois elementos
    num tuplo. O primeiro é a parte cortada, que tem largura
    igual ou inferior à desejada. O restante texto integra a 
    segunda cadeia de caracteres, isto é, o segundo
    elemento do tuplo.
    A função assume que todos os argumentos são válidos.
    """
    #Como queremos que a função não corte a string a meio de uma palavra,
    #vai começar por encontrar um local seguro para o fazer, num espaço. Esse espaço deverá ser
    #o primeiro que for encontrado a partir da esquerda.
    if len(cad_caracteres) > inteiro:
        if cad_caracteres[inteiro] != ' ':
            while cad_caracteres[inteiro] != ' ':
                inteiro -= 1
                if inteiro == 0:
                    return cad_caracteres
                elif cad_caracteres[inteiro] == ' ':
                    corte_feito = True
        else:
            corte_feito = True
        
        cad1 = cad_caracteres[0:inteiro] #Podemos realizar o corte, e definir o primeiro elemento.
        if corte_feito == True:
            cad2 = cad_caracteres[(inteiro+1):len(cad_caracteres)] #Segundo elemento.
        else:
            cad2 = ()
        cad_caracteres = (cad1, cad2) #E a junção deles, num tuplo.
        return cad_caracteres
    elif len(cad_caracteres) <= inteiro: #Neste caso, comprimento ideal, mas deve vir em tuplo.
        cad1 = (cad_caracteres,)
        cad2 = ('',)
        return cad1 + cad2

def insere_espacos(cad_caracteres, inteiro):
    """
    Esta função recebe os seguintes parâmetros, e retorna-os
    da seguinte forma:
        cad_caracteres = str
        inteiro = int
        
        insere_espaços(cad_caracteres, inteiro) -> str

    Esta função é utilizada na resolução dos exercícios: 
        1.2.3 e 1.2.4.

    Esta função recebe uma cadeia de caracteres e um número inteiro,
    correspondente à largura de coluna desejada. 
    Se a cadeia de caracteres tiver duas ou mais palavras,
    adiciona espaços entre as palavras da cadeia de caracteres até
    atingir a largura desejada. Caso só tenha uma palavra, fá-lo-á
    no final dessa mesma palavra.
    Adicionalmente, a função calcula o número de espaços por adicionar 
    logo após a entrada dos seus dois argumentos, em vez de se limitar
    a adicionar espaços à medida que é executada até atingir o tamanho desejado.
    Isto só acontece para efeitos de estatística e possível debugging, uma vez
    que, sem a variável em questão, a_adicionar, reflete o número de espaços a adicionar
    (ou adicionados, após o término da execução.) 
    A função assume que todos os argumentos são válidos.
    """
    a_adicionar = inteiro - len(cad_caracteres) #Número de espaços a adicionar. Ler a docstring.
    cad_caracteres = cad_caracteres.split()
    if len(cad_caracteres) == 1: #Há apenas uma palavra.
        while a_adicionar != 0:
            cad_caracteres[0] += ' '
            a_adicionar -= 1
        return str(cad_caracteres[0])
    else:
        while a_adicionar != 0:
            for t in range(len(cad_caracteres[:-1])):
                if a_adicionar != 0: #Podemos chegar ao objetivo dentro do ciclo.
                    cad_caracteres[t] += ' '
                    a_adicionar -= 1
                else: 
                    break
        return ' '.join(cad_caracteres)

def justifica_texto(cad_caracteres, inteiro):
    """
    Esta função recebe os seguintes parâmetros, e retorna-os
    da seguinte forma:
        cad_caracteres = str
        inteiro = int
        
        justifica_texto(cad_caracteres, inteiro) -> tuple

    Esta função é utilizada na resolução dos exercícios: 
        1.2.4.

    Esta função recebe uma cadeia de caracteres e um número inteiro,
    correspondente à largura de coluna desejada. 
    A função começa por limpar o texto da cadeia de caracteres de
    espaços desnecessários e afixos como \n.
    A função também corta o texto de acordo com a largura indicada. 
    Para este efeito, é usada a função corta_texto, que é aplicada
    até a largura ser a mesma para todos os elementos do tuplo. Isto 
    faz com que o tuplo possa ter vários elementos tanto quanto sejam necessários.
    Se a cadeia de caracteres dentro de cada elemento do tuplo
    tiver duas ou mais palavras, adiciona espaços entre as palavras 
    da cadeia de caracteres até atingir a largura desejada. Caso só
    tenha uma palavra, fá-lo-á no final dessa mesma palavra. Para este 
    efeito, é usada a função insere_espaços, utilizada para cada elemento
    do tuplo. Isto garante que a largura é a mesma para todos os elementos.
    
    A função retorna ValueError caso os seus argumentos sejam inválidos,
    isto é, caso as seguintes condições se verifiquem:
        - cad_caracteres não é string ou inteiro não é inteiro;
        - cad_caracteres é uma string vazia;
        - cad_caracteres não permite um corte à largura pretendida, porque não há
          um espaço entre a largura definida e o início da string;
    O ValueError levantado tem a mensagem seguinte:
        "justifica texto: argumentos invalidos"
    """



    if type(cad_caracteres) != str or type(inteiro) != int or len(cad_caracteres) < 1 or ' ' not in cad_caracteres[:inteiro+1] or (len(cad_caracteres) > inteiro and ' ' not in cad_caracteres):
        raise ValueError('justifica_texto: argumentos invalidos')
    
    cad_caracteres = [limpa_texto(cad_caracteres)] #É feita a limpeza do texto a justificar.
    
    #Passamos à fase de corte de texto.
    #Vamos definir para o corte a variável "appendo", que será uma lista, com o primeiro elemento
    #a guardar o texto cortado e o segundo com tudo o resto, e iremos correr
    #a função corta_texto até ao último elemento de appendo não tiver de ser cortado.
    chave = 0 
    i = 0
    while i <= chave:
        if i == 0 and len(cad_caracteres[0]) > inteiro:
            cad_caracteres = list(corta_texto(cad_caracteres[i], inteiro)) #O 2o elemento pode ser muito longo.
            i += 1 
        else:
            if len(cad_caracteres[i]) > inteiro: #Se o último elemento ainda tiver de ser cortado...
                appendo = [list(corta_texto(cad_caracteres[i], inteiro))] #1o cortado, 2o pode ter de ser cortado.
                cad_caracteres[i] = appendo[0][0] #Subsituir o último elemento da lista pelo corte.
                cad_caracteres = cad_caracteres + [appendo[0][1]] #Para o próximo ciclo.
                i+=1 
            else:
                break
        chave = len(cad_caracteres) #Chave aumenta sempre que i aumenta, logo o ciclo não é quebrado.
    
    #A divisão está feita. Começamos a adicionar espaços a todos os elementos que necessitem.
    for i in range(0, len(cad_caracteres) -1): #Não devemos adicionar espaços ao último elemento ainda.
        cad_caracteres[i] = insere_espacos(cad_caracteres[i], inteiro)
    while len(cad_caracteres[-1]) != inteiro: #Vamos adicionar espaços ao último elemento.
        cad_caracteres[-1] += ' '
    return tuple(cad_caracteres) #A cad_caracteres estava em lista e não tem tuplo.

#2

def calcula_quocientes(dic, inteiro):
    """
    Esta função recebe os seguintes parâmetros, e retorna-os
    da seguinte forma:
        dic = dict
        inteiro = int
        
        calcula_quocientes(dic, inteiro) -> dict

    Esta função é utilizada na resolução dos exercícios:
        2.2.1, 2.2.2 e 2.2.4.

    A função recebe um dicionário, com os pares partidos/votos
    de uma determinada região, e calcula os quocientes dos resultados
    obtidos tendo em conta o Método de Hondt.
    A função assume que todos os argumentos são válidos.
    """

    calculado = dic.copy() #Não devemos alterar o dicionário de entrada.
    for key in calculado.keys(): 
        quociente = [float(calculado[key])] #quociente representa o quociente tendo em conta o divisor.
        divisor = 2 # Não é necessário dividir por 1.
        for i in range(inteiro-1): 
            quociente = quociente + [(quociente[0] / divisor)] #quociente[0] é o número de votos obtido.
            divisor += 1
        calculado[key] = quociente #Podemos associar ao dicionário que vamos devolver.
    return calculado

def maiores_quocientes(dic, inteiro):
    """
    Função auxiliar.
    
    Esta função recebe os seguintes parâmetros, e retorna-os
    da seguinte forma:
        dic = dict
        inteiro = int
        
        maiores_quocientes(dic, inteiro) -> list

    Esta função é utilizada na resolução dos exercícios:
        2.2.2 e 2.2.4.

    A função recebe um dicionário com os quocientes dos pares
    partidos/votos de uma determinada região, tendo em conta o método de Hondt,
    e devolve uma lista com os maiores resultados obtidos, por ordem decrescente.
    A função assume que todos os argumentos são válidos.
    """
    lista = list(dic.values()) #Aqui obtemos a lista com listas, que queremos ordenar.
    res = [] #Esta é a lista que iremos devolver.
    for i in lista:
        for e in i:
            if len(res) != inteiro*len(dic.keys()): #Garante que não adicionamos mais valores do que precisamos.
                res.append(e)
            else:
                break
    return sorted(res, reverse=True)

def verifica_duplicado(lista, inteiro):
    """
    Função auxiliar.
    
    Esta função recebe os seguintes parâmetros, e retorna-os
    da seguinte forma:
        lista = list
        inteiro = int
        
        verifica_duplicado(dic, inteiro) -> list

    Esta função é utilizada na resolução dos exercícios:
        2.2.2 e 2.2.4.

    A função recebe um dicionário com os quocientes dos pares
    partidos/votos de uma determinada região, tendo em conta o método de Hondt,
    e devolve uma lista com os maiores resultados obtidos duplicados.
    Se um resultado aparece duas vezes, ele irá aparecer duas vezes na lista.
    A função assume que todos os argumentos são válidos.
    """

    i = [] #Lista onde iremos acrescentar os valores duplicados.
    for v in range(len(lista)):
        ver = lista[v] #Queremos comparar todos os valores da lista com este valor.
        for c in range(inteiro): #A lista tem sempre este comprimento.
            if lista[c] == ver and v != c:
                i = i + [lista[c]]
    return i

def atribui_mandatos(dic, inteiro):
    """
    Esta função recebe os seguintes parâmetros, e retorna-os
    da seguinte forma:
        dic = dict
        inteiro = int
        
        atribui_mandatos(dic, inteiro) -> list

    Esta função é utilizada na resolução dos exercícios:
        2.2.2 e 2.2.4.

    A função recebe um dicionário com quocientes dos pares partidos/votos de uma determinada região, 
    e um inteiro, representando o número de mandatos a atribuir, tendo em conta o método
    de Hondt. A função devolve então uma lista com os mandatos atribuídos, pela ordem definida.
    A função assume que todos os argumentos são válidos.
    """
    quocientes = calcula_quocientes(dic, inteiro)
    lista = maiores_quocientes(quocientes, inteiro) #Ordenamos, numa lista...
    lista = lista[:inteiro+1] #... com comprimento inteiro.
    duplicado = verifica_duplicado(lista, inteiro) #Uma lista com os quocientes duplicados.
    ranking = list(dic.keys()) #De menos para mais votos.
    houve_troca = False #Bubble sorting.
    for l in range(len(ranking)-1, 0, -1):
        for i in range(l):
            if quocientes[ranking[i]][0] > quocientes[ranking[i+1]][0]:
                backup = ranking[i]
                ranking[i] = ranking[i+1]
                ranking[i+1] = backup
                houve_troca = True
        if houve_troca == False:
            break

    mandatos = [] #Esta é a lista que iremos devolver.
    i = 0

    #Vamos ver se os valores de cada quociente pertencem a um partido, e
    #atribuir-lhe um mandato se for o caso. No entanto, existem dois
    #casos dependendo se o quociente aparece mais que uma vez ou não.
    #A forma com que se atribui mandatos a quocientes duplicados
    #garante que mesmo que se encontre o quociente na lista de outro partido,
    #os menos votados recebem o mandato primeiro.
    while i < inteiro: #O i é o número de mandatos atribuídos.
        if lista[i] not in duplicado and len(mandatos) != inteiro:
            for l in range(len(dic)):
                if lista[i] in list(quocientes.values())[l] and len(mandatos) != inteiro:
                    mandatos += [str(list(dic.keys())[l])] #Adicionamos esse partido à lista.
                    i += 1
                    break
        elif lista[i] in duplicado and len(mandatos) != inteiro:
            duplicados = []
            for k in range(len(ranking)): #Pela ordem do ranking (que na verdade é decrescente).
                if lista[i] in quocientes[ranking[k]]:
                    duplicados += [ranking[k]]
            for m in range(len(duplicados)):
                if len(mandatos) < inteiro:
                    mandatos += duplicados[m]
                    i += 1
    return mandatos

def obtem_partidos(dic):
    """
    Esta função recebe os seguintes parâmetros, e retorna-os
    da seguinte forma:
        dic = dict
        
        obtem_partidos(dic) -> list

    Esta função é utilizada na resolução dos exercícios:
        2.2.3 e 2.2.4.

    A função recebe um dicionário com os pares partidos/votos de uma determinada região, 
    e devolve então uma lista com os partidos que participaram nas eleições.
    A função assume que todos os argumentos são válidos.
    """
    
    lista = [] #Esta será a lista que vamos devolver.
    for local in dic.keys():
        participantes = list(dic[local]["votos"].keys()) #Os participantes de cada região.
        for partido in participantes:
            if partido not in lista:
                lista += [partido]
    return sorted(lista) #Retorna a lista organizada por ordem alfabética.

def obtem_resultado_eleicoes(dic):
    """
    Esta função recebe os seguintes parâmetros, e retorna-os
    da seguinte forma:
        dic = dict
        
        obtem_resultado_eleicoes(dic) -> list

    Esta função é utilizada na resolução dos exercícios:
        2.2.4.

    A função recebe um dicionário com os pares partidos/votos de uma determinada região, 
    e devolve então uma lista com os partidos que participaram nas eleições, o numero de 
    mandatos que obtiveram, e o numero de votos totais que receberam nas eleições.
    A função retorna ValueError caso os seus argumentos não sejam válidos.
    """

    lista = list() #Lista vazia.
    resultados = dict() #Dicionário vazio.
    if type(dic) != dict or len(dic) == 0:
        raise ValueError('obtem_resultado_eleicoes: argumento invalido')
    else:
        for local in list(dic.keys()):
            if type(dic[local]) != dict or type(local) != str or len(local) == 0\
                or "deputados" not in list(dic[local].keys()) or "votos" not in list(dic[local].keys()) or len(dic[local].keys()) != 2 \
                or type(dic[local]["deputados"]) != int or type(dic[local]["votos"]) != dict\
                or dic[local]["deputados"] <= 0 or len(dic[local]["votos"]) <= 0\
                or len(list(dic[local]["votos"].keys())) != len(list(dic[local]["votos"].values())):
                    raise ValueError('obtem_resultado_eleicoes: argumento invalido')
            else:
                for partido in list(dic[local]["votos"].keys()):
                    if type(partido) != str or type(dic[local]["votos"][partido]) != int\
                        or dic[local]["votos"][partido] < 0 or len(partido) == 0:
                        raise ValueError('obtem_resultado_eleicoes: argumento invalido')
                    for resultado in list(dic[local]["votos"].values()):
                        if type(resultado) == int and resultado <= 0:
                            raise ValueError('obtem_resultado_eleicoes: argumento invalido')

    info = obtem_partidos(dic) #Nome dos partidos que participaram nas eleições.
    for partido in info:
        resultados[partido] = [str(partido), 0, 0] #"Ficha" do partido, que começa a 0s.
    for local in list(dic.keys()):
        mandatos_locais = atribui_mandatos(dic[local]["votos"], dic[local]["deputados"])
        for resultado in mandatos_locais:
                resultados[resultado][1] += 1 #Adicionar à ficha de cada vencedor.
        for i in list(resultados.keys()):
            if i in dic[local]["votos"]:
                resultados[i][2] += dic[local]["votos"][i] #Com os votos, a mesma coisa.
    for partidos in list(resultados.keys()):
        lista = lista + [tuple(resultados[partidos])] #As fichas para a lista vazia em tuplos.
    
     #Agora, resta-nos ordenar pela quantidade de mandatos. Se ele for o mesmo,
     #fazemo-lo pelo número de votos. Iremos usar o bubble sorting.
    houve_troca = False
    for l in range(len(info)-1, 0, -1):
        for k in range(l):
            if lista[k][1] < lista[k+1][1]:
                backup = lista[k]
                lista[k] = lista[k+1]
                lista[k+1] = backup
                houve_troca = True
            elif lista[k][1] == lista[k+1][1] and lista[k][2] < lista[k+1][2]:
                backup = lista[k]
                lista[k] = lista[k+1]
                lista[k+1] = backup
                houve_troca = True
        if houve_troca == False:
            break
    return lista

#3
def produto_interno(um, dois):
    """
    Esta função recebe os seguintes parâmetros, e retorna-os
    da seguinte forma:
        um = tuple
        dois = tuple
        
        produto_interno(um, dois) -> float

    Esta função é utilizada na resolução dos exercícios:
        3.2.1 e 3.2.5

    A função recebe dois tuplos, cada um representando um vetor.
    Devolve então um real, representando o produto interno desses dois vetores.
    A função assume que todos os seus argumentos são válidos.
    """
    real = float(0)
    for i in range(len(um)):
        real += float((um[i] * dois[i]))
    return float(real)

def verifica_convergencia(linhas, constantes, x, real):
    """
    Esta função recebe os seguintes parâmetros, e retorna-os
    da seguinte forma:
        linhas = tuple
        constantes = tuple
        x = tuple
        real = float
        
        verifica_convergencia(linhas, constantes, x, real) -> bool

    Esta função é utilizada na resolução dos exercícios:
        3.2.2 e 3.2.5

    A função recebe três tuplos, um representando as linhas da matriz dos coeficientes,
    outro representando as constantes da matriz, e outro representando o vetor dos 
    coeficientes.
    A função devolve um valor bool, dependendo do erro comparado com o real fornecido.
    True, se o valor for inferior ao real, e False se não for.
    A função assume que todos os seus argumentos são válidos.
    """
    a_verificar = []
    for i in range(len(linhas)):
        a_verificar += [abs(produto_interno(linhas[i], x) - constantes[i])] #Erro para todas as variáveis.
    for num in a_verificar: #Vamos avaliar cada uma delas.
        if num >= real:
            return False #Para uma das linhas, o erro ainda é superior ao real.
    return True    

def retira_zeros_diagonal(um, dois):
    """
    Esta função recebe os seguintes parâmetros, e retorna-os
    da seguinte forma:
        um = tuple
        dois = tuple
        
        retira_zeros_diagonal(um, dois) -> tuple, tuple

    Esta função é utilizada na resolução dos exercícios:
        3.2.3 e 3.2.5

    A função recebe dois tuplos, um representando as linhas de uma matriz,
    e outro representando o vetor das constantes dessa matriz.
    A função devolve então esses dois vetores, mas de forma a que não se encontrem
    zeros na diagonal dessa matriz.
    A função assume que todos os seus argumentos são válidos.
    """
    um, dois = list(um), list(dois) #Passamos os dois tuplos a listas, para facilitar.
    for i in range(len(um[0])):
        if um[i][i] == 0:
            for j in range(len(um)):
                if um[j][i] != 0 and um[i][j] != 0:
                    um[i], um[j] = um[j], um[i]
                    dois[i], dois[j] = dois[j], dois[i]
                    break
    return tuple(um), tuple(dois)

def eh_diagonal_dominante(um):
    """
    Esta função recebe os seguintes parâmetros, e retorna-os
    da seguinte forma:
        um = tuple
        
        eh_diagonal_dominante(um) -> bool

    Esta função é utilizada na resolução dos exercícios:
        3.2.4 e 3.2.5

    A função recebe um tuplo, representando uma matriz.
    Devolve então um valor bool, caso a soma do valor absoluto dos 
    valores de cada linha sejam menores que o valor absoluto da diagonal
    ou não. Devolve True se sim, e False se não.
    A função assume que todos os seus argumentos são válidos.
    """
    
    #Calcularemos a soma da seguinte forma:
    #Se estivermos na primeira linha, somamos todos os restantes elementos.
    #Se estivermos numa linha intermédia, dividimos em dois na diagonal, e somamos os elementos dessas metades.
    #Se estivermos na última linha, somamos todas as entradas da linha menos a última.
    for i in range(len(um)):
        soma = 0
        if i == 0:
            for l in range(i+1, len(um)):
                soma += abs(um[i][l])
        elif 0 < i < len(um):
            m1 = um[i][:i]
            m2 = um[i][i+1:]
            for j in range(len(m1)):
                soma += abs(m1[j])
            for k in range(len(m2)):
                soma += abs(m2[k])
        elif i == len(um):
            for m in range(len(um) -1):
                soma += abs(um[i][m])
        if abs(um[i][i]) < soma:
            return False 
    return True

def resolve_sistema(linhas, constantes, real):
    """
    Esta função recebe os seguintes parâmetros, e retorna-os
    da seguinte forma:
        linhas = tuple
        constantes = tuple
        real = float
        
        resolve_sistema(linhas, constantes, real) -> tuple

    Esta função é utilizada na resolução dos exercícios:
        3.2.5.

    A função recebe dois tuplos, um representando as linhas da matriz, e outro
    representando o vetor das constantes. Também recebe um real que representa
    o erro desejado para a aplicação do método iterativo de Jacobi.
    Devolve então um tuplo, com as estimativas finais, após o erro ser menor
    para cada uma delas.
    A função retorna ValueError caso os seus argumentos não sejam válidos, ou
    caso a matriz náo seja diagonal dominante.
    """

    #Começamos pelo levantamento de erros.
    if type(linhas) != tuple or type(constantes) != tuple or type(real) != float\
        or (type(real) == float and real <= 0) or (type(linhas) == tuple and len(linhas)) == 0\
        or len(constantes) == 0 or len(constantes) != len(linhas):
        raise ValueError('resolve_sistema: argumentos invalidos')
    else:
        for tuplo in range(len(linhas)):
            if len(linhas) == 0 or type(linhas[tuplo]) != tuple\
                or len(linhas[tuplo]) != len(linhas):
                raise ValueError('resolve_sistema: argumentos invalidos')
            else:
                for elemento in linhas[tuplo]:
                    if (type(elemento) != int and type(elemento) != float):
                        raise ValueError('resolve_sistema: argumentos invalidos')        
        for constante in constantes:
            if (type(constante) != int and type(constante) != float):
                raise ValueError('resolve_sistema: argumentos invalidos')
    correcao = retira_zeros_diagonal(linhas, constantes) #É necessário fazer uma pequena correção à matriz, agora que sabemos que é válida, antes de vermos se é diagonal dominante.
    linhas = correcao[0]
    constantes = correcao[1]
    if eh_diagonal_dominante(linhas) == False:
        raise ValueError('resolve_sistema: matriz nao diagonal dominante')
    for i in range(len(linhas)):
        if linhas[i][i] == 0: #Se uma das
            raise ValueError('resolve_sistema: matriz nao diagonal dominante')
    
    #Agora que temos a certeza que podemos prosseguir, 
    #já que todos os argumentos são válidos e que a matriz é diagonal dominante, 
    #vamos estimar soluções.
    #Vamos criar uma espécie de tabela, em que "resultado" será
    #a linha da estimativa que está a ser calculada. Quando terminarmos,
    #atualizamos "vetor" esses valores.
    x = float(0) #A estimativa inicial é 0.
    vetor = (x,) * len(linhas) #O vetor aqui torna-se (0, 0, ..., 0), comprimento das linhas.
    resultado = [x] * len(linhas) #Ficamos com um vetor de comprimento igual ao número de linhas.
    while verifica_convergencia(linhas, constantes, vetor, real) != True:
        for i in range(len(linhas)):
            resultado[i] = float(float(vetor[i]) + (float(constantes[i]) - float(produto_interno(linhas[i], vetor)))/float(linhas[i][i]))
        vetor = tuple(resultado)
    return tuple(vetor) #O resultado tem de vir em tuplo.
            




            










