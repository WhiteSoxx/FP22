"""
TAD Gerador

[b, s]
b = bits (int, 32 ou 64)
s = seed (int)

A representação escolhida foi a de uma lista, com o
primeiro elemento da lista a representar os bits, e o
segundo a seed ou estado do gerador.
"""

def cria_gerador(b, s):
    """
    Construtor do TAD gerador.
    cria_gerador(b, s) -> gerador (list)
    b = bits (int)
    s = seed (int)

    Devolve um gerador.
    """
    if not isinstance(b, int) or not isinstance(s, int)\
    or b not in [32, 64] or s <= 0\
    or (b == 32 and s > 2**(32) - 1) or (b == 64 and s > 2**(64) - 1): #se não respeitar o integer limit
            raise ValueError('cria_gerador: argumentos invalidos')
    return [b, s]

def cria_copia_gerador(g):
    """
    Construtor do TAD gerador.
    cria_copia_gerador(g) -> list
    g = gerador (list)

    Devolve uma shallow copy do gerador.
    """
    return g.copy()

def obtem_estado(g):
    """
    Seletor do TAD gerador.
    obtem_estado(g) -> int
    g = gerador (list)

    Devolve o estado do gerador.
    """
    return g[1]

def define_estado(g, s):
    """
    Modificador do TAD gerador.
    define_estado(g, s) -> int
    g = gerador (list)
    s = seed (int)

    Modifica destrutivamente o estado de g, substituindo por s,
    e devolve s.
    """
    g[1] = s
    return s

def atualiza_estado(g):
    """
    Modificador do TAD gerador.
    atualiza_estado(g) -> int
    g = gerador (list)

    Modifica destrutivamente o estado de g com um
    inteiro pseudoaleatório obtido através do método
    xorshift do estado anterior, e devolve o novo estado.
    """
    if g[0] == 32:
        s = g[1]
        s ^= (s << 13) & 0xFFFFFFFF
        s ^= (s >> 17) & 0xFFFFFFFF
        s ^= (s << 5) & 0xFFFFFFFF
    elif g[0] == 64:
        s = g[1]
        s ^= (s << 13) & 0xFFFFFFFFFFFFFFFF
        s ^= (s >> 7) & 0xFFFFFFFFFFFFFFFF
        s ^= (s << 17) & 0xFFFFFFFFFFFFFFFF
    define_estado(g, s)
    return s

def eh_gerador(arg):
    """
    Reconhecedor do TAD gerador.
    eh_gerador(arg) -> bool
    arg = any

    Devolve True se o argumento representa um gerador, 
    e False caso contrário.
    """
    try:
        cria_gerador(arg[0], arg[1])
    except:
        return False
    if type(arg) == list and len(arg) == 2 and isinstance(arg[0], int)\
    and arg[0] == 32 or arg [0] == 64 and isinstance(arg[1], int) and arg[1] > 0 and\
    (arg[0] == 32 and arg[1] <= 2**(32) - 1) or (arg[0] == 64 and arg[1] <= 2**(64) - 1): #integer limit
        return True
    return False

def geradores_iguais(g1, g2):
    """
    Teste do TAD gerador.
    geradores_iguais(g1, g2) -> bool
    g1, g2 = any, any

    Devolve True se os dois geradores fornecidos forem
    geradores e iguais, e False caso uma destas condições
    não se verifique.
    """
    if eh_gerador(g1) and eh_gerador(g2)\
    and g1[0] == g2[0] and g1[1] == g2[1]:
        return True
    return False

def gerador_para_str(g):
    """
    Transformador do TAD gerador.
    gerador_para_str(g) -> str
    g = gerador (list)

    Recebe um gerador, e devolve o equivalente em string.
    """
    return 'xorshift{}(s={})'.format(g[0], g[1]) 

def gera_numero_aleatorio(g, n):
    """
    Função de alto nível associada ao TAD gerador.
    gera_numero_aleatorio(g, n) -> int
    g = gerador (list)
    n = numero (int)

    Atualiza o estado do gerador, e devolve um número aleatório
    do intervalo [1, n], obtido com recurso ao estado de s.
    """
    g[1] = atualiza_estado(g)
    numero = 1 + (g[1] % n)
    return numero

