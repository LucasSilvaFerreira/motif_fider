import simplehmm
hmm_teste = simplehmm.hmm("mrna",['nada'],['nada'])
hmm_teste.load_hmm('mRNAsTRAIN.hmm')
hmm_teste.print_hmm()
hmm_teste.load_hmm('randomseq.hmm')
hmm_teste.print_hmm()