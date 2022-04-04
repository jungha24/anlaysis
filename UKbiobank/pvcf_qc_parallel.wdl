version 1.0

task pvcf_qc_fail_parallel{
    input {
        Array[File]+ pvcf
    }
    command <<<
        set -x -e -o pipefail
        mkdir output_220329
        for input in ~{sep=" " pvcf}; do
            file_prefix=$( basename $input ".vcf.gz")
            time bcftools query -f '%CHROM\t%POS\n' ${input} | split -l 1000 - output_220329/${file_prefix}.split.
            ls output_220329/${file_prefix}.split.* | parallel --eta --jobs 20 time bcftools view --threads 4 -T {} -Oz -o {}.vcf.gz ${input}
            ls output_220329/${file_prefix}.split.*.vcf.gz | parallel --eta --jobs 20 time java -jar  -Xmx100g /usr/picard/picard.jar FilterVcf I={} O={}.vcf.gz MIN_AB=0.15 MIN_DP=7
            ls output_220329/*.vcf.gz.vcf.gz | parallel --eta --jobs 20 time "bcftools view -f PASS {} | bcftools query -f '%ID\n' - > {}.tmp.txt"
            cat output_220329/*.tmp.txt > output_220329/${file_prefix}.fail.txt
            rm output_220329/*.vcf.gz
            rm output_220329/*.tmp.txt
        done
    >>>
    output {
        Array[File] variant = glob("output_220329/*.fail.txt")
    }
    runtime {
        docker: "dx://Rett_20220315:/Docker/pvcf_qc_fail/pvcf_qc_fail_0.3.tar.gz"
        dx_timeout: "48H"
        dx_instance_type: "mem3_ssd1_v2_x96"
    }
    parameter_meta {
    pvcf: {
        description: "chunked pvcf",
        patterns: ["*.vcf.gz"],
        stream: true
    }
    }
}
    
