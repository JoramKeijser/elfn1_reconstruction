# Install missing libraries
required_packages <- c("ggplot2", "msa", "ggmsa")
missing_packages <- required_packages[!(list.of.packages %in% installed.packages()[,"Package"])]
if(length(missing_packages) > 0) {
  install.packages(missing_packages)
}
# Load them
library(msa) # Alignment
library(ggmsa) # Alignment viewer
library(ggplot2) 

# Change to directory with results
filedir <- "/home/joram/Dropbox/elfn1_reconstruction/results/"
# Fasta with aligned amniote ancestor (anc54) and extant species
alignment_file <- paste0(filedir, "ancestors54_and_extant.fasta")
# Load the alignment 
alignments <- readAAStringSet(alignment_file, format="fasta")

# For each protein "domain", save start & end bases, and name
# "IVD" etc are unique identifiers of start and end
lrrs <- c("IVD","YSN", "LRR") 
lrrs12 <- c("IVD","QFN", "LRR12") 
lrrs_CT <- c("PFY", "CTEG", "LRR-CT")
FN3 <- c("QTE", "HNH", "FN3")
TM <- c("IMT", "YCL", "TM")
# Loop over domains
for (domain in list(lrrs, lrrs12, lrrs_CT, FN3, TM)){
  # Find start and end site
  start <- unlist(gregexpr(domain[1], alignments[1]))
  end <- unlist(gregexpr(domain[2], alignments[1]))
  end <- end + nchar(domain[2]) - 1 # include end identifier
  p <- ggmsa(alignment_file, start, end, char_width = .5, 
        seq_name = TRUE, consensus_views = T,  use_dot = TRUE, 
        ref="Mus musculus", border = "white") + ggtitle(domain[3]) 
  print(p)
}
