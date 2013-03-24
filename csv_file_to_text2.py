import sys
import tokenize
from collections import OrderedDict
import csv
import random

fname=sys.argv[1]
inf=open(fname,'r')

articles=OrderedDict()

with open(fname, 'rb') as csvfile:
	csvreader=csv.reader(csvfile,delimiter=',')
	next(csvreader)
	for l in csvreader:
		key=l[1];
		if key not in articles.keys():
			articles[key]=OrderedDict()
			articles[key]=[l]
		else:
			articles[key].append(l)

from parse_jnl import read_journal_list_file
journal_name_map=read_journal_list_file('Assigned_Journals.txt')


wlines=""
for key,jname in random.sample(journal_name_map.items(),len(journal_name_map.keys())):
	#print key,jname
	#for key,value in random.sample(articles.items(),len(articles.keys())):
	wlines+="\n################################################\n"
	wlines+="PRESENTER: "+key+'\n'
	wlines+="################################################\n"
	wlines+="\n".join(jname)+"\n"
	wlines+="______________________________________\n"
	wlines+="\n"
	
	try:
		value=articles[key]
		counter=1
		for val in value:
			wlines+="("+str(counter)+")"+"\n"
			wlines+="JOURNAL: "+val[2]+'\n'
			wlines+="TITLE: "+val[4]+'\n'
			wlines+="AUTHORS: "+val[5]+'\n'
			wlines+="VOLUME: "+val[3]+'\n'
			wlines+="SUMMARY: \n"+'\t '+'\n\t '.join(val[7].split('\n'))+'\n'
			wlines+="\nWEB LINK: "+val[8]+'\n'
			wlines+="WHO SHOULD READ: "+val[9]+'\n'
			wlines+="_______________________________________________________\n"
			wlines+="\n"
			
			counter+=1;

		wlines+="\n\n"
	except:
		wlines+="Papers Not Uploaded "+'\n'
		wlines+="______________________________________\n"
		wlines+="\n\n\n"

outf=open('Journal_Club_papers.txt','w')
outf.writelines(wlines)
outf.close()