def gera_carater_aleatorio(g, str):
    """
    Função de alto nível associada ao TAD gerador.
    gera_carater_aleatorio(g, str) -> str
    g = gerador (list)
    str = string (str)

    Atualiza o estado do gerador, e devolve um caráter aleatório
    do intervalo de letras entre A e str, obtido com recurso ao estado de s.
    """
    g[1] = atualiza_estado(g)
    lista = []
    for i in range(ord('A'), ord(str)+1):
        lista += chr(i)
    return lista[(g[1] % len(lista))] #posição da lista.


"""
TAD Coordenada:

(c, l)
c = coluna (str, entre A a Z)
l = linha (int, entre 1 e 99)

A representação escolhida foi a de um tuplo, com o primeiro
elemento a representar a coluna e o segundo a linha.
"""

def cria_coordenada(col, lin):
    """
    Construtor do TAD coordenada.
    cria_coordenada(col, lin) -> coordenada (tuple)
    col = coluna (str)
    lin = linha (int)

    Cria uma coordenada, em tuplo, através dos dados fornecidos.
    Devolve ValueError em casos inválidos.
    """
    if isinstance(col, str) and isinstance(lin, int)\
    and len(col) == 1 and ord('A') <= ord(col) <= ord('Z')\
    and 1 <= lin <= 99:
        return (col, lin)
    raise ValueError('cria_coordenada: argumentos invalidos')

def obtem_coluna(c):
    """
    Seletor do TAD coordenada.
    obtem_coluna(c) -> str
    c = coordenada (tuple)

    Devolve a coluna da coordenada c.
    """
    return c[0]

def obtem_linha(c):
    """
    Seletor do TAD coordenada.
    obtem_linha(c) -> int
    c = coordenada (tuple)

    Devolve a linha da coordenada c.
    """
    return c[1]

def eh_coordenada(arg):
    """
    Reconhecedor do TAD coordenada.
    eh_coordenada(arg) -> bool
    arg = any

    Devolve True se arg representa uma coordenada
    válida, e False caso contrário.
    """
    try:
        cria_coordenada(arg[0], arg[1])
    except:
        return False
    if isinstance(arg, tuple) and len(arg) == 2\
    and isinstance(arg[0], str) and isinstance(arg[1], int)\
    and ord('A') <= ord(arg[0]) <= ord('Z') and 0 < arg[1] < 100:
        return True
    return False

def coordenadas_iguais(c1, c2):
    """
    Teste do TAD coordenada.
    coordenadas_iguais(c1, c2) -> bool
    c1, c2 = coordenada (tuple)

    Devolve True se c1 e c2 são coordenadas válidas e iguais,
    e False caso uma das condições não se verifique.
    """
    if eh_coordenada(c1) and eh_coordenada(c2)\
    and c1[0] == c2[0] and c1[1] == c2[1]:
        return True
    return False

