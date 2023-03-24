#!/bin/bash -l
#SBATCH --job-name=bootstrap_reconcile
#SBATCH --output=reconcile.out
#SBATCH --error=reconcile.err
#SBATCH --time=07-00:00:00
#SBATCH --nodes=35
#SBATCH --ntasks-per-node=20
#SBATCH --partition=standard

#Activate the topiary conda environment
source ~/miniconda3/bin/activate
export PATH=/home/users/k/keijser/miniconda3/envs/topiary/bin/generax:$PATH
conda activate topiary

# Set up proxy
export https_proxy=http://frontend01:3128/
export http_proxy=http://frontend01:3128/ 

<<<<<<< HEAD
topiary-bootstrap-reconcile /results/ali_to_anc 700
=======
topiary-bootstrap-reconcile ali_to_anc 700
>>>>>>> fccd80c18f9df983a1a8596424c81468e0a95dcf
