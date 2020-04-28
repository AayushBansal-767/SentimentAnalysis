f=open("dataset.txt","r").read()
n,p=[],[]
n=open("neg.txt","a")
p=open("pos.txt","a")

for l in f.split('\n'):
	if l.split('\t')[1]=='0':
		n.write(l.split('\t')[0]+"\n")
	if l.split('\t')[1]=='1':
		p.write(l.split('\t')[0]+"\n")