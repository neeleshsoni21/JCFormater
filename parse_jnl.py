def read_journal_list_file(fname):
	inf=open(fname,'r')
	lines=inf.readlines()
	journal_name={}

	for l in lines:
		if ((l[0]=='#')|(l[0]=="\n")):
			continue;
		toks=l.strip().split('\t\t');
		person_name=toks[0].split(' ')[1]
		journal=toks[1]

		if person_name in journal_name.keys():
			journal_name[person_name].append(journal)
		else:
			journal_name[person_name]=[journal]
	
	return journal_name

