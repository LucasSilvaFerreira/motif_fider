import re
from extract_seq import procurar_seq

anotacao = open('anotacao_ayupi.txt', 'r').read().split('Geneid_NOV_2012_revised_ABR_2013')[1]
cluster_file = open('Projeto/Pearson_backup.txt', 'r').read()
saida = open('Pearson.txt_com_seq.txt', 'w')
for linha in cluster_file.split('\n'):
    #print linha.split(';')[0]
    for x in anotacao.split('\n'):
        try:
            if (re.search(linha.split(';')[0], x)):
                fita = x.split('\t')[8]
                cromossomo = x.split('\t')[11].split('chr')[1].split(':')[0]
                start = x.split('\t')[11].split('chr')[1].split(':')[1].split('-')[0]
                end = x.split('\t')[11].split('chr')[1].split(':')[1].split('-')[1]
                sequencia_recuperada = procurar_seq(cromossomo, fita, start, end)
                #processar valores para jogar em procurar

                saida_str= linha, x.split('\t')[5], x.split('\t')[8], x.split('\t')[11], str(sequencia_recuperada),'\n'
                print saida_str
                saida.write(str(saida_str))
                #(linha, x.split('\t')[5], x.split('\t')[8], x.split('\t')[11], str(sequencia_recuperada),'\n')
        except:
            #print 'error on :',x
            pass

saida.close()