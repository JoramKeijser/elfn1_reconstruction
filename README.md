# Elfn1 reconstruction
Computationally reconstruct the amino acid sequence of the Elfn1 protein from the last amniote ancestor. See the following preprint for context:
[Cortical interneurons: fit for function and fit to function?](https://doi.org/10.1101/2023.02.23.52967), Keijser & Sprekeler 2023. We use the [Topiary package](https://topiary-asr.readthedocs.io/), a very convenient wrapper around software packages that need to be combined for ancestral sequence reconstruction. 

## Installation

Clone this repository:
```
git clone github.com/JoramKeijser/ancestal_elfn1_reconstruction/
```
Recreate the conda environment to install the required Python and R packages/libraries. 
```
cd ancestal_elfn1_reconstruction/
conda env create --name topiary --file environment.yml
conda activate topiary
```
Install the project:
```
pip install -e .
```

## Download data
Download four seed sequences 
```
bash scripts/download_sequences.sh
```
Use the seed sequences to find Elfn1 homologs, do reciprocal BLAST to call their orthology, lower dataset redundancy, and align the resulting sequences. 
This will take less than an hour on a laptop.
```
python scripts/create_seed_dataset.py
```
The results of this step will be in a folder called `seed_to_ali`. Specifically have a look at the `05_clean-aligned-dataframe.csv` and `06_alignment.fasta` files. The former is the input for the next step, the latter can be viewed in an alignment viewer. 

## Infer ancestral sequences
Use the aligned sequences to infer the ancestral proteins. This is a computationally heavy step that I ran on a computing cluster with the following SLURM script. 
```
sbatch scripts/alignment_to_ancestors.sh 
```
The result will be in a folder called `ali_to_anc/results`. 

## Determine branch support
The previous step used bootstrapping to get confidence estimates for the ancestral sequences. In a final step, we determine the confidence in the evolutionary tree on which these sequences are placed. The following SLURM script parallelizes the computation, such that it takes hours instead of days. 
```
sbatch scripts/bootstrap_reconcile.sh 
```
The result will be added to `ali_to_anc/results`. 



