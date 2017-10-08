##
# PYTHON BASICO: LISTAS
# Autor: Sady Sell Neto
# Copyright (C) 2017
##

# Criando uma lista:
o = [13, 11, 7, 5, 3, 2]
vazia = []
vazia2 = list()

# "Clonando" / copiando uma lista:
l = o[:]

# Elementos da lista comecam na posicao 0:
print l[0] # 13
print l[2] # 7

# Posicoes negativas acessam a lista de tras para frente:
print l[-1] # 2
print l[-3] # 5
print ""

# Lista pode ter seus elementos alterados (ela eh dita mutavel):
l[0] = 1
print l[0] # 1

# Lista pode ter seus elementos removidos:
del l[-1]
print l # [1, 11, 7, 5, 3]
print ""

l = o[:]

# Slicing:
# Gerar uma sublista do primeiro ao elemento ate o quarto
# (inclui o primeiro, nao inclui o quarto):
print l[1:4] # [11, 7, 5]

# Pode ser, opcionalmente, especificado o "pulo" da fatia,
# isso eh, pegar elementos de "quanto em quanto".
print l[1:4:2] # [11, 5]

# Esse "pulo" pode ser negativo para percorrer a lista ao contrario:
print l[4:0:-1] # [3, 5, 7, 11]

# Se o primeiro indice da fatia eh omitido, Python usa
# o comeco da lista por padrao.
print l[:4] # [13, 11, 7, 5]

# Se o segundo eh omitido, Python usa o fim da lista por padrao:
print l[2:] # [7, 5, 3, 2]

# Assim, eh facil reverter uma lista:
print l[::-1] # [2, 3, 5, 7, 11, 13]
print ""

# Pode-se escrever em uma fatia, substituindo-a:
l[1:3] = [-11, -7]
print l # [13, -11, -7, 5, 3, 2]

# Pode-se apagar uma fatia tambem:
del l[1:3] # [13, 5, 3, 2]
print l
print ""

# O tamanho de uma lista eh dado pela funcao "len":
print len(o) # 6

# Uma lista pode ser ordenada pela funcao "sorted"
# (retorna uma nova lista):
print sorted(o) # [2, 3, 5, 7, 11, 13]
print ""

l = o[:]

# Para acrescentar um elemento na lista, use o metodo "append":
l.append(17)
print l # [2, 3, 5, 7, 11, 13, 17]

# Para remover o ultimo elemento, metodo "pop"
# (ultimo elemento tambem eh retornado):
n = l.pop()
print l # [2, 3, 5, 7, 11, 13]
print n # 17

# Para achar a posicao de um elemento na lista, metodo "index":
# (Levanta excecao se elemento ausente, portanto use com sabedoria,
# ou o comando try-except, se voce conhece-lo.)
print l.index(5) # 3

# Metodo "count" conta o numero de ocorrencias de um elemento:
l.append(13)
print l.count(13) # 2
l.pop()

# Metodo "sort" ordena a lista (diferentemente da funcao sorted,
# a lista eh alterada):
l.sort() # [2, 3, 5, 7, 11, 13]
print l
print ""

# Operador + concatena listas:
print [1, 2] + [3, 4, 5] # [1, 2, 3, 4, 5]

# Operador * gera repeticoes da lista:
print 3 * [1, 2] # [1, 2, 1, 2, 1, 2]

# Operador "in" verifica se um elemento esta na lista:
# (O contrariro dele eh o "not in").
# (Obs.: 7 not in l eh mais legivel e mais rapido que not(7 in l).)
print 7 in l # True
print 6 in l # False
print 7 not in l # False
print 6 not in l # True
print ""

# Comparacao de listas eh lexicografica, isto eh,
# compara-se elemento a elemento, ate encontrar a
# primeira diferenca; o resultado (< ou >) da diferenca
# entre os elementos diferentes, sera o resultado da
# diferenca entre as listas.
# Dessa definicao tambem decorre que duas listas sao iguais
# se todos os seus elementos sao iguais.
# Tambem decorre dessa definicao que, se uma lista eh
# sublista de outra, ela eh menor que essa outra.
print [1, 2, 3] == [1, 2, 3] # True
print [1, 2, 3] < [1, 2, 4] # True
print [1, 2] < [1, 2, 3] # True
print ""

# Voce pode gerar listas pela sintaxe do comprehension tambem:
l = sorted(o)

r = [x ** 2 for x in l]
print r # [4, 9, 25, 49, 121, 169]

r = [2 * x for x in l if x >= 5]
print r # [10, 14, 22, 26]
print ""

# Obs.:
# Note que para copiar uma lista, voce deve usar a notacao [:].
# Se voce atribuir diretamente a uma variavel, nao estara criando
# uma lista nova, apenas fazendo com que duas variaveis se refiram
# a mesma lista. Veja o exemplo abaixo:
l1 = [1, 2, 3, 4]
l2 = l1
l1.append(5)
print l2 # [1, 2, 3, 4, 5]
# Note que l2 foi modificado pela alteraco de l1.

# Obs.:
# Strings tambem sao listas. Quase tudo aprendido aqui,
# vale para strings tambem.
# Em particular, a comparacao lexicografica aplicada para strings,
# torna possivel a comparacao "por ordem alfabetica".
# Porem, strings sao imutaveis. Isto eh, nao se pode fazer
# del "abc"[0]
# del "abcdef"[1:3]
# "abcdef"[1:3] = "z"
# e nem nada que altere a string em si.
