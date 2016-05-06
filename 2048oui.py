# Grupo 85 - Pedro Farias 81657 e Joao Ramos 80915

from random import random
from random import randint

def cria_coordenada(l,c):
    
    """ esta funcao recebe dois argumentos do tipo inteiro. Numeros entre 1 e 4 
    inclusive, o primeiro numero corresponde a linha e o segundo a coluna """
    
    if isinstance(l,int) and  isinstance(c,int):
        if 1<= l and l <= 4 and 1<= c and c <= 4:
            #verifica se ambos os numeros estao entre 1 e 4 e sao inteiros
            return (l,c)
  
    raise ValueError('cria_coordenada: argumentos invalidos')

def coordenada_linha(coor):
    """ Esta funcao recebe uma coordenada e devolve um inteiro correspondente a linha """
    return coor[0]


def coordenada_coluna(coor):
    """ Esta funcao recebe uma coordenada e devolve um inteiro correspondente a coluna """    
    return coor[1]


def e_coordenada(coor):
    
    """ Esta funcao verifica se e uma coordenada.
    Input- universal
    Output- logico """
    
    if isinstance(coor,tuple) and len(coor) == 2:
        if isinstance(coor[0],int) and  isinstance(coor[1],int):
            if 1<= coor[0] and coor[0] <= 4 and 1<= coor[1] and coor[1] <= 4:
                #verifica se a coordenada e um tuplo, se apenas tem 2 elementos
                #se ambos os elementos sao inteiros e compreendidos entre 1 e 4
                return True
    return False         
    
    
def coordenadas_iguais(coor,coor2):
    
    """ Esta funcao verifica se duas coordenadas sao iguais
    Input- duas coordenadas
    Output- logico """
    
    return coordenada_linha(coor) == coordenada_linha(coor2) and coordenada_coluna(coor) == coordenada_coluna(coor2)

# TAD tabuleiro, representacao interna: um dicionario com a chave 'pont' para a pontuacao
# e a chave 'tab' para o tabuleiro que e' representado em listas

def cria_tabuleiro():
    """ Esta funcao nao recebe nenhum argumento e devolve um tabuleiro vazio. """
    return {'pont': 0, 'tab': [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]}

def tabuleiro_posicao(t,c):
    
    """ Esta funcao recebe uma coordenada e um tabuleiro e devolve um inteiro.
    que corresponde ao valor da posicao no tabuleiro """
    
    if e_coordenada(c):
        return t['tab'][coordenada_linha(c)-1][coordenada_coluna(c)-1]
    #subtrai-se 1 porque nas listas comecam com o elemento 0 e estas coordenadas comecam por 1
    else:
        raise ValueError("tabuleiro_posicao: argumentos invalidos")

def tabuleiro_pontuacao(t):
    """ Esta funcao recebe um tabuleiro e devolve a pontuacao atual """
    return t['pont']

def tabuleiro_posicoes_vazias(t):
    
    """ Esta funcao devolve uma lista com todas as posicoes vazias do tabuleiro
    Input- tabuleiro
    Output- lista """
    
    res = []
    
    for l in range(1,5): 
        for c in range(1,5):
            if tabuleiro_posicao(t,cria_coordenada(l,c)) == 0:
                res = res + [cria_coordenada(l,c)]
    return res
                
                
def tabuleiro_preenche_posicao(t,c,v):
    
    """ Esta funcao preenche a posicao c com o valor v
    Input- tabuleiro(t), coordenada(c) e inteiro(v)
    Output- tabuleiro modificado(t) """
    
    if e_coordenada(c) and isinstance(v,int):
        t['tab'][coordenada_linha(c)-1][coordenada_coluna(c)-1] = v
        return t
    else:
        raise ValueError('tabuleiro_preenche_posicao: argumentos invalidos')
    

def tabuleiro_actualiza_pontuacao(t,v):
    
    """ Esta funcao recebe um tabuleiro e um numero inteiro e retorna um tabuleiro com a pontuacao actualizada """
    
    if isinstance(v,int) and v % 4 == 0 and v >= 0:
        t['pont'] = tabuleiro_pontuacao(t) + v
        return t
    else:
        raise ValueError("tabuleiro_actualiza_pontuacao: argumentos invalidos")
    
def tabuleiro_reduz(t, d):
    
    """ Esta funcao faz a reducao do tabuleiro t na direcao d """
    
    if d in ('N','S','W','E'):
        indices = [1,2,3,4]
    
        if d in ('E', 'S'):
            indices = indices[::-1]
        #se reduzir para baixo ou para a direita, inverte os indices para contar de 4 até 1
        
        if d in ('E', 'W'): #reducao horizontal
            for l in range(1,5):
                # este lambda mantem a linha constante
                reduz(t,l,lambda l,x: cria_coordenada(l,x), indices)  
                
        else: #reducao vertical
            for c in range(1,5): 
                # este lambda mantem a coluna constante
                reduz(t,c,lambda c,x: cria_coordenada(x,c),indices)
                
        return t
    else:
        raise ValueError("tabuleiro_reduz: argumentos invalidos")
            
