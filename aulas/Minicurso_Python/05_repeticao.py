##
# PYTHON BASICO: ESTRUTURAS DE REPETICAO
# Autor: Sady Sell Neto
# Copyright (C) 2017
##

# Uma das principais estrutras de decisao: while:

i = 10
while i > 0:
  print i,
  i -= 1

print ""
# 10 9 8 7 6 5 4 3 2 1

# Python nao possui do-while.

# O for do python passa sobre cada elemento de uma sequencia:
for i in [2, 3, 5]:
  print 2 * i,
print ""
# 4 6 10

# Para gerar listas a fim de que o "for" funcione como o
# "for" aritmetico classico, use a funcao "range".
# A funcao range funciona assim:
# range(start, stop, step) gera uma lista
#   no intervalo de [start, stop), de step em step numeros.
# range(start, stop) gera uma lista no intervalo de [start, stop).
# range(stop) gera uma lsita no intervalo [0, stop)
#   (possuindo "stop" elementos).

for i in range(10, 20):
  print i,
print ""
# 10 11 12 13 14 15 16 17 18 19

for i in range(20, 10, -1):
  print i,
print ""
# 20 19 18 17 16 15 14 13 12 11

# Para listas grandes, considere usar xrange que,
# em vez de gerar uma lista propriamente dita,
# gera os numeros que a comporiam sob demanda.
# No Python3, esse ja eh o comportamento da funcao range,
# sendo desnecessaria uma funcao xrange.

i = 0
for i in xrange(1000):
  pass # Usado para preencher um bloco vazio.
print i # 999
