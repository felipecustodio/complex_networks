##
# PYTHON BASICO: CONJUNTOS
# Autor: Sady Sell Neto
# Copyright (C) 2017
##

# Criando um conjunto:
o = {13, 11, 7, 5, 3, 2}
vazio = set()

# "Clonando" um conjunto:
s = set(o)

# O tamanho (cardinalidade) de um conjunto eh dado pela funcao "len":
print len(o) # 6
print ""

# Para adicionar um elemento no conjunto, use a funcao "add":
s.add(17)
print s # set([13, 11, 7, 5, 3, 2, 17]) 

# Para remover um elemento, use a funcao "remove":
# (Levanta excecao se elemento ausente.)
s.remove(17)
print s # set([13, 11, 7, 5, 3, 2])
print ""

# Operador "in" verifica se um elemento pertence ao conjunto
# ("not in" tambem disponivel):
print 7 in s # True
print 6 in s # False

# Operador & realiza interseccao:
print {1, 2, 3} & {2, 3, 4} # set([2, 3])

# Oprador | realiza uniao:
print {1, 2, 3} | {2, 3, 4} # set([1, 2, 3, 4])

# Operador - realiza subtracao de conjuntos
print {1, 3} - {2, 3} # set([1])

# Operador <= eh o "esta contido" / "subconjunto"
# e o operador >= eh o "contem" / "sobreconjunto":
print {1, 2, 3} <= {2, 3, 4} # False
print {1, 2} <= {1, 2, 3} # True
print ""

# Conjuntos sao iteraveis:
for e in o:
  print e,
print ""
print ""
# 2 3 5 7 11 13

# Comprehensions tambem disponiveis para conjuntos:
r = {x ** 2 for x in o}
print r # set([4, 9, 25, 49, 121, 169])

# Obs.:
# O mesmo problema de atribuicao de variavel acontece nos conjuntos,
# isto eh, o conjunto continua um, apenas com duas variaveis
# referindo-se a ele. Deve se clonar o conjunto, em vez de so atribuir
# a uma variavel.
