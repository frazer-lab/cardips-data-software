import os
from os.path import join
import subprocess

import pandas as pd

# File locations
# Rather than specifying paths all over, I'll just put the paths to commonly
# used files and directories here and use the package to open them. 
def _get_project_dir():
    return os.path.sep.join(os.path.abspath(__file__).split(os.path.sep)[0:-3])

root = _get_project_dir()

software = '/raid3/software'
public_data = '/raid3/publicdata'

environment = join(root, 'environment.sh')

## public data
subdir = public_data
encode_blacklist = join(subdir, 'encode_blacklist.bed')
hg19 = join(subdir, 'hg19', 'hg19.fa')
star_index = join(subdir, 'star_index')
rsem_reference = join(subdir, 'rsem_reference', 'gencode_v19_ref')
gencode_gtf = join(subdir, 'gencode_v19', 'gencode.v19.annotation.gtf')
gencode_splice_jxn_info = join(subdir, 'gencode_v19', 'splice_jxn_info.tsv')
gencode_gene_info = join(subdir, 'gencode_v19', 'gene_info.tsv')
gencode_transcript_gene = join(subdir, 'gencode_v19', 'gene_transcript.tsv')
gencode_dexseq_annotation = join(subdir, 'gencode_v19',
                                 'gencode.v19.dexseq.gff')
gencode_gene_bed = join(subdir, 'gencode_v19', 'genes.bed')
gencode_transcript_bed = join(subdir, 'gencode_v19', 'transcripts.bed')
gencode_exon_bed = join(subdir, 'gencode_v19', 'exons.bed')
gencode_utr_bed = join(subdir, 'gencode_v19', 'utrs.bed')
gencode_promoter_bed = join(subdir, 'gencode_v19', 'promoters.bed')
picard_ref_flat = join(subdir, 'gencode_v19', 'gencode_no_rRNA.txt.gz')
picard_rrna = join(subdir, 'gencode_v19', 'rrna.interval')
roadmap_25_state = join(subdir, 'roadmap_25_state')
roadmap_25_state_sample_legend = join(roadmap_25_state, 'EIDlegend.txt')
roadmap_25_state_annotation = join(roadmap_25_state,
                                   'annotation_25_imputed12marks.txt')
## software
subdir = software
bcftools= join(subdir, 'bcftools-1.2', 'bin', 'bcftools')
bedGraphToBigWig = join(subdir, 'bedGraphToBigWig')
epacts = join(subdir, 'EPACTS-3.2.6', 'bin', 'epacts')
gtfToGenePred= join(subdir, 'gtfToGenePred')
bedtools = join(subdir, 'bedtools2-2.23.0/bin/bedtools')
blat = join(subdir, 'blat')
fastqc = join(subdir, 'fastqc_v0.11.2', 'fastqc')
fastx = join(subdir, 'fastx_toolkit-0.0.14')
featureCounts = join(subdir, 'subread-1.4.6-Linux-x86_64', 'bin',
                     'featureCounts')
homer = join(subdir, 'homer', 'bin')
igvtools = join(subdir, 'IGVTools')
picard = join(subdir, 'picard-1.131', 'dist', 'picard.jar')
R = join(subdir, 'R-3.1.1', 'bin', 'R')
Rscript = join(subdir, 'R-3.1.1', 'bin', 'Rscript')
rsem = join(subdir, 'rsem-1.2.20')
samtools = join(subdir, 'samtools-1.2', 'bin', 'samtools')
snpeff = join(subdir, 'snpEff_v4_1g_core', 'snpEff.jar')
snpsift = join(subdir, 'snpEff', 'SnpSift.jar')
star = join(subdir, 'STAR-STAR_2.4.0h', 'bin', 'Linux_x86_64_static', 'STAR')
vcftools = join(subdir, 'vcftools_0.1.12b', 'bin', 'vcftools')
weblogo = join(subdir, 'weblogo', 'seqlogo')

## functions

def makedir(p):
    """Make a directory if it doesn't already exist"""
    try:
        os.makedirs(p)
    except OSError:
        pass

def submit_job(fn):
    subprocess.check_call('ssh cdeboever@flc.ucsd.edu \'qsub {}\''.format(fn),
                          shell=True)
