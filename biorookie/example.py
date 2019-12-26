import biowu as wu
import os
os.mkdir("./example")
os.chdir("./example")
acc=["AJ534526","AJ534527"]
accf=[acc[0]+".fasta",acc[1]+".fasta"]
accg=[acc[0]+".gb",acc[1]+".gb"]
#1.download data
wu.download_ncbi(acc,"nucleotide",'fasta')
wu.download_ncbi(acc,"nucleotide",'gb')
#2.read the file of 'fasta'
a=wu.read_fasta(accf[0])
b=wu.read_fasta(accf[1])
#3.read the file of 'gb'
a=wu.read_genbank(accg[0])
b=wu.read_genbank(accg[1])
#4.Calculate base frequency
c=wu.analyse.base(a[2])
#5.Finding the reverse complementary sequence
d=wu.analyse.reverse_comple(b[2])
#6.Pairwise alignment
e=wu.alignment(a[2],b[2])


