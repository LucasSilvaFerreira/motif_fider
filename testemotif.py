import simplehmm
import math

from motif_find import motif_finder
teste= motif_finder('/home/lucas/lucas/motif_fider/PFMDir_original/')
teste.set_pontas_porcentagem(15)
lncrna_train=open('lnc_maiores_6k_menosres_11_complementar.txt','r').read()

treinar=[]
finalizando=0 
classificar_vetor=[]
for lncRNA in lncrna_train.split('\n'):
      lncRNA=lncRNA.upper()
      organizar,t,nomes,train,classificar=teste.procurar(lncRNA)
      #print classificar
      teste_vetor=[] 
      
      train=sorted(train)
      classificado_testar=sorted(classificar)
      
      for pegar_nomes in classificado_testar:
                  print pegar_nomes[1]
                  teste_vetor.append(pegar_nomes[1])
      #print finalizando
      finalizando +=1
      #print classificado_testar
      print train
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
test_hmm_states = ['1','3', '2']
#test_hmm_observ=[]	
test_hmm = simplehmm.hmm('15 porcento lncRNA', test_hmm_states, nomes)
#print test_hmm_observ
'''
temos que colocar todos os arquivos train dentro da tabela com o append por meio de um FOR
A TABELA DE TREINAMENTO TEM QUE SAIR ORGANIZADA E NaO ESTa
'''


#treinar.append(train)
print '---------------------',treinar,'---------------------------------'
#print test_hmm.check_prob()
test_hmm.train(treinar, smoothing='absdiscount')
#print test_hmm.check_prob()
#print test_hmm.print_hmm()
#test_hmm.save_hmm("15_lncrna.hmm")

lnc_hmm = simplehmm.hmm('LncRNA',  ['dummy'], ['dummy'])
lnc_hmm.load_hmm('15_lncrna.hmm')
lnc_hmm.print_hmm()  # Print it out

mrna_hmm = simplehmm.hmm('mRNA',  ['dummy'], ['dummy'])
mrna_hmm.load_hmm('15_mrna.hmm')
mrna_hmm.print_hmm()  # Print it out


for teste in classificar_vetor:
      #print 'lnc',lnc_hmm.viterbi(teste)
      #print 'mrna',mrna_hmm.viterbi(teste)
      print math.log(lnc_hmm.viterbi(teste)[1]/mrna_hmm.viterbi(teste)[1])
     #pass 
      
      


