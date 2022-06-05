import pysam

#GABBR2
#bamfile = pysam.AlignmentFile('/Users/jeongha/Dropbox/JH/2021/sat_mut/pacbio/20211214_deeper_seq/Gabbr2_sat_mu.hifi_reads.length.sorted.bam', 'rb')
#output = open('/Users/jeongha/Dropbox/JH/2021/sat_mut/pacbio/20211214_deeper_seq/Gabbr2_sat_mu.hifi_reads.length.sorted.bam.ORFcall_v10_indel.txt','w')
#ref = 'ATGGCTTCCCCGCGGAGCTCCGGGCAGCCCGGGCCGCCGCCGCCGCCGCCACCGCCGCCCGCGCGCCTGCTACTGCTACTGCTGCTGCCGCTGCTGCTGCCTCTGGCGCCCGGGGCCTGGGGCTGGGCGCGGGGCGCCCCCCGGCCGCCGCCCAGCAGCCCGCCGCTCTCCATCATGGGCCTCATGCCGCTCACCAAGGAGGTGGCCAAGGGCAGCATCGGGCGCGGTGTGCTCCCCGCCGTGGAACTGGCCATCGAGCAGATCCGCAACGAGTCACTCCTGCGCCCCTACTTCCTCGACCTGCGGCTCTATGACACGGAGTGCGACAACGCAAAAGGGTTGAAAGCCTTCTACGATGCAATAAAATACGGGCCTAACCACTTGATGGTGTTTGGAGGCGTCTGTCCATCCGTCACATCCATCATTGCAGAGTCCCTCCAAGGCTGGAATCTGGTGCAGCTTTCTTTTGCTGCAACCACGCCTGTTCTAGCCGATAAGAAAAAATACCCTTATTTCTTTCGGACCGTCCCATCAGACAATGCGGTGAATCCAGCCATTCTGAAGTTGCTCAAGCACTACCAGTGGAAGCGCGTGGGCACGCTGACGCAAGACGTTCAGAGGTTCTCTGAGGTGCGGAATGACCTGACTGGAGTTCTGTATGGCGAGGACATTGAGATTTCAGACACCGAGAGCTTCTCCAACGATCCCTGTACCAGTGTCAAAAAGCTGAAGGGGAATGATGTGCGGATCATCCTTGGCCAGTTTGACCAGAATATGGCAGCAAAAGTGTTCTGTTGTGCATACGAGGAGAACATGTATGGTAGTAAATATCAGTGGATCATTCCGGGCTGGTACGAGCCTTCTTGGTGGGAGCAGGTGCACACGGAAGCCAACTCATCCCGCTGCCTCCGGAAGAATCTGCTTGCTGCCATGGAGGGCTACATTGGCGTGGATTTCGAGCCCCTGAGCTCCAAGCAGATCAAGACCATCTCAGGAAAGACTCCACAGCAGTATGAGAGAGAGTACAACAACAAGCGGTCAGGCGTGGGGCCCAGCAAGTTCCACGGGTACGCCTACGATGGCATCTGGGTCATCGCCAAGACACTGCAGAGGGCCATGGAGACACTGCATGCCAGCAGCCGGCACCAGCGGATCCAGGACTTCAACTACACGGACCACACGCTGGGCAGGATCATCCTCAATGCCATGAACGAGACCAACTTCTTCGGGGTCACGGGTCAAGTTGTATTCCGGAATGGGGAGAGAATGGGGACCATTAAATTTACTCAATTTCAAGACAGCAGGGAGGTGAAGGTGGGAGAGTACAACGCTGTGGCCGACACACTGGAGATCATCAATGACACCATCAGGTTCCAAGGATCCGAACCACCAAAAGACAAGACCATCATCCTGGAGCAGCTGCGGAAGATCTCCCTACCTCTCTACAGCATCCTCTCTGCCCTCACCATCCTCGGGATGATCATGGCCAGTGCTTTTCTCTTCTTCAACATCAAGAACCGGAATCAGAAGCTCATAAAGATGTCGAGTCCATACATGAACAACCTTATCATCCTTGGAGGGATGCTCTCCTATGCTTCCATATTTCTCTTTGGCCTTGATGGATCCTTTGTCTCTGAAAAGACCTTTGAAACACTTTGCACCGTCAGGACCTGGATTCTCACCGTGGGCTACACGACCGCTTTTGGGGCCATGTTTGCAAAGACCTGGAGAGTCCACGCCATCTTCAAAAATGTGAAAATGAAGAAGAAGATCATCAAGGACCAGAAACTGCTTGTGATCGTGGGGGGCATGCTGCTGATCGACCTGTGTATCCTGATCTGCTGGCAGGCTGTGGACCCCCTGCGAAGGACAGTGGAGAAGTACAGCATGGAGCCGGACCCAGCAGGACGGGATATCTCCATCCGCCCTCTCCTGGAGCACTGTGAGAACACCCATATGACCATCTGGCTTGGCATCGTCTATGCCTACAAGGGACTTCTCATGTTGTTCGGTTGTTTCTTAGCTTGGGAGACCCGCAACGTCAGCATCCCCGCACTCAACGACAGCAAGTACATCGGGATGAGTGTCTACAACGTGGGGATCATGTGCATCATCGGGGCCGCTGTCTCCTTCCTGACCCGGGACCAGCCCAATGTGCAGTTCTGCATCGTGGCTCTGGTCATCATCTTCTGCAGCACCATCACCCTCTGCCTGGTATTCGTGCCGAAGCTCATCACCCTGAGAACAAACCCAGATGCAGCAACGCAGAACAGGCGATTCCAGTTCACTCAGAATCAGAAGAAAGAAGATTCTAAAACGTCCACCTCGGTCACCAGTGTGAACCAAGCCAGCACATCCCGCCTGGAGGGCCTACAGTCAGAAAACCATCGCCTGCGAATGAAGATCACAGAGCTGGATAAAGACTTGGAAGAGGTCACCATGCAGCTGCAGGACACACCAGAAAAGACCACCTACATTAAACAGAACCACTACCAAGAGCTCAATGACATCCTCAACCTGGGAAACTTCACTGAGAGCACAGATGGAGGAAAGGCCATTTTAAAAAATCACCTCGATCAAAATCCCCAGCTACAGTGGAACACAACAGAGCCCTCTCGAACATGCAAAGATCCTATAGAAGATATAAACTCTCCAGAACACATCCAGCGTCGGCTGTCCCTCCAGCTCCCCATCCTCCACCACGCCTACCTCCCATCCATCGGAGGCGTGGACGCCAGCTGTGTCAGCCCCTGCGTCAGCCCCACCGCCAGCCCCCGCCACAGACATGTGCCACCCTCCTTCCGAGTCATGGTCTCGGGCCTGTAA'

