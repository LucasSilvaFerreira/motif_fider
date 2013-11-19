import re
from extract_seq import procurar_seq
arquivo=open('anotacao_ayupi.txt','r').read() #arquivo de anotacao grande gerado pela ayupi
hash={}
for linha in arquivo.split('\n'):
    #print linha
    if re.search('chr',linha):
        extrair=linha.split('\t')
       # print extrair[1],extrair[7],extrair[8]
        #print extrair[11]
        if extrair[1] in hash:
            pass
        else:
            #print '<'+extrair[11]+'>'
            if len(extrair[11])>6:
                chr= re.search(r'chr(\d+|X|Y):(\d+)-(\d+)',extrair[11])
                hash[extrair[1]]= chr.group(1),chr.group(2),chr.group(3),extrair[8]
            

count =0

for x in hash:
   # print hash[x][0],hash[x][1],hash[x][2],hash[x][3]
    #pass
    count=count + 1
    #print (count*100)/len(hash),'%'
    #print ((count*len(hash))/100),'%'
    hash[x] =hash[x],(procurar_seq(hash[x][0],hash[x][3],hash[x][1],hash[x][2]))
    print (count*100)/len(hash),'%'
# print hash[x][1]
# pass
import pickle
with open("hash_sequencias.hash", "wb") as handle:
    pickle.dump(hash, handle)


#abrindo
#with open('hash_sequencias.hash', 'rb') as handle_abrir:
#  minha_hash = pickle.load(handle_abrir)

#for key in minha_hash:
#    print key
