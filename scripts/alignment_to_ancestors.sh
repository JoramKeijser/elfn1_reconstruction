#!/bin/bash -l
#SBATCH --job-name=ali_to_anc
#SBATCH --output=ali_to_anc.out
#SBATCH --error=ali_to_anc.err
#SBATCH --partition=standard
#SBATCH --time=07-00:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=16
#SBATCH --cpus-per-task=1

#Activate the topiary conda environment
source ~/miniconda3/bin/activate
export PATH=/home/users/k/keijser/miniconda3/envs/topiary/bin/generax:$PATH
conda activate topiary

# Set up proxy
export https_proxy=http://frontend01:3128/
export http_proxy=http://frontend01:3128/ 

<<<<<<< HEAD
topiary-alignment-to-ancestors /results/seed_to_ali/05_clean-aligned-dataframe.csv --out_dir /results/ali_to_anc
=======
topiary-alignment-to-ancestors seed_to_ali/05_clean-aligned-dataframe.csv --out_dir ali_to_anc
>>>>>>> fccd80c18f9df983a1a8596424c81468e0a95dcf
