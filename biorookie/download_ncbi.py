#import the modul
from Bio import Entrez
from Bio import SeqIO
import sys
import os
#Set up the email in NCBI.Data can only be fetched if it is set.
def download_ncbi(acc,debase="nucleotide",type='fasta'):
	Entrez.email="1027127497@qq.com" 
	length=len(acc)
	while(length>0):
		catch=Entrez.efetch(db=debase,id=acc[length-1],rettype=type)
		#Catch the data from NCBI.
		data=SeqIO.read(catch,type)
		#Read the file into 'data'.
		newfile_name=acc[length-1]+'.'+type
		#Paste the filename we open in next.
		newfile=open(newfile_name,'w')
		#Open a new file which used to write the data.
		SeqIO.write(data,newfile,type)
		#Write the data into the 'newfile' which we open before.
		newfile.close
		acc.pop()
		length=length-1