
fasta = open('MECP2.hifi_reads.fasta', 'r')
output = open('MECP2.hifi_reads.fasta.length.txt','w')
output2 = open('MECP2.hifi_reads.length.fasta', 'w')

output.write('read_name'  + '\t' + 'length' + '\n')
n=0
newline=''
read_dic = {}
first=True
for line in fasta:
    if line[0] == '>':

        if first:
            readid=line.rstrip()[1:]
            first=False

        else:
            read_dic[readid] = [len(newline),newline]
            output.write(readid +'\t' +str(len(newline))+'\n')
            newline=''
            readid=line.rstrip()[1:]
            continue
    else:
        newline += line.rstrip()
        continue



for key,value in read_dic.items():
	if value[0] in range(1484,1491):
		output2.write('>' +key +'\n')
		output2.write(value[1] + '\n')
		continue
	else:	continue
