import re
saida=open('sequencias_encontradas.txt','w')
arquivo = open('/home/lucas/lucas/motif_fider/Pearson.txt_com_seq_merda.txt', 'r').read()
arquivo = re.sub(',', ';', arquivo)
arquivo = re.sub(' ', '', arquivo)
arquivo = re.sub('\'', '', arquivo)
arquivo = re.sub('\(', '', arquivo)
for linha in arquivo.split(')'):
    try:
        if len(linha.split(';')[106])>1 and not re.search('N',linha.split(';')[106]):
            print linha.split(';')[0] + ' ' + linha.split(';')[106]
            saida.write(linha.split(';')[0] + ' ' + linha.split(';')[106]+'\n')
    except :
        pass