def coordenada_para_str(c):
    """
    Transformador do TAD coordenada.
    coordenada_para_str(c) -> str
    c = coordenada (tuple)

    Devolve o equivalente à coordenada c em string.
    """
    return c[0] + str((c[1] // 10)) + str(c[1] % 10) 
    #Calcula-se os dois digitos em separado para garantir que é 0 se linha < 10.

def str_para_coordenada(s):
    """
    Transformador do TAD coordenada.
    str_para_coordenada(s) -> tuple
    s = str

    Devolve o equivalente à string s em coordenada (tuplo),
    assumindo que representa um conjunto de coordenadas válido.
    """
    if int(s[1:]) >= 10:
        return (s[0], int(s[1:]))
    else:
        return (s[0], int(s[-1]))
    #Mais uma vez, para interpretar o 0 de forma diferente se linha < 10.

def obtem_coordenadas_vizinhas(c):
    """
    Função de alto nível associada ao TAD coordenada.
    obtem_coordenadas_vizinhas(c) -> tuple
    c = coordenada (tuple)
    
    Devolve um tuplo com as coordenadas (também tuplos) vizinhas
    da coordenada argumento, por ordem, começando do canto superior esquerdo,
    sempre que possível, e existentes.
    """
    vizinhas = ()
    ha_espaço_a_esquerda, ha_espaço_em_cima, ha_espaço_a_direita, ha_espaço_em_baixo\
        = False, False, False, False #Para computar vizinhas que realmente existam...
    #Vamos ver onde há espaço.
    if ord(obtem_coluna(c)) - 1 >= ord('A'):
        ha_espaço_a_esquerda = True
        coluna_esquerda = chr(ord(obtem_coluna(c)) - 1)
    if obtem_linha(c) - 1 >= 1:
        ha_espaço_em_cima = True
        linha_em_cima = obtem_linha(c) - 1
    if ord(obtem_coluna(c)) + 1 <= ord('Z'):
        ha_espaço_a_direita = True
        coluna_direita = chr(ord(obtem_coluna(c)) + 1)
    if obtem_linha(c) + 1 <= 99:
        ha_espaço_em_baixo = True
        linha_em_baixo = obtem_linha(c) + 1
    #E seguimos por ordem.
    if ha_espaço_em_cima:
        if ha_espaço_a_esquerda:
            vizinhas += (cria_coordenada(coluna_esquerda, linha_em_cima),)
        vizinhas += (cria_coordenada(obtem_coluna(c), linha_em_cima),)
    if ha_espaço_a_direita:
        if ha_espaço_em_cima:
            vizinhas += (cria_coordenada(coluna_direita, linha_em_cima),)
        vizinhas += (cria_coordenada(coluna_direita, obtem_linha(c)),)
    if ha_espaço_em_baixo:
        if ha_espaço_a_direita:
            vizinhas += (cria_coordenada(coluna_direita, linha_em_baixo),)
        vizinhas += (cria_coordenada(obtem_coluna(c), linha_em_baixo),)
    if ha_espaço_a_esquerda:
        if ha_espaço_em_baixo:
            vizinhas += (cria_coordenada(coluna_esquerda, linha_em_baixo),)
        vizinhas += (cria_coordenada(coluna_esquerda, obtem_linha(c)),)
    return vizinhas
            
def obtem_coordenada_aleatoria(c, g):
    """
    Função de alto nível associada ao TAD coordenada.
    obtem_coordenada_aleatoria(c, g) -> tuple
    c = coordenada (tuple)
    g = gerador (list)
    
    Com recurso às funções que geram caracteres e números aleatórios,
    cria uma coordenada aleatória, começando pela coluna e depois pela
    linja, nunca mais para a direita ou para baixo da coordenada c.
    """
    return cria_coordenada(gera_carater_aleatorio(g, obtem_coluna(c)), gera_numero_aleatorio(g, obtem_linha(c))) 


"""
TAD Parcela:

{'estado': tapada/marcada/limpa, 'minada': True/False, 'numero': ' '/num}

A representação escolhida foi a de um dicionário, de chaves:
- 'estado' representa os estados possíveis, tapada, marcada e limpa;
- 'minada' representa um bool, indicando se há uma mina ou não;
- 'numero' foi adicionado posteriormente, e indica o numero de minas vizinhas, em str.
    É representado por um espaço se for 0.
"""

def cria_parcela():
    """
    Construtor do TAD parcela.
    cria_parcela() -> parcela (dict)
    
    Cria um dicionário que guarda as informações relevantes
    à parcela.
    """
    return {'estado': 'tapada', 'minada': False, 'numero': ' '}

def cria_copia_parcela(p):
    """
    Construtor do TAD parcela.
    cria_copia_parcela(p) -> parcela (dict)
    p = parcela (dict)

    Cria uma shallow copy do dicionário parcela.
    """
    return p.copy()

def numero_em_str(p):
    """
    Função auxiliar, seletor do TAD parcela.
    numero_em_str(p) -> str
    p = parcela (dict)

    Devolve a str que presenta o número de minas vizinhas da parcela.
    """
    return p['numero']

def limpa_parcela(p):
    """
    Modificador do TAD parcela.
    limpa_parcela(p) -> parcela (dict)
    p = parcela (dict)
    
    Modifica destrutivamente o estado de p para limpa, 
    e devolve p.
    """
    p['estado'] = 'limpa'
    return p

def marca_parcela(p):
    """Modificador do TAD parcela.
    limpa_parcela(p) -> parcela (dict)
    p = parcela (dict)
    
    Modifica destrutivamente o estado 
    de p para marcada, e devolve p.
    """
    p['estado'] = 'marcada'
    return p

def desmarca_parcela(p):
    """Modificador do TAD parcela.
    limpa_parcela(p) -> parcela (dict)
    p = parcela (dict)
    
    Modifica destrutivamente o estado 
    de p para tapada, e devolve p.
    """
    p['estado'] = 'tapada'
    return p

def esconde_mina(p):
    """Modificador do TAD parcela.
    limpa_parcela(p) -> parcela (dict)
    p = parcela (dict)
    
    Modifica destrutivamente o valor de 
    'minada' para True, e devolve p.
    """
    p['minada'] = True
    return p

def altera_numero_minas_vizinhas(p, n):
    """
    Função auxiliar, modificador do TAD parcela.
    alterna_numero_minas_vizinhas(p, n) -> parcela (dict)
    p = parcela (dict)
    n = numero de minas (int)
    """
    if n > 0:
        p['numero'] = str(n)
    else: 
        p['numero'] = ' ' #Como descrito na assinatura do TAD, 0 é representado por um espaço.
    return p

def eh_parcela(arg):
    """
    Reconhecedor do TAD parcela.
    eh_parcela(arg) -> bool
    arg = any
    
    Devolve True se arg for uma parcela válida,
    e False caso contrário.
    """
    if isinstance(arg, dict) and len(arg) == 3\
    and 'estado' in arg.keys() and 'minada' in arg.keys() and 'numero' in arg.keys()\
    and isinstance(arg['estado'], str) and isinstance(arg['minada'], bool) and isinstance(arg['numero'], str)\
    and arg['estado'] in ['tapada', 'limpa', 'marcada']\
    and isinstance(arg['minada'], bool):
        return True
    return False

def eh_parcela_tapada(p):
    """
    Reconhecedor do TAD parcela.
    eh_parcela_tapada(p) -> bool 
    
    Devolve True se a parcela estiver tapada,
    e False caso contrário.
    """
    if p['estado'] == 'tapada':
        return True
    return False

def eh_parcela_marcada(p):
    """
    Reconhecedor do TAD parcela.
    eh_parcela_marcada(p) -> bool 
    
    Devolve True se a parcela estiver marcada,
    e False caso contrário.
    """
    if p['estado'] == 'marcada':
        return True
    return False

def eh_parcela_limpa(p):
    """
    Reconhecedor do TAD parcela.
    eh_parcela_limpa(p) -> bool 
    
    Devolve True se a parcela estiver limpa,
    e False caso contrário.
    """
    if p['estado'] == 'limpa':
        return True
    return False

def eh_parcela_minada(p):
    """
    Reconhecedor do TAD parcela.
    eh_parcela_minada(p) -> bool 
    
    Devolve True se a parcela tiver uma 
    mina, e False caso contrário.
    """
    return p['minada']

def parcelas_iguais(p1, p2):
    """
    Teste do TAD parcela.
    parcelas_iguais(p1, p2) -> bool
    p1, p2 = parcela (dict)
    """
    if eh_parcela(p1) and eh_parcela(p2):
        if p1['estado'] == p2['estado']\
        and p1['minada'] == p2['minada']\
        and p1['numero'] == p2['numero']:
            return True
    return False

def parcela_para_str(p):
    """
    Transformador do TAD parcela.
    parcela_para_str(p) -> str
    p = parcela (dict)
    
    Devolve uma string (#, @, ? ou X) dependendo do 
    estado e se a parcela tem uma mina ou não.
    """
    if eh_parcela_tapada(p):
        return '#'
    elif eh_parcela_marcada(p):
        return '@'
    elif eh_parcela_limpa(p):
        if not eh_parcela_minada(p):
            return '?'
        else:
            return 'X'

def alterna_bandeira(p):
    """
    Função de alto nível associada ao TAD parcela.
    alterna_bandeira(p) -> bool
    p = parcela (dict)
    
    Devolve True or False, dependendo se a operação
    de alternar o estado da parcela de limpa para
    marcada foi bem-sucedida ou não.
    """
    if eh_parcela_marcada(p):
        desmarca_parcela(p)
        return True
    elif eh_parcela_tapada(p):
        marca_parcela(p)
        return True
    return False


"""
TAD Campo:

A representação escolhida foi a de uma lista, com cada
elemento da lista a representar uma linha do campo.
As linhas têm como comprimento o número de colunas do campo,
e cada elemento dentro das linhas representa uma parcela.
"""

def cria_campo(c, l):
    """
    Construtor do TAD campo.
    cria_campo(c, l) -> campo (list)
    c = última coluna (str)
    l = última linha (int)
    
    Devolve um campo com o tamanho adequado de forma a que
    a última coluna e linha sejam as definidas, com cada parcela
    tapada e sem minas escondidas. Devolve ValueError caso
    os seus argumentos não sejam válidos.
    """
    try:
        eh_coordenada(cria_coordenada(c, l))
    except:
        raise ValueError('cria_campo: argumentos invalidos')
    if not isinstance(c, str) or not isinstance(l, int)\
    or ord('A') <= ord(c) > ord('Z') or 1 <= l >= 100:
        raise ValueError('cria_campo: argumentos invalidos')
    campo = []
    for linha in range(0, l):
        a_adicionar = []
        for coluna in range(ord('A'), ord(c) + 1):
            a_adicionar.append(cria_parcela())
        campo.append(a_adicionar) #linha e coluna só servem o propósito de garantir o tamanho desejado.
    return campo

def cria_copia_campo(m):
    """
    Construtor do TAD campo. 
    cria_copia_campo(m) -> campo (dict)
    m = campo (list)
    
    Devolve uma cópia do campo m através do método
    deepcopy (não houve import), para garantir que cada
    parcela é modificada independente da original.
    """
    copia = m.copy()
    for linha in range(0, len(copia)):
        copia[linha] = m[linha].copy()
        for coluna in range(0, len(copia[0])):
            copia[linha][coluna] = cria_copia_parcela(obtem_parcela(m, cria_coordenada(chr(coluna + ord('A')), linha + 1)))
    return copia

def obtem_ultima_coluna(m):
    """
    Seletor do TAD campo.
    obtem_ultima_coluna(m) -> str
    m = campo (list)
    
    Devolve a última coluna do campo m.
    """
    return chr(ord('A') + len(m[0]) - 1)

def obtem_ultima_linha(m):
    """
    Seletor do TAD campo.
    obtem_ultima_linha(m) -> int
    m = campo (list)
    
    Devolve o valor da última linha do campo m.
    """
    return len(m)

def obtem_parcela(m, c):
    """
    Seletor do TAD campo.
    obtem_parcela(m) -> parcela (dict)
    m = campo (list)
    c = coordenada (tuple)
    
    Devolve a a parcela presente na coordenada c no campo m.
    """
    return m[obtem_linha(c) - 1][ord(obtem_coluna(c)) - ord('A')]

def obtem_coordenadas(m, s):
    """
    Seletor do TAD campo.
    obtem_coordenadas(m, s) -> tuple
    m = campo (list)
    s = str
    
    Devolve um tuplo com as coordenadas (também tuplos) que
    satisfazem a condição requerida pela string.
    Ex.: s = 'minadas', devolve um tuplo com as coordenadas minadas.
    """
    tuplo = ()
    for linha in range(len(m)):
        for coluna in range(len(m[linha])):
            coordenada = cria_coordenada((chr(ord('A') + coluna)), linha + 1)
            if s == 'limpas' and eh_parcela_limpa(obtem_parcela(m, coordenada)):
                tuplo += (coordenada,)
            elif s == 'tapadas' and eh_parcela_tapada(obtem_parcela(m, coordenada)):
                tuplo += (coordenada,)
            elif s == 'marcadas' and eh_parcela_marcada(obtem_parcela(m, coordenada)):
                tuplo += (coordenada,)
            elif s == 'minadas' and eh_parcela_minada(obtem_parcela(m, coordenada)):
                tuplo += (coordenada,)
    return tuplo

def obtem_numero_minas_vizinhas(m, c):
    """
    Seletor do TAD campo.
    obtem_numero_minas_vizinhas(m, c) -> int
    m = campo (list)
    c = coordenada (tuple)
    
    Devolve o número de parcelas minadas adjacentes à
    parcela na coordenada fornecida.
    """
    minas_vizinhas = 0
    parcelas_vizinhas = obtem_coordenadas_vizinhas(c)
    for parcela in parcelas_vizinhas:
        if eh_coordenada_do_campo(m, parcela) and eh_parcela_minada(obtem_parcela(m, parcela)):
            minas_vizinhas += 1
    return minas_vizinhas

def eh_campo(arg):
    """
    Reconhecedor do TAD campo.
    eh_campo(arg) -> bool
    arg = any
    
    Devolve True caso arg seja um campo válido,
    e False caso contrário.
    """
    if isinstance(arg, list) and 1 < len(arg) < 100\
    and 1 < len(arg[0]) < 26:
        for linha in range(len(arg)):
            for coluna in range(len(arg[linha])):
                if not eh_parcela(arg[linha][coluna]):
                    return False
        return True
    return False

def eh_coordenada_do_campo(m, c):
    """
    Reconhecedor do TAD campo.
    eh_coordenada_do_campo(m, c) -> bool
    m = campo (list)
    c = coordenada (tuple)
    
    Devolve True caso a coordenada pertenca aos limites
    do campo, e False caso contrário.
    """
    if eh_coordenada(c):
        if not ord('A') <= ord(obtem_coluna(c)) <= ord(obtem_ultima_coluna(m)):
            return False
        elif not 1 <= obtem_linha(c) <= obtem_ultima_linha(m):
            return False
    return True

def campos_iguais(m1, m2):
    """
    Teste do TAD campo.
    campos_iguais(m1, m2) -> bool
    m1, m2 = campo (list)
    
    Devolve True se os argumentos m1 e m2 são campos
    e iguais, e False caso uma destas condições não
    se verifique.
    """
    if eh_campo(m1) and eh_campo(m2):
        for i in m1:
            for l in m2:
                if len(i) != len(l): #linhas com comprimentos diferentes
                    return False 
        if len(m1) == len(m2) and len(m1[0]) == len(m2[0]):
            for linha in range(0, obtem_ultima_linha(m1)):
                for coluna in range(0, ord(obtem_ultima_coluna(m1)) - ord('A')):
                    coordenada = cria_coordenada(chr(coluna + 65), linha + 1)
                    if not parcelas_iguais(obtem_parcela(m1, coordenada), obtem_parcela(m2, coordenada)):
                        return False
            return True
    return False

def campo_para_str(m):
    """
    Transformador do TAD campo.
    campo_para_str(m) -> str
    m = campo (list)
    
    Devolve o campo m em string.
    """
    linhas, colunas = [], []
    for linha in range(1, obtem_ultima_linha(m) + 1):
        linhas += [linha] #lista de todas as linhas
    for coluna in range(ord('A'), ord(obtem_ultima_coluna(m)) + 1):
        colunas += [chr(coluna)] #lista de todas as colunas

    cabeça = '   {}\n'.format(''.join(colunas))
    divisória = '  +{}+'.format('-' * len(colunas))
    corpo = '\n'
    for linha in linhas:
        for coluna in colunas:
            coordenadas = cria_coordenada(coluna, linha)
            parcela = obtem_parcela(m, coordenadas)
            num_minas = obtem_numero_minas_vizinhas(m, coordenadas)
            if eh_parcela_limpa(parcela) and not eh_parcela_minada(parcela) and num_minas > 0:
                altera_numero_minas_vizinhas(parcela, num_minas)
            else:
                altera_numero_minas_vizinhas(parcela, 0) #o número de minas vizinhas de uma parcela minada não importa.

    for linha in linhas:
        a_adicionar = ''
        for coluna in colunas:
            coordenadas = cria_coordenada(coluna, linha)
            parcela = obtem_parcela(m, coordenadas)
            if eh_parcela_limpa(parcela)\
            and not eh_parcela_minada(parcela): #vamos adicionar os numeros como strings.
                a_adicionar += numero_em_str(parcela)
            else:
                a_adicionar += parcela_para_str(parcela)
        if linha < 10:
            corpo += '0{}|{}|\n'.format(linha, a_adicionar)
        else:
            corpo += '{}|{}|\n'.format(linha, a_adicionar)
    return cabeça + divisória + corpo + divisória

def coloca_minas(m, c, g, n):
    """
    Função de alto nível associada ao TAD campo.
    m = campo (list)
    c = coordenada (tuple)
    g = gerador (list)
    n = numero de minas (int)
    
    Calcula através do gerador possíveis localizações para
    cada mina (não pode ser na vizinhança da coordenada) e
    coloca-las até todas serem colocadas, altura em que 
    devolve o campo."""
    coordenadas_a_evitar = obtem_coordenadas_vizinhas(c) + (c,) #vizinhança de c, e c.
    if len(coordenadas_a_evitar) != len(obtem_coordenadas(m, 'tapadas')): #nenhuma mina é colocada se não houver espaço, para começar.
        while n != 0:
            coluna_mina = gera_carater_aleatorio(g, obtem_ultima_coluna(m))
            linha_mina = gera_numero_aleatorio(g, obtem_ultima_linha(m))
            possivel_mina = cria_coordenada(coluna_mina, linha_mina)
            parcela = obtem_parcela(m, possivel_mina)
            if not eh_parcela_minada(parcela)\
            and possivel_mina not in coordenadas_a_evitar:
                esconde_mina(parcela)
                n -= 1
    return m

def limpa_campo(m, c):
    """
    Função de alto nível associada ao TAD campo.
    limpa_campo(m, c) -> campo (list)
    m = campo (list)
    c = coordenada (tuple)
    
    Limpa a coordenada selecionada, e se esta não tiver
    minas adjacentes, faz o mesmo a essas parcelas, 
    até existirem parcelas adjacentes por limpar com minas.
    """
    coordenadas_a_limpar = [c]
    parcela = obtem_parcela(m, c)
    if eh_coordenada_do_campo(m, c) and not eh_parcela_minada(parcela)\
    and not eh_parcela_limpa(parcela):
        if obtem_numero_minas_vizinhas(m, c) == 0:
            limpa_parcela(parcela)
            vizinhas = list(obtem_coordenadas_vizinhas(c))
            for vizinha in vizinhas:
                if eh_coordenada_do_campo(m, vizinha) and vizinha not in coordenadas_a_limpar:
                    coordenadas_a_limpar += [vizinha]
        else:
            limpa_parcela(parcela)
            return m
    while True:
        mudou = 0
        for coordenadas in coordenadas_a_limpar:
            parcela = obtem_parcela(m, coordenadas)
            if eh_coordenada_do_campo(m, coordenadas) and not eh_parcela_minada(parcela)\
            and not eh_parcela_limpa(parcela) and not eh_parcela_marcada(parcela):
                if obtem_numero_minas_vizinhas(m, coordenadas) == 0:
                    limpa_parcela(parcela)
                    vizinhas = list(obtem_coordenadas_vizinhas(coordenadas))
                    mudou += 1
                    for vizinha in vizinhas:
                        if eh_coordenada_do_campo(m, vizinha) and vizinha not in coordenadas_a_limpar:
                            coordenadas_a_limpar += [vizinha]
                else:
                    limpa_parcela(parcela) #se houver uma mina nas redondezas, não se limpa essas parcelas, por esta.
                    mudou += 1
            elif eh_coordenada_do_campo(m, coordenadas) and eh_parcela_minada(parcela)\
            and not eh_parcela_limpa(parcela) and not eh_parcela_marcada(parcela):
                limpa_parcela(parcela)
                break
        if mudou == 0:
            break #já todas a limpar foram limpas.
    return m

def jogo_ganho(m):
    """
    Função adicional (não auxiliar!).
    jogo_ganho(m) -> bool
    m = campo (list)
    
    Devolve True se todas as parcelas tapadas sem minas
    tiverem sido limpas, e False caso contrário.
    """
    linhas, colunas = [], []
    for linha in range(1, obtem_ultima_linha(m) + 1):
        linhas += [linha]
    for coluna in range(ord('A'), ord(obtem_ultima_coluna(m)) + 1):
        colunas += [chr(coluna)]

    for linha in linhas:
        for coluna in colunas:
            parcela = obtem_parcela(m, cria_coordenada(coluna, linha))
            if not eh_parcela_minada(parcela): #verificar se ainda existe uma parcela não minada tapada.
                if not eh_parcela_limpa(parcela):
                    return False
    return True

def turno_jogador(m):
    """
    Função adicional (não auxiliar!).
    turno_jogador(m) -> bool
    m = campo (list)
    
    Recebe input (L/M) assinalando as ações de limpar ou marcar, 
    sendo que escolhido uma, recebe input de uma coordenada 
    para realizar a ação. Devolve True caso a ação tenha sido 
    realizada, mas False se foi limpa uma parcela com mina.
    Se receber um input inválido, pede-o novamente.
    """
    while True: #para podermos repetir o input.
        ação = input('Escolha uma ação, [L]impar ou [M]arcar:')
        if ação == 'L':
            while True: #a mesma coisa do último while.
                try: #possiveis coordenadas inválidas
                    coordenadas = input('Escolha uma coordenada:')
                    if len(coordenadas) == 3:
                        coordenadas = str_para_coordenada(coordenadas)
                        parcela = obtem_parcela(m, coordenadas)
                    if eh_parcela(parcela):
                        if not eh_parcela_limpa(parcela) and not eh_parcela_minada(parcela):
                            limpa_campo(m, coordenadas)
                            return True
                        elif eh_parcela_limpa(parcela):
                            return True
                        elif not eh_parcela_limpa(parcela) and eh_parcela_minada(parcela):
                            limpa_parcela(parcela)
                            return False
                except:
                    continue
        elif ação == 'M':
            while True:
                try: #o mesmo motivo do anterior
                    coordenadas = input('Escolha uma coordenada:')
                    if len(coordenadas) == 3:
                        coordenadas = str_para_coordenada(coordenadas)
                        parcela = obtem_parcela(m, coordenadas)
                    if eh_parcela(parcela):
                        if not eh_parcela_limpa(parcela):
                            alterna_bandeira(parcela)
                            return True
                        elif eh_parcela_limpa(parcela):
                            return True
                except:
                    continue

def numero_bandeiras(m, n):
    """
    Função auxiliar.
    numero_bandeiras(m, n) -> str
    m = campo (list)
    n = numero de minas (int)
    
    Devolve uma str representando o cabeçalho do jogo de 
    minas, onde é contabilizado o número de bandeiras em campo.
    """
    num = 0
    for coluna in range(ord('A'), ord(obtem_ultima_coluna(m)) + 1):
        for linha in range(1, obtem_ultima_linha(m) + 1):
            coordenadas = cria_coordenada(chr(coluna), linha)
            parcela = obtem_parcela(m, coordenadas)
            if eh_parcela_marcada(parcela):
                num += 1
    return '   [Bandeiras {}/{}]'.format(num, n) #uma simples iteração.


def minas(c, l, n, d, s):
    """
    Função adicional (não auxiliar!)
    minas(c, l, n, d, s) -> bool
    c = ultima coluna (str)
    l = ultima linha (int)
    n = numero de minas (int)
    d = bits do gerador (int)
    s = seed (int)

    Função que permite jogar ao jogo de minas. Repete a função
    turno_jogador até o jogo ser vencido ou perdido. Devolve
    True e False, respetivamente, dependendo do resultado.
    Devolve ValueError caso receba argumentos inválidos.
    """
    try:
        m = cria_campo(c, l)
        g = cria_gerador(d, s)
    except:
        raise ValueError('minas: argumentos invalidos')
    if not isinstance(n, int) or n <= 0 or n >= len(obtem_coordenadas(m, 'tapadas')) - 9:
        raise ValueError('minas: argumentos invalidos')
    print(numero_bandeiras(m, n))
    print(campo_para_str(m))
    while True: #temos de pedir input outra vez.
        try:
            coordenada_inicial = input('Escolha uma coordenada:')
            if len(coordenada_inicial) == 3: #Ter por exemplo 'E3' induz a função em erro.
                coordenada_inicial = str_para_coordenada(coordenada_inicial)
            if eh_coordenada(coordenada_inicial) and eh_coordenada_do_campo(m, coordenada_inicial)\
            and eh_parcela(obtem_parcela(m, coordenada_inicial)):
                break
        except:
            raise ValueError('minas: argumentos invalidos')
    limpa_campo(coloca_minas(m, coordenada_inicial, g, n), coordenada_inicial)
    if len(obtem_coordenadas(m, 'minadas')) == 0:
        raise ValueError('minas: argumentos invalidos')
    perdeu = False #O jogo nunca começa perdido.
    while not jogo_ganho(m) and perdeu == False:
        print(numero_bandeiras(m, n))
        print(campo_para_str(m))
        if turno_jogador(m) == False: #uma mina foi ativada.
            perdeu = True
    if perdeu:
        print(numero_bandeiras(m, n))
        print(campo_para_str(m))
        print('BOOOOOOOM!!!')
        return False
    else:
        print(numero_bandeiras(m, n))
        print(campo_para_str(m))
        print('VITORIA!!!')
        return True




