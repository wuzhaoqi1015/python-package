import re
import os
def read_fasta(file):
	#Initializations
	seq=""
	seq_name=file.split(".")[0]+"_seq"+".txt"
	output=open(seq_name,"w")
	for line in open(file):
		if(">" in line):
			symbol=line
			num_0=re.split(r'\s',symbol)[0]
			num_1 = re.compile(">")
			number = num_1.sub('',num_0)
			describe=re.split(r'\s',symbol,1)[1]
			describe=describe.strip('\n')
		else:
			seq=seq+''+line
	seq=seq.replace("\n","")
	#Delete the '\n'
	print(seq,file=output)
	print("-"*55+"\n"+"Successfully read the FASTA file!"+"\n"+"-"*55)
	result=[number,describe,seq]
	return(result)