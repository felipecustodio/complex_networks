##
# PYTHON BASICO: FUNCOES
# Autor: Sady Sell Neto
# Copyright (C) 2017
##

# Definir uma funcao:
def dobro(x):
  return 2 * x

# Note que, em Python, nao se define tipo dos parametros
# ou tipo de retorno.
print dobro(5) # 10
print ""

# Parametros com valor padrao:
def mols(p = 1.0, v = 22.4, t = 273.15):
  return p * v / (0.082057338 * t)

print mols(2.0, 11.2, 273.15) # ~1
print mols(2.0, 11.2) # mesmo resultado de cima
print mols(2.0) # ~2

print mols(v = 11.2) # ~0.5
print mols(t = 298.15) # ~0.9
print mols(2.0, t = 298.15) # ~1.8

print ""

# Funcoes void sao criadas simplesmente nao colocando
# nenhuma instrucao "return" (ou entao, usando o "return"
# sozinho, nao seguido de uma expressao):
def diz_sinal(x):
  if x > 0:
    print "Positivo."
  elif x < 0:
    print "Negativo."
  else:
    print "Zero."

diz_sinal(0)
