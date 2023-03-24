#!/bin/bash

mkdir data
mkdir data/seed_sequences

# Mouse
wget -P ./data/seed_sequences/ https://rest.uniprot.org/uniprotkb/Q8C8T7.fasta
# Human
wget -P ./data/seed_sequences/ https://rest.uniprot.org/uniprotkb/P0C7U0.fasta
# Turtle
wget -P ./data/seed_sequences/ https://rest.uniprot.org/uniprotkb/K7FQE3.fasta
# Zebra finch
wget -P ./data/seed_sequences/ https://rest.uniprot.org/uniprotkb/A0A674HDW1.fasta

