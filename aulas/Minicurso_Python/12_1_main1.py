##
# PYTHON BASICO: FUNCAO MAIN BASICA
# Autor: Sady Sell Neto
# Copyright (C) 2017
##

# Funcao main feita de forma simples.
# Funciona como ponto de entrada do programa.
# Nao se preocupa com argumentos da linha de comando
# nem com valor de retorno para o SO.
def main():
  pass # Conteudo da funcao aqui.

# A variavel __name__ valerá "__main__" apenas
# quando o modulo nao for importado.
# Dessa forma, pode-se ter varias funcoes main, e a unica
# executada sera a daquele sobre o qual o interpretador foi
# invocado (pois apenas esse modulo ter "__main__" em __name__).
if __name__ == "__main__":
  main()