# MECP2
bamfile =pysam.AlignmentFile('/Users/jeongha/Dropbox/JH/2022/saturation_mutagenesis/MECP2/pacbio_220605/MECP2.hifi_reads.length.sorted.bam', 'rb')
output = open('/Users/jeongha/Dropbox/JH/2022/saturation_mutagenesis/MECP2/pacbio_220605/MECP2.hifi_reads.length.sorted.bam.ORFcall_v10_indel.txt','w')
ref = 'ATGGTAGCTGGGATGTTAGGGCTCAGGGAAGAAAAGTCAGAAGACCAGGACCTCCAGGGCCTCAAGGACAAACCCCTCAAGTTTAAAAAGGTGAAGAAAGATAAGAAAGAAGAGAAAGAGGGCAAGCATGAGCCCGTGCAGCCATCAGCCCACCACTCTGCTGAGCCCGCAGAGGCAGGCAAAGCAGAGACATCAGAAGGGTCAGGCTCCGCCCCGGCTGTGCCGGAAGCTTCTGCCTCCCCCAAACAGCGGCGCTCCATCATCCGTGACCGGGGACCCATGTATGATGACCCCACCCTGCCTGAAGGCTGGACACGGAAGCTTAAGCAAAGGAAATCTGGCCGCTCTGCTGGGAAGTATGATGTGTATTTGATCAATCCCCAGGGAAAAGCCTTTCGCTCTAAAGTGGAGTTGATTGCGTACTTCGAAAAGGTAGGCGACACATCCCTGGACCCTAATGATTTTGACTTCACGGTAACTGGGAGAGGGAGCCCCTCCCGGCGAGAGCAGAAACCACCTAAGAAGCCCAAATCTCCCAAAGCTCCAGGAACTGGCAGAGGCCGGGGACGCCCCAAAGGGAGCGGCACCACGAGACCCAAGGCGGCCACGTCAGAGGGTGTGCAGGTGAAAAGGGTCCTGGAGAAAAGTCCTGGGAAGCTCCTTGTCAAGATGCCTTTTCAAACTTCGCCAGGGGGCAAGGCTGAGGGGGGTGGGGCCACCACATCCACCCAGGTCATGGTGATCAAACGCCCCGGCAGGAAGCGAAAAGCTGAGGCCGACCCTCAGGCCATTCCCAAGAAACGGGGCCGAAAGCCGGGGAGTGTGGTGGCAGCCGCTGCCGCCGAGGCCAAAAAGAAAGCCGTGAAGGAGTCTTCTATCCGATCTGTGCAGGAGACCGTACTCCCCATCAAGAAGCGCAAGACCCGGGAGACGGTCAGCATCGAGGTCAAGGAAGTGGTGAAGCCCCTGCTGGTGTCCACCCTCGGTGAGAAGAGCGGGAAAGGACTGAAGACCTGTAAGAGCCCTGGGCGGAAAAGCAAGGAGAGCAGCCCCAAGGGGCGCAGCAGCAGCGCCTCCTCACCCCCCAAGAAGGAGCACCACCACCATCACCACCACTCAGAGTCCCCAAAGGCCCCCGTGCCACTGCTCCCACCCCTGCCCCCACCTCCACCTGAGCCCGAGAGCTCCGAGGACCCCACCAGCCCCCCTGAGCCCCAGGACTTGAGCAGCAGCGTCTGCAAAGAGGAGAAGATGCCCAGAGGAGGCTCACTGGAGAGCGACGGCTGCCCCAAGGAGCCAGCTAAGACTCAGCCCGCGGTTGCCACCGCCGCCACGGCCGCAGAAAAGTACAAACACCGAGGGGAGGGAGAGCGCAAAGACATTGTTTCATCCTCCATGCCAAGGCCAAACAGAGAGGAGCCTGTGGACAGCCGGACGCCCGTGACCGAGAGAGTTAGCTGA'

