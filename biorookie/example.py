import biorookie as rk
import os
os.mkdir("./example")
os.chdir("./example")
acc=["AJ534526","AJ534527"]
accf=[acc[0]+".fasta",acc[1]+".fasta"]
accg=[acc[0]+".gb",acc[1]+".gb"]
#1.download data
rk.download_ncbi(acc,"nucleotide",'fasta')
acc=["AJ534526","AJ534527"]
rk.download_ncbi(acc,"nucleotide",'gb')
#2.read the file of 'fasta'
a=rk.read_fasta(accf[0])
b=rk.read_fasta(accf[1])
#3.read the file of 'gb'
a2=rk.read_genbank(accg[0])
b2=rk.read_genbank(accg[1])
#4.Calculate base frequency
c=rk.analyse.base(a[2])
d=rk.analyse.base(b[2])
#5.Finding the reverse complementary sequence
e=rk.analyse.reverse_comple(a[2])
f=rk.analyse.reverse_comple(b[2])
#6.Pairwise alignment
g=rk.alignment(a[2],b[2])


