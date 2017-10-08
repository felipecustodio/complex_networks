##
# PYTHON BASICO: OPERADORES
# Autor: Sady Sell Neto
# Copyright (C) 2017
##

# Operadores aritmeticos:
print 3 + 2 # 5
print 3 - 2 # 1
print 3 * 2 # 6
print 3 / 2 # 1, pois divisao entre inteiros sera sempre inteira (quociente)
print 3 / 2.0 # 1.5, pois divisao envolvendo um numero real sera real
print 3 // 2.0 # 1.0, // descarta a parte decimal (o resultado eh real se um operando for real)
print 3 % 2 # 1
print 3 ** 2 # 9
print ""

# Obs.: No Python2, divisao entre inteiros sera sempre inteira (quociente).
# No Python3, o resultado pode ser real.
# (Ex.: 3 / 2 = 1 (Python2); 3 / 2 = 1.5 (Python3).)
# Use // no Python3 caso queira o quociente.

# Operadores relacionais:
print 3 == 2 # False
print 3 != 2 # True
print 3 < 2 # False
print 3 <= 2 # False
print 3 > 2 # True
print 3 >= 2 # True

# Para verificar se uma variavel eh nula (None),
# use os operadores "is  None" e "is not None".
print 3 is None # False
print 3 is not None # True

n = None
print n is None # True
print n is not None # False

print ""

# Operadores logicos:
print True and False # False
print True or False # True
print not True # False
print ""
