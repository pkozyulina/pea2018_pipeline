workdir: '.'

RSEMREF = '/home/pkozyulina/reference/PisumSativum'
BWT2REF = '/home/pkozyulina/reference/PisumSativum_bwt'
PATHTOBOWTIE2 = '/home/pkozyulina/TOOLS/bowtie2-2.3.4.1-linux-x86_64/'
PATHTORSEM = '/home/pkozyulina/TOOLS/RSEM-1.3.1'
THREADS = 8
READLENGTH = 86
READSD = 1809

### SCRIPT FOR MACE RNASeq ANALYSIS PREPROCESSING ###


#### SET VARIABLES ####
FASTQ = expand('FASTQ/{sample}.fq', sample=config["samples"])
ISOCOUNTS = expand('{sample}.isoforms.results', sample=config["samples"])
SAM = expand('SAM/{sample}.sam', sample=config["samples"])



INP = lambda wildcards: config["samples"][wildcards.sample]



#### PREPARE SAMPLE LIST ####
rule targets:
    input:
        FASTQ, SAM, ISOCOUNTS


##### CLEAN #####
rule clean:
    shell: "rm [0-9]*.snakemake-job*"


#### MAKE FASTQ FROM BAM ####
rule bamtofq:
	input:
		INP
	output:
		'FASTQ/{sample}.fq'
	shell:
		'bedtools bamtofastq -i {input} -fq {output}'


#### REALIGN WITH BOWTIE2 #####
rule realign:
	input:
		rules.bamtofq.output
	output:
		'SAM/{sample}.sam'
	shell:
		'bowtie2 -x {BWT2REF} -p {THREADS} --local --no-unal -U {input} -S {output}'



#### RUN RSEM AND GET ISOFORM COUNTS ####
rule runrsem:
	input:
		rules.realign.output
	output:
		'{sample}.isoforms.results'
	log:
        'logs/rsem_{sample}.log'
	shell:
		'{PATHTORSEM}/rsem-calculate-expression -p {THREADS} --no-bam-output --bowtie2 --bowtie2-path {PATHTOBOWTIE2} --strandedness none --sam  {input} {RSEMREF} {wildcards.sample} '


