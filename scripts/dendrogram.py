import matplotlib.pyplot as plt

import pandas as pd

#sci kit learn dendrogram
from scipy.cluster.hierarchy import dendrogram, link
from sklearn.preprocessing import StandardScaler




marrvel_sample_pairs = {
    "Gene_Disease_Pair": [
        "SHANK3 : Phelan-McDermid",
        "SHANK3 : Schizophrenia 15",
        "MECP2 : Rett Syndrome",
        "GENE_A : Recessive Microcephaly",
        "GENE_B : Mild Neurodevelopmental",
    ],
    "Inheritance_AD": [1, 1, 1, 0, 0],
    "gnomAD_pLI": [1.00, 1.00, 1.00, 0.05, 0.12],
    "gnomAD_LoF_oe": [0.04, 0.04, 0.01, 0.85, 0.65],
    "ClinVar_Pathogenic_Count": [240, 240, 310, 12, 4],
    "DIOPT_Mouse_Score": [12, 12, 15, 6, 8],
}



df = pd.DataFrame(marrvel_sample_pairs)

features = [
    "Inheritance_AD",
    "gnomAD_pLI",
    "gnomAD_LoF_oe",
    "ClinVar_Pathogenic_Count",
    "DIOPT_Mouse_Score",
]




scaler = StandardScaler()


X_scaled = scaler.fit_transform(df[features])






print("Dendrogram below...")


linked = link(X_scaled, method="ward")



plt.figure(figsize=(7, 4))
dendrogram(linked, labels=df["Gene_Disease_Pair"].values, orientation="top")

plt.title("Gene to Disease Pair Tree (dendogram based on Marrvel data)")
plt.ylabel("Variance Distance")


plt.xticks(rotation=45, ha="right")
plt.tight_layout()

plt.show()