#TP53
# bamfile = pysam.AlignmentFile('/Users/jeongha/Dropbox/JH/2021/sat_mut/pacbio/TP53/p53_sat_mu.aligned.sorted.bam', 'rb')
# output = open('/Users/jeongha/Dropbox/JH/2021/sat_mut/pacbio/TP53/p532_sat_mu.aligned.sorted.bam.ORFcall_v10_indel.txt','w')
# ref= 'ATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCTGTCCCTTCCCAGAAAACCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTCCCCTGCCCTCAACAAGATGTTTTGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACACCCCCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGCCCCCACCATGAGCGCTGCTCAGATAGCGATGGTCTGGCCCCTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGACAGAAACACTTTTCGACATAGTGTGGTGGTGCCCTATGAGCCGCCTGAGGTTGGCTCTGACTGTACCACCATCCACTACAACTACATGTGTAACAGTTCCTGCATGGGCGGCATGAACCGGAGGCCCATCCTCACCATCATCACACTGGAAGACTCCAGTGGTAATCTACTGGGACGGAACAGCTTTGAGGTGCGTGTTTGTGCCTGTCCTGGGAGAGACCGGCGCACAGAGGAAGAGAATCTCCGCAAGAAAGGGGAGCCTCACCACGAGCTGCCCCCAGGGAGCACTAAGCGAGCACTGCCCAACAACACCAGCTCCTCTCCCCAGCCAAAGAAGAAACCACTGGATGGAGAATATTTCACCCTTCAGATCCGTGGGCGTGAGCGCTTCGAGATGTTCCGAGAGCTGAATGAGGCCTTGGAACTCAAGGATGCCCAGGCTGGGAAGGAGCCAGGGGGGAGCAGGGCTCACTCCAGCCACCTGAAGTCCAAAAAGGGTCAGTCTACCTCCCGCCATAAAAAACTCATGTTCAAGACAGAAGGGCCTGACTCAGACTGA'

