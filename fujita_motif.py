import simplehmm
import math
from motif_find import motif_finder
nome_saida='analisando_half_life'
teste = motif_finder('PFMDir_original/')
teste.set_pontas_porcentagem(15)
dados = open('Projeto/preparada_para_half_Life_busca.txt', 'r').read()
vetor_maior_valor = []
for search_maior_valor in dados.split('\n'):
    capturado = int(search_maior_valor.split(';')[2]) #numero de clusters
    vetor_maior_valor.append(capturado)

print len(vetor_maior_valor),max(vetor_maior_valor)
numero_clusters=max(vetor_maior_valor) #as classes devem ser numeros
print numero_clusters
for loop_cluster in range(0,numero_clusters+1):
    #print loop_cluster
    mega_string_cluster=''
    for cluster in dados.split('\n'):

        if int(cluster.split(';')[2])==loop_cluster:
            print loop_cluster,'-----------------------------------------------------'
            mega_string_cluster=mega_string_cluster+cluster.split(';')[1]+'\n'

    lncrna_train = mega_string_cluster
    print lncrna_train
    treinar = []
    finalizando = 0
    classificar_vetor = []
    for lncRNA in lncrna_train.split('\n'):
        lncRNA = lncRNA.upper()
        organizar, t, nomes, train, classificar = teste.procurar(lncRNA)
        #print classificar
        teste_vetor = []

        train = sorted(train)
        classificado_testar = sorted(classificar)

        for pegar_nomes in classificado_testar:
            #print pegar_nomes[1]
            teste_vetor.append(pegar_nomes[1])
            #print finalizando
        finalizando += 1
        #print classificado_testar
        print train
        if len(train) > 1:
            classificar_vetor.append(teste_vetor)
            treinar.append(train)

    print classificar_vetor
    print(teste.get_dir())

    #teste.set_pontas_porcentagem(15)
    #print(teste.get_pontas())


    #organizar
    #print (organizar[0])
    #print(sorted(organizar)) # esse comando deve ser feito usando o primeiro objeto ZERO e nao UM
    print (sorted(train))
    test_hmm_states = ['1', '3', '2']
    #test_hmm_observ=[]
    test_hmm = simplehmm.hmm('15 porcento lncRNA', test_hmm_states, nomes)
    #print test_hmm_observ
    '''
    temos que colocar todos os arquivos train dentro da tabela com o append por meio de um FOR
    A TABELA DE TREINAMENTO TEM QUE SAIR ORGANIZADA E NaO ESTa
    '''


    #treinar.append(train)
    print '---------------------', treinar, '---------------------------------'
    #print test_hmm.check_prob()
    test_hmm.train(treinar, smoothing='absdiscount')
    #print test_hmm.check_prob()
    print test_hmm.print_hmm()
    if nome_saida =='':
        print ('De um nome para os arquivos de saida')
    test_hmm.save_hmm('resultados/'+nome_saida+'_'+str(loop_cluster)+"_cluster.hmm")
