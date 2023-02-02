import sys
from  datetime import date
#CONSTANTES#
TIPO_VALOR = 3
FINAL = 4
FRASE = 2
TAMANHO2FINAL = 4
OPCAO = 1
#main#
#<OPÇÃO> <frase> <tipo,valor> <final>
#<OPÇÃO> <frase> <tipo,valor>
def geraFraseComNumero(inicio, final):
    data_atual = date.today()
    if(final == None):
        final = data_atual.year

    for iten in range(inicio, final):
        frase = sys.argv[FRASE] + str(iten)
        print(frase)
try:
    
    if(sys.argv[OPCAO] == "--help"):
        print("<OPÇÃO> <frase> <tipo,valor> <final> or <OPÇÃO> <frase> <tipo,valor>")
        print("-n \t gerar usando frase e números")
    elif(sys.argv[OPCAO] == "-n"):
        #gera palavra combinando frase + numero
        #converte o argumento para lista
        contador = 0
        final = 0
        lista_argumento = sys.argv[TIPO_VALOR].split(",")
        if(lista_argumento[0] == "int"):
            #converte o proximo elemento em inteiro
            inicio = int(lista_argumento[1])
            if(len(sys.argv) > TAMANHO2FINAL):
                final  = int(sys.argv[FINAL])
            else:
                final = None
            geraFraseComNumero(inicio, final)

except:
    print("error!")