#SPOP
# bamfile = pysam.AlignmentFile('/Users/jeongha/Dropbox/JH/2021/sat_mut/pacbio/SPOP/SPOP_sat_mu.sorted.bam', 'rb')
# output = open('/Users/jeongha/Dropbox/JH/2021/sat_mut/pacbio/SPOP/SPOP_sat_mu.sorted.bam.ORFcall_v10_indel.txt','w')
# ref= 'ATGTCAAGGGTTCCAAGTCCTCCACCTCCGGCAGAAATGTCGAGTGGCCCCGTAGCTGAGAGTTGGTGCTACACACAGATCAAGGTAGTGAAATTCTCCTACATGTGGACCATCAATAACTTTAGCTTTTGCCGGGAGGAAATGGGTGAAGTCATTAAAAGTTCTACATTTTCATCAGGAGCAAATGATAAACTGAAATGGTGTTTGCGAGTAAACCCCAAAGGGTTAGATGAAGAAAGCAAAGATTACCTGTCACTTTACCTGTTACTGGTCAGCTGTCCAAAGAGTGAAGTTCGGGCAAAATTCAAATTCTCCATCCTGAATGCCAAGGGAGAAGAAACCAAAGCTATGGAGAGTCAACGGGCATATAGGTTTGTGCAAGGCAAAGACTGGGGATTCAAGAAATTCATCCGTAGAGATTTTCTTTTGGATGAGGCCAACGGGCTTCTCCCTGATGACAAGCTTACCCTCTTCTGCGAGGTGAGTGTTGTGCAAGATTCTGTCAACATTTCTGGCCAGAATACCATGAACATGGTAAAGGTTCCTGAGTGCCGGCTGGCAGATGAGTTAGGAGGACTGTGGGAGAATTCCCGGTTCACAGACTGCTGCTTGTGTGTTGCCGGCCAGGAATTCCAGGCTCACAAGGCTATCTTAGCAGCTCGTTCTCCGGTTTTTAGTGCCATGTTTGAACATGAAATGGAGGAGAGCAAAAAGAATCGAGTTGAAATCAATGATGTGGAGCCTGAAGTTTTTAAGGAAATGATGTGCTTCATTTACACGGGGAAGGCTCCAAACCTCGACAAAATGGCTGATGATTTGCTGGCAGCTGCTGACAAGTATGCCCTGGAGCGCTTAAAGGTCATGTGTGAGGATGCCCTCTGCAGTAACCTGTCCGTGGAGAACGCTGCAGAAATTCTCATCCTGGCCGACCTCCACAGTGCAGATCAGTTGAAAACTCAGGCAGTGGATTTCATCAACTATCATGCTTCGGATGTCTTGGAGACCTCTGGGTGGAAGTCAATGGTGGTGTCACATCCCCACTTGGTGGCTGAGGCATACCGCTCTCTGGCTTCAGCACAGTGCCCTTTTCTGGGACCCCCACGCAAACGCCTGAAGCAATCCTAA'

cigar_dic = {0:'M', 1:'I',2:'D',3:'N',4:'S',5:'H',6:'P',7:'=',8:'X',9:'B'}
codon_dic = {'G': ['ggt', 'ggc', 'gga', 'ggg'], 'A': ['gct', 'gcc', 'gca', 'gcg'],
             'V': ['gtt', 'gtc', 'gta', 'gtg'], 'L': ['tta', 'ttg', 'ctt', 'ctc', 'cta', 'ctg'],
             'I': ['att', 'atc', 'ata'], 'M': ['atg'], 'F': ['ttt', 'ttc'], 'W': ['tgg'],
             'P': ['cct', 'ccc', 'cca', 'ccg'], 'S': ['tct', 'tcc', 'tca', 'tcg', 'agt', 'agc'],
             'T': ['act', 'acc', 'aca', 'acg'], 'C': ['tgt', 'tgc'], 'Y': ['tat', 'tac'], 'N': ['aat', 'aac'],
             'Q': ['caa', 'cag'], 'D': ['gat', 'gac'], 'E': ['gaa', 'gag'], 'K': ['aaa', 'aag'],
             'R': ['cgt', 'cgc', 'cga', 'cgg', 'agg', 'aga'], 'H': ['cat', 'cac'], '*': ['taa', 'tag', 'tga']}
