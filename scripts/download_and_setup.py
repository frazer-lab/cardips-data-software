# This script downloads and installs necessary software and annotations. At some
# points the script may stop and ask for user input, and you may have to stop
# the script and restart at some points (this weirdness is due to the fun of
# trying to compile and install software automatically).

import os

import cdpybio as cpb
import pipelines as ps

import projectpy as ppy

if not os.path.exists(ppy.snpeff):
    ps.prepare.download_snpeff(ppy.software)

if not os.path.exists(ppy.igvtools):
    ps.prepare.download_igvtools(ppy.software)

if not os.path.exists(ppy.gtfToGenePred):
    ps.prepare.download_gtfToGenePred(ppy.software)

if not os.path.exists(ppy.bedGraphToBigWig):
    ps.prepare.download_bedGraphToBigWig(ppy.software)

if not os.path.exists(ppy.bedtools):
    ps.prepare.download_bedtools(ppy.software)

if not os.path.exists(ppy.samtools):
    ps.prepare.download_samtools(ppy.software)

if not os.path.exists(ppy.picard):
    ps.prepare.download_picard(ppy.software)

if not os.path.exists(ppy.R):
    ps.prepare.download_r(ppy.software)

if not os.path.exists(ppy.star):
    ps.prepare.download_star(ppy.software)

if not os.path.exists(ppy.fastqc):
    ps.prepare.download_fastqc(ppy.software)

if not os.path.exists(ppy.featureCounts):
    ps.prepare.download_subread(ppy.software)

if not os.path.exists(ppy.fastx):
    ps.prepare.download_fastx_toolkit(ppy.software)

if not os.path.exists(ppy.vcftools):
    ps.prepare.download_vcftools(ppy.software)

if not os.path.exists(ppy.hg19):
    ps.prepare.download_hg19(ppy.public_data, ppy.samtools)

if not os.path.exists(ppy.gencode_gtf):
    ps.prepare.download_gencode_gtf(ppy.public_data)

if not os.path.exists(ppy.gencode_gene_info):
    df = cpb.gencode.make_gene_info_df(ppy.gencode_gtf)
    df.to_csv(ppy.gencode_gene_info, sep='\t')

if not os.path.exists(ppy.gencode_gene_bed):
    bt = cpb.gencode.make_feature_bed(ppy.gencode_gtf, 'gene',
                                      out=ppy.gencode_gene_bed)

if not os.path.exists(ppy.gencode_transcript_bed):
    bt = cpb.gencode.make_feature_bed(ppy.gencode_gtf, 'transcript',
                                      out=ppy.gencode_transcript_bed)

if not os.path.exists(ppy.gencode_exon_bed):
    bt = cpb.gencode.make_feature_bed(ppy.gencode_gtf, 'exon',
                                      out=ppy.gencode_exon_bed)

if not os.path.exists(ppy.gencode_utr_bed):
    bt = cpb.gencode.make_feature_bed(ppy.gencode_gtf, 'utr',
                                      out=ppy.gencode_utr_bed)

if not os.path.exists(ppy.gencode_transcript_gene):
    tg = cpb.gencode.make_transcript_gene_se(ppy.gencode_gtf)
    tg.to_csv(ppy.gencode_transcript_gene, sep='\t')

if not os.path.exists(ppy.gencode_promoter_bed):
    bt = cpb.gencode.make_promoter_bed(ppy.gencode_gtf,
                                       out=ppy.gencode_promoter_bed)

if not os.path.exists(ppy.roadmap_25_state):
    ps.prepare.download_roadmap_25_state_chromatin_model(ppy.roadmap_25_state)

if not os.path.exists(ppy.featureCounts):
    ps.prepare.download_subread(ppy.software)

if not os.path.exists(ppy.weblogo):
    ps.prepare.download_weblogo(ppy.software)

if not os.path.exists(ppy.blat):
    ps.prepare.download_blat(ppy.software)

if not os.path.exists(ppy.star_index):
    ps.prepare.make_star_index(ppy.public_data, 30, ppy.hg19, ppy.gencode_gtf,
                               star_path=ppy.star)

if not os.path.exists(ppy.rsem):
    ps.prepare.download_rsem(ppy.software, lncurses=True)

dy = os.path.split(ppy.rsem_reference)[0]
if not os.path.exists(dy):
    ppy.makedir(dy)
    ps.prepare.rsem_prepare_reference(ppy.hg19, ppy.rsem_reference, ppy.rsem,
                                      gtf=ppy.gencode_gtf)

try:
    import rpy2
except ImportError:
    ps.prepare.download_install_rpy2(ppy.R, os.path.join(ppy.software))

# I need to update this so the bioconductor dependencies aren't installed
# every time the script is run.
# try:
#     import rpy2
#     ps.prepare.install_bioconductor_dependencies()
# except ImportError:
#     print('rpy2 not installed\n')

if not os.path.exists(ppy.gencode_dexseq_annotation):
    ps.prepare.make_dexseq_annotation(ppy.gencode_gtf,
                                      ppy.gencode_dexseq_annotation)

if not os.path.exists(ppy.encode_blacklist):
    ps.prepare.download_encode_blacklist(ppy.public_data)

if not os.path.exists(ppy.picard_ref_flat):
    ps.prepare.make_rna_seq_metrics_files(
        os.path.join(ppy.public_data, 'gencode_v19'), ppy.gencode_gtf, ppy.hg19,
        ppy.picard, ppy.gtfToGenePred)
