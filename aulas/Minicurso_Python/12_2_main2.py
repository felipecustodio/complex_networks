##
# PYTHON BASICO: FUNCAO MAIN AVANCADA
# Autor: Sady Sell Neto
# Copyright (C) 2017
##

import sys

# Funcao main mais elaborada, completa.
# Funciona como ponto de entrada do programa.
# Acessa os argumentos da linha de comando via o parametro "args"
# e retorna um codigo para o SO (0, se nao houver instrucao de
# de retorno na funcao).
def main(args):
  pass # Conteudo da funcao aqui.
  
# A variavel __name__ valerá "__main__" apenas
# quando o modulo nao for importado.
# Dessa forma, pode-se ter varias funcoes main, e a unica
# executada sera a daquele sobre o qual o interpretador foi
# invocado (pois apenas esse modulo ter "__main__" em __name__).
if __name__ == "__main__":
  sys.exit(int(main(sys.argv[1:]) or 0))

# Obs.: Ao se utilizar sys.argv[1:], a funcao "main" dispora apenas
# dos argumentos para o programa em si, isto eh, descartando o
# argumento que corresponde a propria invocacao do programa. Caso
# nao deseje descarta-lo, utilize sys.argv[:] em vez de sys.argv[1:]
# (sys.argv[:] eh preferivel em relacao a sys.argv, pois o primeiro
# cria uma copia da lista, podendo ser mais livremente alterada).
