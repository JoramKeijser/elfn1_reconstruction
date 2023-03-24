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
Use the aligned sequences to infer the ancestral proteins. This is a computationally heavy step because it relies on bootstrapping. I ran the following SLURM batch script on a computing cluster: 
```
sbatch scripts/alignment_to_ancestors.sh 
```
You can also run this step locally since it cannot be parallelized across multiple machines anyway:
```
topiary-alignment-to-ancestors seed_to_ali/05_clean-aligned-dataframe.csv --out_dir ali_to_anc 
```
The run time will depend on the number of cores and the (automatically determined) number of bootstrap replicates. Doing 600 replicates on 8 cores takes ca. 14 hours. The results will be in the `ali_to_anc/results` folder. 

## Determine branch support
The previous step estimated our confidence in the ancestral sequences. Finally, we determine our confidence in the evolutionary tree on which the reconstructed sequences are placed. This is again done using the bootstrap. The following SLURM script parallelizes the computation:
```
sbatch scripts/bootstrap_reconcile.sh 
```
The run time will depend on the parallelization scheme and the number of bootstrap replicates. Doing 600 replicates on 35 nodes took ca. 8 hours. The result will be added to `ali_to_anc/results`. 



