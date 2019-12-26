import re
def base(file):
	if("." in file):
		line=open(file,"r")
		outfile_name=file.split("_")[0]+"_base"+".txt"
	elif(type(file)==str):
		line=file
		outfile_name="_base"+".txt"
	elif(type(file)==list):
		line=file[2]
		outfile_name=file[0]+"_base"+".txt"
	else:
		return "Please enter the correct parameters!"
	#Initializations
	line=line.upper()
	seq="";sum_a=0;sum_t=0;sum_c=0;sum_g=0
	output=open(outfile_name,"w")
	#Call the built-in function to count the number of each base.
	sum_a=line.count("A")+sum_a
	sum_t=line.count("T")+sum_t
	sum_c=line.count("C")+sum_c
	sum_g=line.count("G")+sum_g
	sum=sum_a+sum_t+sum_c+sum_g
	seq=seq+''+line
	seq=seq.replace("\n","")
	#Delete \n
	result={"A":(sum_a/sum),"T":(sum_t/sum),"C":(sum_c/sum),"G":(sum_g/sum)}
	print(seq,file=output)
	print("-"*55+"\n"+"Base ratio:")
	print("%4f" % (sum_a/sum),"%4f" % (sum_t/sum),"%4f" % (sum_c/sum),"%4f" % (sum_g/sum)+"\n"+"-"*55)
	return(result)
#This function realizes base complementation.
def complement(seq):
	seq = seq.upper()
	#For the first time, replace with lowercase letters, indicating that the base has been replaced to prevent repeated replacement.
	seq = seq.replace("A","t")		
	seq = seq.replace("T","a")		
	seq = seq.replace("C","g")		
	seq = seq.replace("G","c")		
	return seq.upper()
def reverse_comple(file):
	seq_name="_rc"+".txt"
	output=open(seq_name,"w")
	if("." in file):
		line=open(file,"r")
		newline=complement(line)[::-1]
	else:
		line=file
		newline=complement(line)[::-1]
	newline=newline.replace("\n","")
	print(newline,file=output)
	return(newline)
	