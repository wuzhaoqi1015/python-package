import numpy as np
import pandas as pd
def alignment(file1,file2,score=[4,-5,-4]):
	outfile_name="result_align"+".txt"
	output=open(outfile_name,"w")
	if("." in file1):
		seq1=str(open(file1,"r"))
		seq2=str(open(file2,"r"))
	else:
		seq1=file1
		seq2=file2
	s1=""
	s2=""
	length_1=len(seq1)
	length_2=len(seq2)
	score_max=0
	score_table = {
			'A': {'A': score[0], 'G': score[1], 'C': score[1], 'T': score[1]},
			'G': {'A': score[1], 'G': score[0], 'C': score[1], 'T': score[1]},
			'C': {'A': score[1], 'G': score[1], 'C': score[0], 'T': score[1]},
			'T': {'A': score[1], 'G': score[1], 'C': score[1], 'T': score[0]}
			}
	score_matrix = np.zeros(shape= (length_2+1,length_1+1),dtype = int)
	def get_match_score(a1,a2):
		sscore=score_table[a1][a2]
		return sscore
	def get_matrix_max(ma):
		maxx=ma.max()
		for i in range(0,length_2+1):
			for j in range(0,length_1+1):
				if ma[i][j]==maxx:
					return (i,j)	
	for i in range(0,length_2+1):
		for j in range(0,length_1+1):
			if i == 0 or j == 0:
				score_matrix[i][j]=score[2]*(max(i,j))
			else:
				match=get_match_score(seq2[i-1],seq1[j-1])
				up_score = score_matrix[i-1][j]+score[2]
				left_score = score_matrix[i][j-1]+score[2]
				match_score = score_matrix[i-1][j-1]+match
				score_max= max(left_score,up_score,match_score)
				score_matrix[i][j]=score_max
	i=length_2
	j=length_1
	while(i>0 and j>0):
		match = get_match_score(seq2[i-1],seq1[j-1])
		if i>0 and j>0 and score_matrix[i][j] == score_matrix[i-1][j-1]+match:
			s1=s1+seq1[j-1]
			s2=s2+seq2[i-1]
			i=i-1
			j=j-1
			
		elif i>0 and score_matrix[i][j]==score_matrix[i-1][j]+score[2]:
			s1=s1+"-"
			s2=s2+seq2[i-1]
			i=i-1
		else:
			s1=s1+seq1[j-1]
			s2=s2+"-"
			j=j-1
	score_final=score_matrix.max()
	print("-"*30+"\n"+"Successfully alignment!"+"\n"+"-"*30)
	print("Alignment:")
	print(" "+"Sequence1:"+s1[::-1]+'\n'+" "+"Sequence2:"+s2[::-1]+"\n"+"-"*30)
	print("Dynamc programming matrix:")
	print(score_matrix)
	print("-"*30+"\n"+"Score:",score_final)
	print(file1[0]+"\n"+s1[::-1]+'\n'+file2[0]+"\n"+s2[::-1],file=output)
	return(s1[::-1],s2[::-1],score_final)
	

	
	
	
	
	
	