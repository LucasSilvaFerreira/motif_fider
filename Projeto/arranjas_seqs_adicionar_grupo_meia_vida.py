import re
saida=open('grupos_separacao_em_horas_sequencias_encontradas_half_life.txt','w')
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
            grupo=linha.split(';')[1]
            grupo=round(float(grupo))
            print linha.split(';')[0] + ' ' + linha.split(';')[tamanho_total]+ ' ' + str(grupo)
            saida.write(linha.split(';')[0] + ';' + linha.split(';')[tamanho_total]+';'+ str(int(grupo))+'\n')
    except :
        pass