#import the modul
from Bio import Entrez
from Bio import SeqIO
import sys
import os
def download_ncbi(acc,debase,type):
	Entrez.email="1027127497@qq.com"
	length=len(acc)
	while(length>0):
		catch=Entrez.efetch(db=debase,id=acc[length-1],rettype=type)
		data=SeqIO.read(catch,type)
		newfile_name=acc[length-1]+'.'+type
		newfile=open(newfile_name,'w')
		SeqIO.write(data,newfile,type)
		newfile.close
		acc.pop()
		length=length-1
		