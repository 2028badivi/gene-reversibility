#import dependencies

import pandas as pd

#scikit learn kmeans and scalar for reliable clustering
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler



# an example (template) dataset based on the type of data that Marrvel provides
marrvel_example_pairs = {
    "Gene_Disease_Pair": [
        "SHANK3 : Phelan-McDermid",
        "SHANK3 : Schizophrenia 15",
        "MECP2 : Rett Syndrome",
        "GENE_A : Recessive Microcephaly",
        "GENE_B : Mild Neurodevelopmental",
    ],
    "Inheritance_AD": [1, 1, 1, 1, 1],  # binary (1 means Autosomal Dominant and   0 means something else)
    "gnomAD_pLI": [1.00, 1.00, 1.00, 1.00, 1.0],
    "gnomAD_LoF_oe": [0.25, 0.25, 0.25, 0.25, 0.25],
    "ClinVar_Pathogenic_Count": [4, 4, 4, 4, 4],
    "DIOPT_Mouse_Score": [8, 8, 8, 8, 8],  

}

#make this sample data into a pandas dataframe
df = pd.DataFrame(marrvel_example_pairs)


features_in_sample_data = [

    "Inheritance_AD",

    "gnomAD_pLI",

    "gnomAD_LoF_oe",

    "ClinVar_Pathogenic_Count",

    "DIOPT_Mouse_Score",

]


# for kmeans its important to scale teh values so that the higher numbers wouldn't overpower the signficance of the smaller values.
scaler = StandardScaler()

X_scaled = scaler.fit_transform(df[features])




print("K-Means clustering results are below...")



kmeans = KMeans(n_clusters=2, random_state=42, n_init=10)  #the random seed hyperparam is basically standard; the number of clusters was just a manual choice, we can test the Elbow method and calculate WCSS to find the sweet spot for k value



df["KMeans_Cluster"]=kmeans.fit_predict(X_scaled)




print(df[["Gene_Disease_Pair", "KMeans_Cluster"]])