def reduz(t, x, coord, indices):
    
    """ Esta funcao faz a reducao de uma linha ou de uma coluna
    x corresponde 'a linha se a direcao for E ou W ou 'a coluna caso contrario """
    
    troca = [-1,-1] # troca[0] e a ultimo valor nao nulo e troca[1] é a posicao desse valor
    
    for i in indices:
        valor = tabuleiro_posicao(t,coord(x,i))
        
        if valor == 0:  # ignora os zeros
            continue   # salta para a proxima iteracao
        
        tabuleiro_preenche_posicao(t, coord(x,i), 0)
        
        if valor != troca[0]:  # se os valores forem diferentes
            #coloca o valor na posicao a seguir ao ultimo valor
            tabuleiro_preenche_posicao(t, coord(x,indices[troca[1]+1]), valor)  
            #coloca o novo valor como ultimo valor e a sua posicao
            troca = [valor,troca[1]+1]
            
         
        elif valor == troca[0]: #se os valores forem iguais
            #coloca o dobro do valor na posicao equivalente ao ultimo valor
            tabuleiro_preenche_posicao(t, coord(x,indices[troca[1]]), valor*2)
            tabuleiro_actualiza_pontuacao(t, valor*2) 
            # coloca o ultimo valor como -1 (para ser diferente e não juntar duas vezes)
            troca[0] = -1
            
            
def e_tabuleiro(t):
    
    """ Funcao que permite vericar se e um tabuleiro
    Input- universal
    Output- logico"""
    
    def verifica_matriz(m):
        """ Funcao que verifica se o tabuleiro e constituido por matrizes de listas com inteiros """
        #verifica se o tabuleiro e constituido por matrizes. Em que a primeiro
        # e constituida por uma lista com 4 posicoes
        if isinstance(m, list) and len(m) == 4:
            for i in m:
                if isinstance(i, list) and len(i) == 4:
                    #verifica se dentro da primeira lista existem 4 listas com 4 posicoes
                    for e in i:
                        # verifica se cada posicao das 4 listas e inteiro
                        if not isinstance(e,int):
                            return False
                else:
                    return False
            return True
            
        else:
            return False
        
    if isinstance(t,dict):
        #verifica se o tabuleiro e um dicionario e e' constituido por dois elementos
        if len(t) == 2:
            if 'tab' in t and 'pont' in t: 
                #verifica se um dos elementos chama-se 'tab' e o outro 'pont'
                if isinstance(t['pont'], int) and verifica_matriz(t['tab']):
                    return True
    return False

def tabuleiro_terminado(t):
    
    """ Esta funcao verifica se o tabuleiro esta terminado
    Input- tabuleiro
    Output- logico """
    
    for l in range(1,5):
        for c in range(1,5):
            valor = tabuleiro_posicao(t, cria_coordenada(l,c))
            #se a posicao estiver vazia ou se não estiver mas a coluna ou linha a seguir for igual, devolve falso
            if valor == 0 or c != 4 and valor == tabuleiro_posicao(t, cria_coordenada(l,c+1)) \
            or l != 4 and valor == tabuleiro_posicao(t, cria_coordenada(l+1,c)):
                return False
            
    return True
    
def tabuleiros_iguais(t1,t2):
    
    """ Esta funcao recebe dois tabuleiros e verifica se sao iguais """
    
    if tabuleiro_pontuacao(t1) == tabuleiro_pontuacao(t2):
        for l in range(1,5):
            for c in range(1,5):
                # verifica cada posicao
                coord = cria_coordenada(l,c)
                if tabuleiro_posicao(t1,coord) != tabuleiro_posicao(t2,coord):
                    return False
            
        return True
  
    return False

def escreve_tabuleiro(t):
    
    """ Esta funcao recebe um tabuleiro e escreve a sua representacao no ecra """
    
    if e_tabuleiro(t):
        for l in range(1,5):
            linha = ""
            for c in range(1,5):
                linha = linha + '[ ' + str(tabuleiro_posicao(t,cria_coordenada(l,c))) + ' ]' + " "
            print(linha)
        print("Pontuacao:", tabuleiro_pontuacao(t))
        
    else:
        raise ValueError('escreve_tabuleiro: argumentos invalidos')
    
def pede_jogada():
    
    """ Esta funcao nao recebe nada, apenas pede ao jogador uma jogada. 
    Caso nao introduza umas das 4 teclas possiveis, escreve "Jogada invalida." e volta a pedir  """
    
    while True:
        d = input("Introduza uma jogada (N, S, E, W): ")
        if d in ('N','S', 'E', 'W'):
            return d
        print("Jogada invalida.")
        

def jogo_2048():
    
    """ Esta funcao e a principal do jogo. 
    Permite a utilizador jogar um jogo completo de 2048 """
    
    valida = True  # variavel que verifica se a jogada foi va'lida
    t = cria_tabuleiro()
    preenche_posicao_aleatoria(t)
    
    while not tabuleiro_terminado(t):
        if valida:  # se a jogada foi va'lida preenche uma posicao
            preenche_posicao_aleatoria(t)
            
        valida = True
        
        escreve_tabuleiro(t)
        
        # verifica se a jogada foi v'alida
        if tabuleiros_iguais(copia_tabuleiro(t), tabuleiro_reduz(t,pede_jogada())):
            valida = False 
    
    
def preenche_posicao_aleatoria(t):
    
    """ Funcao que permite escrever no tabuleiro uma posicao aleatoria """
    
    vazias = tabuleiro_posicoes_vazias(t)
    valor = 2
    
    # os valores sao aleatorios de 0 a 9 onde 0 e 1 sao 20%
    
    if int(random()*10) <= 1:
        valor = 4
    
    # aleatoriamente prenche uma posicao vazia
    tabuleiro_preenche_posicao(t, vazias[randint(0, len(vazias)-1)], valor)
    
def copia_tabuleiro(t):
    
    """ Esta funcao recebe um tabuleiro e devolve uma copia do mesmo """    
    
    copia = cria_tabuleiro()
    tabuleiro_actualiza_pontuacao(copia, tabuleiro_pontuacao(t))
    
    for l in range(1,5):
        for c in range(1,5):
            coord = cria_coordenada(l,c)
            tabuleiro_preenche_posicao(copia, coord, tabuleiro_posicao(t,coord))
    
    return copia