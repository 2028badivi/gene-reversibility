#imports dependencies


import pandas as pd

#sci kit learn's random forest algorithm
from sklearn.ensemble import RandomForestClassifier



# this dataset is the same sample data set as K-means, but I'm adding the reversibility label that we would get for the literature review process 
marrvel_sample_pairs= {
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
    "Is_Reversible": [
        1,
        0,
        1,
        0,
        0,
    ], 
}

df = pd.DataFrame(marrvel_sample_pairs)


marrvel_features = [
    "Inheritance_AD",
    "gnomAD_pLI",
    "gnomAD_LoF_oe",
    "ClinVar_Pathogenic_Count",
    "DIOPT_Mouse_Score",
]


X = df[features]
y = df["Is_Reversible"]



print("Random Forest")


rf = RandomForestClassifier(random_state=42, n_estimators=50) #Again, these are both just manually selected hyperparameters, but I can do a versatility test on them later. 


rf.fit(X, y)



for feature, importance in zip(features, rf.feature_importances_):
    print(f"Marrvel metric: {feature:25} and importance (signficance) score : {importance:.4f}")
