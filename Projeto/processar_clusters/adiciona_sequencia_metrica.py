import re
'''
cria arquivos adicionando sequencias aos arquivos de metrica
'''
nome_metrica='out_my.groups_hr_ids.txt'
saida=open('sequencias_'+nome_metrica,'w')
sequencia_data =open('sequencias_encontradas.txt','r').read()
metrica = open(nome_metrica,'r').read()
for seq in sequencia_data.split('\n'):
    #print seq
    for query in metrica.split('\n'):
        #print query
        if re.match(seq.split(' ')[0],query):
            print seq.split(' ')[0]+';'+seq.split(' ')[1]+';'+query.split('\t')[1]
            saida.write(seq.split(' ')[0]+';'+seq.split(' ')[1]+';'+query.split('\t')[1]+'\n')

saida.close()