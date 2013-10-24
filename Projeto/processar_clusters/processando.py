import re
nome='my.groups_hr_ids.txt'
arquivo=open(nome,'r').read()
saida=open('out_'+nome,'w')
for grupo in arquivo.split('[['):
   # print grupo.split("]]")[0]

    grupo=re.sub('\[\d*\]','',grupo)
    grupo=re.sub(' |\n',';',grupo)
    grupo=re.sub(';;',';',grupo)
    grupo=re.sub('\"','',grupo)
    grupo=re.sub(';;',';',grupo)

    #print grupo
    grupo_x= grupo.split(']]')[0]

    #grupo_x= grupo.split(']]')[0]
    for x in grupo.split(';'):
        if re.match('\w',x) and not re.match('\d+]]',x):
            print x,grupo.split(']]')[0]
            saida.write(x+'\t'+grupo.split(']]')[0]+'\n')
saida.close()