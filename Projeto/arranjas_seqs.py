import re
saida=open('sequencias_encontradas_half_life.txt','w')
arquivo = open('merge_menor_maior_3horas.txt', 'r').read()
#print arquivo
arquivo = re.sub(',', ';', arquivo)
arquivo = re.sub(' ', '', arquivo)
arquivo = re.sub('\'', '', arquivo)
arquivo = re.sub('\(', '', arquivo)
for linha in arquivo.split(')'):
    tamanho_total= len(linha.split(';'))-1
    #print len(linha.split(';')[tamanho_total-1])
    try:
        if len(linha.split(';')[tamanho_total]) >1 and not re.search('N',linha.split(';')[tamanho_total]):
            print linha.split(';')[0] + ' ' + linha.split(';')[tamanho_total]
            saida.write(linha.split(';')[0] + ' ' + linha.split(';')[tamanho_total]+'\n')
    except :
        pass