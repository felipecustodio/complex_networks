##
# PYTHON BASICO: DICIONARIOS
# Autor: Sady Sell Neto
# Copyright (C) 2017
##

# Criando um dicionario:
o = {"a": 1, "b": 2, "c": 3}
vazio = {}
vazio2 = dict()

# "Clonando" um dicionario:
d = dict(o)

# Acesso como lista para verificar elemento associado:
# (Levanta excecao se chave ausente.)
print d["b"] # 2

# Use o metodo "get", para tratar o elemento ausente e acessar
# o dicionario de forma segura.
print d.get("a", 0) # 1
print d.get("e", 0) # 0
print ""

# Atribuicao em uma chave, substitui o elemento mapeado.
# Caso a chave nao exista, ela eh inserida
d["c"] = -3
d["d"] = 4
print d # {'a': 1, 'b': 2, 'c': -3, 'd': 4}

# Chaves podem ser removidas:
del d["c"]
print d # {'a': 1, 'b': 2, 'd': 4}
print ""

d = dict(o)

# Funcao "len" conta o numero de chaves
# (e de mapeamentos, como consequencia):
print len(d) # 3

# Funcao "sorted" retorna uma lista ordenada
# de chaves:
print sorted(d) # ['a', 'b', 'c']

# Metodo "keys" retorna uma lista de chaves:
print d.keys() # ['a', 'b', 'c'] (ordem arbitraria)

# Metodo "values" retorna uma lista de valores:
print d.values() # [1, 2, 3] (ordem arbitraria)

# Metodo "items" retorna uma lista de tuplas (chave, valor):
print d.items() # [('a', 1), ('b', 2), ('c', 3)] (ordem arbitraria)
print ""

# Operador "in" verifica se uma chave pertence ao dicionario
# ("not in" tambem disponivel):
print "a" in d
print "z" in d
print ""

# Dicionarios sao iteraveis (itera-se sobre as chaves):
for k in o:
  print k,
print ""
# a b c (ordem arbitaria)

# Mas, por meio do metodo "items", consegue-se iterar sobre os dois:
for k, v in o.items():
  print "%s -> %d" % (k, v)
print ""
# a -> 1
# b -> 2
# c -> 3
# (ordem arbitraria)

# Comprehensions tambem disponiveis para dicionarios:
r = {x: x ** 2 for x in [2, 3, 5, 7, 11]}
print r # {2: 4, 3: 9, 5: 25, 7: 49, 11: 121}

# Obs.:
# O mesmo problema de atribuicao de variavel acontece nos
# dicionarios, isto eh, o dicionario continua um, apenas com duas
# variaveis referindo-se a ele. Deve se clonar o dicionario, em vez
# de so atribuir a uma variavel.
