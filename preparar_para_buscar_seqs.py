__author__ = 'Lucas'
#prepara para buscar seq no arquivo intersect_cluster_anotacao_para_apenas_um_grupo.py
arquivo=open('half_life_AS_menor 3h.txt','r').read()
saida=open('half_life_AS_menor_3h_preparada.txt','w')
for probe in arquivo.split('\n'):
    #print probe
    if  probe.find('File Name'):
        print probe.split('\t')[0],probe.split('\t')[1],probe.split('\t')[8]
        saida.write(probe.split('\t')[0]+';'+probe.split('\t')[1]+';'+probe.split('\t')[8]+'\n')
            #print 'teste',cut_probe
            #print cut_probe[0],cut_probe[1],cut_probe[5]