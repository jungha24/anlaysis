
import sys
import math

input_file=sys.argv[1]
batch_size=int(sys.argv[2])

def _parse_dx_delim(delim_line):
    '''parse each list of delim output from dx find into NAME, ID, SIZE, and FOLDER'''
    #size=_parse_size(delim_line[2])
    size=delim_line[2]
    id=delim_line[-1]
    split_path=delim_line[3].split('/')
    folder='/'+'/'.join(split_path[:-1])
    name=split_path[-1]

    return name,id,size,folder

fd=open(input_file)
lines=fd.readlines()
sample_number=len(lines)
batch_mapped_files=''
input_number=0
number_of_batch = int(math.ceil(sample_number*1.0/batch_size))
for batch_number in range(number_of_batch):
    batch_mapped_files=''
    for member in range(batch_size):
        delim_line = lines[input_number].strip().split('\t')
        name, id, size, folder = _parse_dx_delim(delim_line)
        batch_mapped_files += '-ipvcf={} '.format(id)
        final_folder='/pVCF_qc_process/' + str(batch_number)
        input_number+=1
        if input_number == sample_number:
            break

    print('dx run /pvcf_qc_fail_parallel {batch_mapped_files} --folder="{final_folder}" --tag 200K_exome_exome_analysis --tag original --tag batch_n_{batch_number} --priority normal -y --brief '.format(batch_mapped_files=batch_mapped_files,batch_number=batch_number,final_folder=final_folder))
