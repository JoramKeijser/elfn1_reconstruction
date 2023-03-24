# Put the seed sequences into a data frame
import pandas as pd
import numpy as np


def main():
    datadir = "./data/seed_sequences/"
    savedir = "./data/"
    fasta_names = {'Mus musculus': 'Q8C8T7', 
               'Homo sapiens': 'P0C7U0', 
               'Taeniopygia guttata': 'A0A674HDW1',
               'Pelodiscus sinensis': 'K7FQE3'
              }
    df = pd.DataFrame(dtype='str', index=None)
    for i, (species, entry) in enumerate(fasta_names.items()):
        metadata = np.loadtxt(datadir + f"{entry}.fasta", dtype='str', max_rows=1)
        sequence = np.loadtxt(datadir + f"{entry}.fasta", skiprows=1, dtype="str", delimiter=',')
        if i == 0:
            df['species'] = [species]
            df['sequence'] = "".join(list(sequence))
        else:
            df2 = pd.DataFrame(dtype='str')
            df2['species'] = [species]
            df2['sequence'] = "".join(list(sequence))
            df = pd.concat((df, df2))
    # Add aliases
    df['name'] = ['Elfn1'] * len(df)
    df['aliases'] = 'PPP1R28'
    df = df[['name', 'species','sequence','aliases']]
    print(df)
    df.to_csv(savedir + "seed-dataframe.csv", index=False)
    return 0


if __name__=="__main__":
    main()
