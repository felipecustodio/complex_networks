##
# PYTHON BASICO: STRINGS
# Autor: Sady Sell Neto
# Copyright (C) 2017
##

# Strings tem bastantes similaridades a uma lista.
# Porem, eh importante entender que nao existe o tipo caractere
# em Python. Apenas podemos representar strings.

# Criando uma string:
s = "abcdefghij"
vazia = ""
vazia2 = str()

# Acesso de elementos em string eh identico a lista:
print s[0] # a
print s[2] # c
print s[-1] # j
print s[-3] # h
print ""

# Porem a string nao pode ter seus elementos alterados,
# sendo assim, dita imutavel. As seguintes instrucoes
# sao invalidas:
# s[0] += 1
# del s[-1]

# String tambem suporta slicing:
print s[1:4] # bcd
print s[1:4:2] # bd
print s[4:0:-1] # dcb
print s[:4] # abc
print s[2:] # cdefghij
print s[::-1] # jihgfedcba
print ""

# Porem, por ser imutavel, atribuicao e delecao de slicing
# tambem sao invalidas, como os exemplos abaixo:
# s[1:3] = "z"
# del s[1:3] # [13, 5, 3, 2]

# O tamanho de uma string eh dado pela funcao "len":
print len(s) # 10

# Metodos "capitalize", "lower", "upper" retornam uma versao
# modificada da string com a caixa dos caracteres alteradas:
print "apple".capitalize() # apple
print "Apple".lower() # apple
print "Apple".upper() # APPLE
print ""

# Metodo "count" conta quantas vezes uma substring aparace
# na string:
print "banana".count("na") # 2

# Metodo "find" procura uma substring na string, retornando
# o indice da primeira ocorrencia, ou -1 se nao encontrado.
# O metodo "index" faz a mesma coisa, porem levanta excecao
# se substring nao encontrada, em vez de retornar -1.
# Metodos "rfind" e "rindex" fazem a mesma coisa, porem
# retornando o indice da ultima ocorrrencia.
print "banana".find("na") # 2
print "banana".rfind("na") # 4

# Metodo "replace" substitui cada ocorrencia da substring
# na string por uma nova substring:
print "banana".replace("na", "ta") # batata
print ""

# Metodo "join" pega um iteravel (qualquer coisa que pode ser
# colocada no "for", como listas, tuplas, conjuntos,
# dicionarios, ...) compostas de strings e faz uma string com seus
# elementos unidos por um separador:
print "|".join(["1", "2", "3"]) # 1|2|3

# Metodo "split" procura um separador e separa as ocorrencias
# anteriores e posteriores da string, retornando assim, uma
# lista de strings:
print "a|b|c".split("|") # ['a', 'b', 'c']
# (o separador padrao pode ser usado para separar palavras:)
b = "Esse eh\tum texto\nbem    baguncado"
print b # Esse eh   um texto
# bem    baguncado
for palavra in b.split():
    print palavra,
print ""
print ""

# Operador + concantena strings:
print "abc" + "def" # abcdef

# Operador * gera repeticoes da string:
print 10 * "k" # kkkkkkkkkk

# Operador "in" verifica se uma substring esta presente na string:
# ("not in" tambem disponivel):
print "na" in "banana" # True

# Operador % eh usado para formatacao de strings
print "%d pessoas sobreviveram." % 70
# 70 pessoas sobreviveram.
print "O %s esta acima de %.2f %s!" % ("dolar", 3.0, "reais")
# O dolar esta acima de 3.00 reais!

# Como a comparacao de strings tambem eh lexicografica,
# pode-se usar o operador < para saber se uma string
# vem antes da outra em ordem alfabetica (vice-versa
# para o operador >).
print "banana" == "banana" # True
print "banana" < "batata" # True
print ""

# Strings tambem sao iteraveis (itera-se sobre cada caractere como
# uma substring de tamanho 1):
for c in "abcde":
    print c,
print ""
# a b c d e

# Obs.:
# Como string sao imutaveis, o problema do clone VS atribuicao
# que ocorre em outras estruturas de dados eh irrelevante
# para strings.