ref_aa = ''
refaa =''
temp = ''
for n in range(0,len(ref)):
    if n%3 !=2:
        temp += ref[n]
        continue
    else:
        temp += ref[n]
        for aa, codon in codon_dic.items():
            if temp.lower() in codon:
                ref_aa += aa +'\t'
                refaa +=aa
                break
            else:   continue
        temp =''
codon_ins=0
output.write('readid' +'\t' + 'orf_length' + '\t' + 'ins' +'\t' + 'del' + '\t' + 'fs' +'\t' +'#aachange'+'\t' '#aalength'+'\t' + 'comment'+'\t' + 'barcode' +'\t' + 'variant:variant' + '\n')

total_read = 0
taaasis1_read =0
noGCGGCC = 0
#length_read =0
backward_read =0
forward_read =0
for read in bamfile.fetch():
    total_read +=1
    readid = read.query_name
    if readid =='m64224e_211209_224344/8/ccs':
        print('sd')
    start = read.pos +1
    cigar_tup = read.cigartuples
    sequence = read.query_sequence
    flag = read.flag
    # if len(sequence) > 2840:
    #     if len(sequence) <2870:
    #         length_read +=1

    if flag ==16 | 2064:
        backward_read +=1
    else:
        forward_read +=1
    if 'TGAGCG' in sequence:    #MECP2
    # if 'TAAGCG' in sequence:	#gabbr
        taaasis1_read += 1

        orf = sequence[:]

        if cigar_tup[0][0] == 4:
            orf = orf[cigar_tup[0][1]:]

        orf_test = orf[:]
        final_orf = ''
        while True:
            if 'TGAGCG' in orf_test:
                final_orf += orf_test[:orf_test.index('TGAGCG')+3]
                orf_test = orf_test[orf_test.index('TGAGCG')+3:]
            else:
                break


        deletion = 0
        insertion = 0
        del_list = []
        del_list_nt = []
        ins_list=[]
        ins_list_nt=[]
        m=0
        first =True

        for tup in cigar_tup:
            if m < len(final_orf):
                if first:
                    if tup[0]==4:
                        first=False
                        continue
                    else:
                        first=False
                if tup[0] == 1:
                    insertion += tup[1]
                    ins_list.append(m)
                    ins_list_nt.append(tup[1])
                    m += tup[1]
                elif tup[0] == 2:
                    deletion += tup[1]
                    del_list.append(m)
                    del_list_nt.append(tup[1])
                else:
                    m += tup[1]


            else:   break




        del_index=0
        if (1,3) in cigar_tup:
            codon_ins +=1
        if insertion ==0:
            if deletion ==3:
                if (2,3) in cigar_tup:
                    first=True
                    for tup in cigar_tup:
                        if first:
                            if tup[0] ==4:
                                first=False
                                continue
                            else:   first=False
                        if tup[0] !=2:
                            del_index+= tup[1]
                        else:
                            break




        # orf = orf[:orf.index('TGAGCG')+3]
        # barcode_temp = sequence[sequence.index('TGAGCG')+3:]
        barcode = orf[len(final_orf):]

        temp_read = ''
        read_aa=''
        readaa=''
        readaalength=0
        aachange= 0
        j=0

        if (start-1)%3 ==0:
            itera = (start - 1) / 3
            if itera != 0:
                for k in range(0, itera):
                    read_aa += '?' + '\t'

        elif (start-1)%3==1:
            itera = (start - 1) / 3
            for k in range(0, itera+1):
                read_aa += '?' + '\t'
            j=2
        else:
            itera = (start - 1) / 3
            for k in range(0, itera + 1):
                read_aa += '?' + '\t'
            j = 1
        h=0

        for n in range(j, len(final_orf)):
            if del_index !=0:
                if n==del_index:
                    if h%3==0:
                        read_aa += '-' + '\t'
                        readaa += '-'

            if h % 3 != 2:
                temp_read += final_orf[n]
                h+=1
                continue
            else:
                temp_read += final_orf[n]
                for aa, codon in codon_dic.items():
                    if temp_read.lower() in codon:
                        read_aa += aa + '\t'
                        readaa += aa
                        break
                    else:
                        continue
                temp_read =''
                h=0
        #output.write('readid' + '\t' + 'ins' + '\t' + 'del' + '\t' + 'fs' + '\t' + 'barcode' + '\t' + ref_aa + '\n')
        fs =''
        orf_ins =0
        orf_del =0
        if '*' in readaa:
            if len(ins_list) ==0:
                ort_ins =0
            else:
                for ins in ins_list:
                    if ins < 3*len(readaa[:readaa.index('*')])+3:
                        orf_ins +=ins_list_nt[ins_list.index(ins)]
                    else:   continue

            if len(del_list) ==0:
                orf_del =0
            else:
                for dele in del_list:
                    if dele < 3*len(readaa[:readaa.index('*')])+3:
                        orf_del +=del_list_nt[del_list.index(dele)]
                    else:   continue
        else:
            orf_ins = insertion
            orf_del = deletion
        if (orf_ins - orf_del)%3 ==0:
            fs = 'in-frame'
        else:
            fs = 'frame-shift'
        # if in_frame_val =='':
        #     if len(ref_aa) ==len(read_aa):
        #         in_frame_val= 'substitution'
        comment =''
        variant =''


        if '*' in readaa:
            readaalength = len(readaa[:readaa.index('*')])
            # if readaalength == 941: #gabbr2
            if readaalength == 486: #mecp2
            # if readaalength == 393: #tp53
            # if readaalength == 374:  # spop
                comment = 'full_length'
                # for i in range(0, 941):    #gabbr2
                for i in range(0, 486):    #mecp2
                # for i in range(0, 393): #tp53
                # for i in range(0, 374):  # spop
                    if refaa[i] != readaa[i]:
                        aachange += 1
                        variant += refaa[i] + str(i+1) + readaa[i]+':'
                        continue
                    else:
                        continue
            else:
                # if readaalength < 941:    #gabbr2
                if readaalength < 486:    #mecp2
                # if readaalength < 393:  #tp53
                # if readaalength < 374:  # spop
                    aachange +=1
                    for i in range(0, readaalength):
                        if refaa[i] != readaa[i]:
                            aachange += 1
                            variant += refaa[i] + str(i + 1) + readaa[i] + ':'
                            continue
                        else:
                            continue


                    comment='stop-gain'
                    #aachange =1
                    variant +=refaa[readaalength-1] + str(readaalength) + 'X' +':'
                else:
                    comment='additional_aa'
                    # for i in range(0, 941): # gabbr2
                    for i in range(0, 486): # mecp2
                    # for i in range(0, 393): # tp53
                    # for i in range(0, 374):  # spop
                        if refaa[i] != readaa[i]:
                            aachange += 1
                            variant += refaa[i] + str(i + 1) + readaa[i] + ':'
                            continue
                        else:
                            continue
                    # for l in range(941, readaalength):  #gabbr2
                    for l in range(486, readaalength):  #mecp2
                    # for l in range(393, readaalength):  #tp53
                    # for l in range(374, readaalength):  # spop
                        aachange+=1
                        variant += 'Ins' + str(l+1) + readaa[l] +':'
                        continue

        else:
            readaalength = len(readaa)
            comment='stop-lost'



        output.write(readid + '\t' + str(len(final_orf)) +'\t' + str(insertion) +'\t' + str(deletion) +'\t' + fs + '\t'+ str(aachange) +'\t' +str(readaalength)+ '\t'+ comment+'\t' + barcode + '\t' + variant[:-1]+'\n')
        #output2.write(readid + '\t' + str(len(final_orf)) +'\t' + str(insertion) +'\t' + str(deletion) +'\t' + fs + '\t'+ str(aachange) +'\t' +str(readaalength)+ '\t'+ comment+'\t' + barcode+'\n')

    else:
        continue
        #output2.write(readid + '\n')



print('total_read: '+ str(total_read))
#print('length_read: '+ str(length_read))
print('backward_read: '+ str(backward_read))
print('forward_read: '+ str(forward_read))
print('taaasis1_read: '+ str(taaasis1_read))
print('noGCGGCC: '+ str(noGCGGCC) )
print('codon_ins: '+ str(codon_ins))


#total_read: 64152
#backward_read: 2
#forward_read: 64150
#taaasis1_read: 58141
#noGCGGCC: 0
#codon_ins: 4533

#total_read: 64152
#backward_read: 2
#forward_read: 64150
#taaasis1_read: 58277
#noGCGGCC: 0
#codon_ins: 4550