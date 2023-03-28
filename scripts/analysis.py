# Analyse ASR results
import topiary
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from src.plotting_utils import plot_ancestor_data, plot_conservation_data
from src.plotting_utils import GRAY, RED

# Determine amount of conservation
# Load extant sequences
df = pd.read_csv("./results/extant_dataframe.csv")
df = df[df['keep']] # throw out a few sequences according to Topiary's heuristics
mus = df.iloc[0]['alignment'] # mouse is reference 
ali_len = len(mus)
n_alis = df.shape[0]
# First dim corresponds to extant species
# Second dim corresponds to sites
equality = np.zeros((n_alis, ali_len))
for i in range(n_alis):
    for site in range(ali_len):
        equality[i, site] = df.iloc[0]['alignment'][site] == df.iloc[i]['alignment'][site]

# Load stats from reconstructed sequence
df_anc = pd.read_csv("./results/anc54.csv")
# Add fraction across extant species equal to each site
df_anc['equal'] = equality.mean(0) 

# Plot conservation
fig, ax = plot_conservation_data(df_anc)
plt.subplots_adjust(bottom=0.15)
ax[0].set_xlabel("Alignment site")
ax[0].set_ylabel("Conservation", fontsize=15)

# Annotate protein "domains". Find start and end 
mus_aligned = "MAGHGWGT---AWVLVAAATLLHAGGLAQGDCWLIEGDKGFVWLAICSQNQPPYEAIPQQINNTIVDLRLNENRIRSVQY" + \
"ASLSRFGNLTYLNLTKNEIGYIEDGAFSGQFNLQVLQLGYNRLRNLTEGMLRGLSKLEYLYLQANLIEVVMASAFWECPN" + \
"IVNIDLSMNRIQQLGSGTFAGLTKLSVCEIYSNPFYCSCELLGFLRWLAAFTNATQTHDRVQCESPPVYAGYFLLGQGRH" + \
"GHQRSILSKLQSVCTEGSYTAEVLGPPRPVPGRSQPGHSPPP-PPPEPSDMPCADDECFSGDGTTPLVILTTLVPQTEAR" + \
"PSMKVKQLTQNSATIMVQLPSPFNRMYTLEQYNNSKSFTVSKLTQPQEEIRLTNLYTLTNYTYCVVSTSSGTHHNHTCLT" + \
"ICLPKPPSPPGPVPSPSTATHYIMTILGCLFGMVLVLGAVYYCLRKRRRQEEKHKKAV-AAAAGSLKKTIIELKYGPEIE" + \
"APGLAPLTQGPLLGPEAVTRIPYLPAATSDVEQYKLVESSETPKATKGNYIEVRTGEPQERRGCELSRP-GEPQSSVAEI" + \
"STIAKEVDRVNQIINNCIDALKSESTSFQGAKSGAVSAAEPQLVLLSEPLASKHSFLSPVYKDAFGHGGLQRHHSVEAAP" + \
"GPPRASTSSSGSARSPRTFRAEATGTHKAPATETKYIEKSSPVPETILTVTPAATVLRAEADKSRQYGEHRHSYPGSHPA" + \
"EPPAPP--PPPPTHEGLGGRKASILEPLTRPRPRDLVYSQLSPQYHNLSYSSSPEYTCRASPSIWERLRLSRRRHKDDAE" + \
"FMAAGHALRKKVQFAKDEDLHDILDYWKGVSAQHKS"

# Find start and end sites of protein domains
domains = {}
domains['LRRs'] = [mus_aligned.find("IVD"), mus_aligned.find("YSN")]
domains['LRR-CT'] = [mus_aligned.find("PFY"), mus_aligned.find("EGS")]
domains['FN3'] = [mus_aligned.find("TEARP"), mus_aligned.find("HHNH")]
domains['TM'] = [mus_aligned.find("IMTIL"), mus_aligned.find("YYCL")]

# Add with domain names on top
xvals = {"LRRs": 85, "LRR-CT": 170, "FN3": 320, "TM": 405}
for name, bookends in domains.items():
    print(name, bookends)
    ax[0].hlines(1.1, bookends[0], bookends[1], lw=3, color='black', alpha=0.75)
    ax[0].text(xvals[name], 1.15, name, alpha=0.75)
plt.savefig("./figures/conservation.png", dpi=400)

# Visualize reconstruction quality
fig, ax = plot_ancestor_data(df_anc)
plt.subplots_adjust(bottom=0.15)
ax[0].text(1020, .8, "Most likely (ML)", color = GRAY)
ax[0].text(1020, .1, "2nd most likely", color=RED)
ax[0].set_xlabel("Alignment site")
ax[0].set_ylabel("Posterior probability", fontsize=15)
for name, bookends in domains.items():
    ax[0].hlines(1.1, bookends[0], bookends[1], lw=6, color='black', alpha=0.75)
    ax[0].text(xvals[name], 1.15, name, alpha=0.75)
plt.savefig("./figures/anc54_quality.png", dpi=400)


