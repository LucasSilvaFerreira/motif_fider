import glob
import re
from Bio import Motif
from Bio.Seq import Seq
from Bio.Motif import Thresholds
import math
class motif_finder:
	def __init__(self, pfm_dir):
		'''
		LEMBRANDO: ALUMAS MODIFICACOES NO ARQUIVO Bio.Motif foram necessarias
		O arquivo de diretorio deve possuir um arquivo contendo o nome real e cOdigo de todos os motivos.
		Esse mesmo cOdigo deve existir no nome do arquivo.pfm
		Os Diretorio deve ser escrito com essa seguinte sintaxe: diretorio/diretorio/  
		A barra no final deve existir
		'''
		self.diretorio = pfm_dir
		print ("Motif criado em :" + self.diretorio)
		
	threshold=5	
	def set_threshold(self,threshold):
		'''
		Configure a threshold do que e considerado motivo default 5.0 representa 32x acima do background
		'''
		self.threshold=threshold
		
	
	
	pontas =15
	
	def get_pontas(self):
		print self.pontas
		return self.pontas	
		
	
	#diretorio=None
	def set_pontas_porcentagem(self,porcentagem):
		'''
		Configure a porcentagem do que e considerado extremidade da sequencia
		'''
		self.pontas=porcentagem
	
	
	def get_dir(self):
		'''
		Retorna o diretorio escolhido
		'''
		return self.diretorio
	def set_dir(self,novo_diretorio):
		'''
		troca o diretorio de arquivos PFM
		'''
		self.diretorio= novo_diretorio

	
	
	def procurar(self,sequencia_string):
		'''
		Retorno = vetor de resultados
			    tamanho da sequencia	
		'''
		files = glob.glob( self.diretorio + "*.pfm")
		motivos_finais=[]
		nomes = open( self.diretorio +"matrix_list.txt", 'r').read()
		nomes_vetor = nomes.split('\n')
		
		#print nomes_vetor
		# print files
		#motif = Motif.read(open("PFMDir/1026_10858445.pfm"), "jaspar-pfm")
		# motif.make_instances_from_counts() 3
		lista_motivos = []
		lista_nomes = []
		motivos_checar_repetidos = {}
		for motivo in files:
		
		
			#print motivo
			isolar_nome = re.search(r'(\d*_\d*)\.pfm$', motivo)
			
			isolado = isolar_nome.group(1)
			
			
			for n_pesquisa in nomes_vetor:
				isolado_pesquisa = n_pesquisa.split('\t')
				id_encontrado = isolado_pesquisa[0]
				# print '<'+n_pesquisa+'>'
				if (id_encontrado == isolado):
					#print isolado
					nome_recolocar = n_pesquisa.split('\t')[2].split('_')[1]
						
					
					if nome_recolocar in motivos_checar_repetidos:
						motivos_checar_repetidos[nome_recolocar] += 1
						#print ('ja encontrado')
					else:
						#print motivo
						motivos_checar_repetidos[nome_recolocar] = 1
						lista_motivos.append(Motif.read(open(motivo), "jaspar-pfm"))
						lista_nomes.append(nome_recolocar)
		sequencia = Seq(sequencia_string.upper())
		#print lista_nomes
		#print(len(lista_motivos))
		# print motif.has_counts
		# print motif.counts
		contador = 0
		for converter in lista_motivos:
			#print contador
			#print converter.instances
			
			converter.make_instances_from_counts()
			contador += 1	
		
		# print motif.
		# motif.weblogo("teste.bmp")
		
		tamanho_seq=len(sequencia_string)
		tss=((tamanho_seq*self.pontas)/100)
		three_end= tamanho_seq-tss
		print tss,three_end
		count_erro=0
		nome_contador=0
		saida_hmm=[]
		classificar=[]
		motif_Contador =1
		for procura in lista_motivos:
			print  ("---------------->"  + str(motif_Contador) + "<---------------------------------------")
			#print (procura)
			motif_Contador += 1
			#for position_s,score_p in procura.search_pwm(sequencia,threshold=1):
				##print procura
				#print math.fabs(position_s),score_p,"teste"
				#print lista_nomes[nome_contador]
				#print '-----------------'
				#print count_errorandomseq.txt
				#count_erro=+ 1
			#print "----------------------------------------------"
			for pos, seq in procura.search_pwm(sequencia,threshold=10):
				#print teste
				#print "entrou"
				posicao=""
				if (pos<=tss):
					posicao="1"
				if (pos>=three_end)	:
					posicao="3"
				if (pos>tss and pos<three_end):
					posicao="2"
				motivos_finais.append((pos, seq ,lista_nomes[nome_contador],posicao))	
				#motivos_finais.append(str(pos) + "\t" + seq + "\t" +lista_nomes[nome_contador]+"\t"+posicao)
				saida_hmm.append((posicao,lista_nomes[nome_contador]))
				ordenar_teste=(posicao,lista_nomes[nome_contador])
				ordenar_teste=sorted(sorted(ordenar_teste))
				classificar.append(ordenar_teste)
				#print (str(pos) + "\t" + seq + "\t" +lista_nomes[nome_contador]+"\t"+ str(posicao))
				
			nome_contador+=1
		
		return (motivos_finais,tamanho_seq,lista_nomes,saida_hmm,classificar)
	#return tamanho_seq	
		# print(motif.search_instances(sequencia)
		
		# print(motif.counts)
		# print(sequencia.tostring())
		
