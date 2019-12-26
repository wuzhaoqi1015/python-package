import re
def read_genbank(file):
	#Initializations
	seq="";key=0;number="";describe=""
	seq_name=file.split(".")[0]+"_seq"+".txt"
	output=open(seq_name,"w")
	for line in open(file):
		if("ACCESSION" in line):
			number=line.split("\s")[0]
			number=number.replace("\n","")
		if("DEFINITION"in line):
			describe=line.split("\s")[0]
			describe=describe.replace("\n","")
			describe=describe.replace(".","")
		if("ORIGIN" in line):
			key=1
			continue
		if(key==1):
			seq=seq+''+line
		else:
			continue
	seq=re.sub('\d+', '', seq)
	seq=seq.replace("\n","")
	seq=seq.replace(" ","")
	seq=seq.replace("//","")
	#Delete \n
	print(seq.upper(),file=output)
	print("-"*55+"\n"+"Successfully read the GENBANK file!"+"\n"+"-"*55)
	result=[number,describe,seq.upper()]
	return(result)