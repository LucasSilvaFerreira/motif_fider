from Bio import Entrez, SeqIO
Entrez.email = "lucas.ralley@hotmail.com"     
def procurar_seq(id_in,strand_in,seq_start_in,seq_stop_in):
      
      '''strand - what strand of DNA to show (1 = plus or 2 = minus)
      Id_in= number of human chormosome
      seq_start - show sequence starting from this base number
      seq_stop - show sequence ending on this base number
      
      '''
      strand_in=str(strand_in)
      if strand_in=="+":
            strand_in=1  
      if strand_in=="-":
            strand_in=2  
      
      if str(id_in).upper()=='X':
            id_in = 22
      if str(id_in).upper()=='Y':
            id_in = 23     
      id_in=int(id_in)
      if id_in>23:
            print "this is not one human chromosome GI (22=x 23=y)"
      cromossomos_humanos=str(74273681-int(id_in))
      
      
     # print cromossomos_humanos
      
      handle = Entrez.efetch(db="nucleotide", 
                             id=cromossomos_humanos, 
                             rettype="fasta", 
                             strand=strand_in, 
                             seq_start=seq_start_in, 
                             seq_stop=seq_stop_in)
      record = SeqIO.read(handle, "fasta")
      handle.close()
      return record.seq

#print procurar_seq('x', '+', 990, 1000)

