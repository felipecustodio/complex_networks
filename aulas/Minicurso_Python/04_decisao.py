##
# PYTHON BASICO: ESTRUTURAS DE DECISAO
# Autor: Sady Sell Neto
# Copyright (C) 2017
##

# Principal estrutra de decisao eh o if-elif-else:
x = 5
if x > 0:
  print "Positivo."
elif x < 0:
  print "Negativo."
else:
  print "Zero."
# Positivo.

x = -5
if x > 0:
  print "Positivo."
elif x < 0:
  print "Negativo."
else:
  print "Zero."
# Negativo.

x = 0
if x > 0:
  print "Positivo."
elif x < 0:
  print "Negativo."
else:
  print "Zero."
# Zero.

# Se for usar mais de um comando, o Python detecta o bloco de
# comandos pela indentacao. Lembre-se de usar indentacao consistente
# (ex.: sempre dois espacos por bloco).
# Se for usar um unico comando, ele pode ser escrito
# na mesma linha apos os dois pontos (:).

# Python nao possui switch-case.

# Expressao if (deve ser usado como expressao):
a = 5
b = 3
maior = a if a > b else b
print maior # 5
