# This script downloads and installs necessary software and annotations. At some
# points the script may stop and ask for user input, and you may have to stop
# the script and restart at some points (this weirdness is due to the fun of
# trying to compile and install software automatically).

import os

import cdpybio as cpb
import pipelines as ps

import cardipspy as cpy

if not os.path.exists(cpy.epacts):
    ps.prepare.download_epacts(cpy.software)

if not os.path.exists(cpy.snpeff):
    ps.prepare.download_snpeff(cpy.software)

if not os.path.exists(cpy.igvtools):
    ps.prepare.download_igvtools(cpy.software)

if not os.path.exists(cpy.gtfToGenePred):
    ps.prepare.download_gtfToGenePred(cpy.software)

if not os.path.exists(cpy.bedGraphToBigWig):
    ps.prepare.download_bedGraphToBigWig(cpy.software)

if not os.path.exists(cpy.liftOver):
    ps.prepare.download_liftOver(cpy.software)

if not os.path.exists(cpy.bedtools):
    ps.prepare.download_bedtools(cpy.software)

if not os.path.exists(cpy.bcftools):
    ps.prepare.download_bcftools(cpy.software)

if not os.path.exists(cpy.samtools):
    ps.prepare.download_samtools(cpy.software, lncurses=True)

if not os.path.exists(cpy.htslib):
    ps.prepare.download_htslib(cpy.software)

if not os.path.exists(cpy.picard):
    ps.prepare.download_picard(cpy.software)

if not os.path.exists(cpy.R):
    ps.prepare.download_r(cpy.software)

if not os.path.exists(cpy.star):
    ps.prepare.download_star(cpy.software)

if not os.path.exists(cpy.fastqc):
    ps.prepare.download_fastqc(cpy.software)

if not os.path.exists(cpy.featureCounts):
    ps.prepare.download_subread(cpy.software)

if not os.path.exists(cpy.fastx):
    ps.prepare.download_fastx_toolkit(cpy.software)

if not os.path.exists(cpy.vcftools):
    ps.prepare.download_vcftools(cpy.software)

if not os.path.exists(cpy.hg19):
    ps.prepare.download_hg19(cpy.public_data, cpy.samtools)

if not os.path.exists(cpy.gencode_gtf):
    ps.prepare.download_gencode_gtf(cpy.public_data)

if not os.path.exists(cpy.gencode_splice_jxn_info):
    df = cpb.gencode.make_splice_junction_df(cpy.gencode_gtf)
    df.to_csv(cpy.gencode_splice_jxn_info, sep='\t')

if not os.path.exists(cpy.gencode_gene_info):
    df = cpb.gencode.make_gene_info_df(cpy.gencode_gtf)
    df.to_csv(cpy.gencode_gene_info, sep='\t')

if not os.path.exists(cpy.gencode_gene_bed):
    bt = cpb.gencode.make_feature_bed(cpy.gencode_gtf, 'gene',
                                      out=cpy.gencode_gene_bed)

if not os.path.exists(cpy.gencode_transcript_bed):
    bt = cpb.gencode.make_feature_bed(cpy.gencode_gtf, 'transcript',
                                      out=cpy.gencode_transcript_bed)

if not os.path.exists(cpy.gencode_exon_bed):
    bt = cpb.gencode.make_feature_bed(cpy.gencode_gtf, 'exon',
                                      out=cpy.gencode_exon_bed)

if not os.path.exists(cpy.gencode_utr_bed):
    bt = cpb.gencode.make_feature_bed(cpy.gencode_gtf, 'utr',
                                      out=cpy.gencode_utr_bed)

if not os.path.exists(cpy.gencode_transcript_gene):
    tg = cpb.gencode.make_transcript_gene_se(cpy.gencode_gtf)
    tg.to_csv(cpy.gencode_transcript_gene, sep='\t')

if not os.path.exists(cpy.gencode_promoter_bed):
    bt = cpb.gencode.make_promoter_bed(cpy.gencode_gtf,
                                       out=cpy.gencode_promoter_bed)

if not os.path.exists(cpy.gencode_tss_bed):
    bt = cpb.gencode.make_promoter_bed(cpy.gencode_gtf,
                                       out=cpy.gencode_tss_bed,
                                       tss=True)

if not os.path.exists(cpy.roadmap_15_state):
    ps.prepare.download_roadmap_15_state_chromatin_model(cpy.roadmap_15_state)

if not os.path.exists(cpy.roadmap_25_state):
    ps.prepare.download_roadmap_25_state_chromatin_model(cpy.roadmap_25_state)

if not os.path.exists(cpy.featureCounts):
    ps.prepare.download_subread(cpy.software)

if not os.path.exists(cpy.weblogo):
    ps.prepare.download_weblogo(cpy.software)

if not os.path.exists(cpy.blat):
    ps.prepare.download_blat(cpy.software)

if not os.path.exists(cpy.star_index):
    ps.prepare.make_star_index(cpy.public_data, 30, cpy.hg19, cpy.gencode_gtf,
                               star_path=cpy.star)

if not os.path.exists(cpy.rsem):
    ps.prepare.download_rsem(cpy.software, lncurses=True)

dy = os.path.split(cpy.rsem_reference)[0]
if not os.path.exists(dy):
    cpy.makedir(dy)
    ps.prepare.rsem_prepare_reference(cpy.hg19, cpy.rsem_reference, cpy.rsem,
                                      gtf=cpy.gencode_gtf)

# try:
#     import rpy2
# except ImportError:
#     ps.prepare.download_install_rpy2(cpy.R, os.path.join(cpy.software))
# 
# # I need to update this so the bioconductor dependencies aren't installed
# # every time the script is run.
# try:
#     import rpy2
#     ps.prepare.install_bioconductor_dependencies()
# except ImportError:
#     print('rpy2 not installed\n')
# 
if not os.path.exists(cpy.gencode_dexseq_annotation):
    ps.prepare.make_dexseq_annotation(cpy.gencode_gtf,
                                      cpy.gencode_dexseq_annotation)

if not os.path.exists(cpy.gwas_catalog):
    ps.prepare.download_gwas_catalog(cpy.public_data)

if not os.path.exists(cpy.encode_blacklist):
    ps.prepare.download_encode_blacklist(cpy.public_data)

if not os.path.exists(cpy.picard_ref_flat):
    ps.prepare.make_rna_seq_metrics_files(
        os.path.join(cpy.public_data, 'gencode_v19'), cpy.gencode_gtf, cpy.hg19,
        cpy.picard, cpy.gtfToGenePred)

if not os.path.exists(cpy.kheradpour_motifs):
    dy = os.path.split(cpy.kheradpour_motifs)[0]
    cpy.makedir(dy)
    ps.prepare.download_kheradpour_motifs(dy)
