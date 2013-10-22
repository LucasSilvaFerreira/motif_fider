import re
def extrair(file_in,file_out):
      '''
      file_in = arquivo fasta entrada
      file_out=arquivo fasta saida
      '''
      saida= open (file_out,'w')
      arquivo=open(file_in,'r').read()
      n_linhas=1
      for sequencia in re.split(r'>.*\n',arquivo):
            print n_linhas
            saida.write(re.sub('\n', '',sequencia)+'\n')
            n_linhas += 1


extrair("lncipedia.fasta.txt","lncrna_fasta_processado.txt")