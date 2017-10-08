##
# PYTHON BASICO: TUPLAS
# Autor: Sady Sell Neto
# Copyright (C) 2017
##

# Criando uma tupla:
o = 1, 2, 3
t = (4, 5, 6)

# Os parenteses sao obrigatorios em lugares que a virgula
# eh parte da sintaxe, como no comando print do Python2,
# formatacao de strings com o operador %, argumentos de funcao,
# entre outros.

# Ex.: imprimir duas tuplas:
print (1, 2), (3, 4) # (1, 2) (3, 4)
print ""

# Tupla de um elemento (singleton):
singleton = 10,

# Tupla vazia
vazia = ()
vazia2 = tuple()

t = o

# Elementos sao acessados como na lista:
print t[1] # 2

# A tupla eh imutavel, portanto
# t[1] = 0
# del t[1]
# resultam em erro.
print ""

# O tamanho (n-aridade) de um conjunto eh dado pela funcao "len":
print len(t) # 3
print ""

# Operator + concatena tuplas:
print (1, 2) + (3, 4, 5) # (1, 2, 3, 4, 5)

# Operator * gera repeticoes da tupla:
print 3 * (1, 2) # (1, 2, 1, 2, 1, 2)

# Operador "in" verifica se um elemento esta na tupla
# ("not in" tambem disponivel):
print 3 in t # True
print 0 in t # False
print ""

# Comparacao de tuplas eh lexicografica, isto eh,
# compara-se elemento a elemento, ate encontrar a
# primeira diferenca; o resultado (< ou >) da diferenca
# entre os elementos diferentes, sera o resultado da
# diferenca entre as tuplas.
# Dessa definicao tambem decorre que duas tuplas sao iguais
# se todos os seus elementos sao iguais.
# Tambem decorre dessa definicao que, se uma tupla eh
# "subtupla" de outra, ela eh menor que essa outra.

# Funcao "zip" transforma varias listas em uma lista
# de tuplas
# (Util para se iterar simultaneamente sobre varias listas):
print zip([1, 2, 3], ["a", "b", "c"]) # [(1, 'a'), (2, 'b'), (3, 'c')]
print zip([5, -5], ["5", "-5"], [5.0, -5.0]) # [(5, '5', 5.0), (-5, '-5', 5.0)]
print ""

# Tuplas podem expandir e comprimir na atribuicao
# e em algumas outras expressoes:
t = 5, -5
a, b = t
c, d = a, b
print a, b, c, d, t # 5 -5 5 -5 (5, -5)

# Obs.:
# Como tuplas sao imutaveis, o problema do clone VS atribuicao
# que ocorre em outras estruturas de dados eh irrelevante
# para tuplas.
