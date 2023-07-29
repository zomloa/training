# Importation package Pandas
import pandas as pd
# Création des dataframe avec pandas
### Création à partir d'un dictionnaire
# Création du dictionnaire
etudiant = {'Nom':["Mendong", "Zibi", "Ekounou", "Bastos"]
           ,
           "Prenom":["Chloe", "Loic", "Helene", "Nathan"],
           "Notes":[19,18,15,13]}
etudiant

# Transformer le dictionnaire en dataframe
df_etudiant = pd.DataFrame(etudiant)
df_etudiant

### Création à partir d'un fichier csv
# Importation à partir d'un fichier csv
df=pd.read_csv("credit_risk_dataset.csv",sep=";")
df
# Importation à partir d'un fichier excel
df=pd.read_excel("credit_dataset_excel.xlsx")
df
## Afficher un dataframe et afficher le type de données et description des colonnes
# Afficher les 5 premiers éléments
df.head()
# Afficher les 5 derniers éléments
df.tail()
# avoir la liste des colonnes du dataframe
df.columns
# Avoir le type de données de ma bd
df.dtypes
# Voir la dimension du tableau
df.shape
# Lecture des tableaux avec pandas
### Sélectionner des colonnes
#Si la variable n'a pas d'espace
df.Id_personne.head(5)
#Si la variable a des caractères spéciaux
df['Type de domicile'].tail(5)
#Selectionner plusieurs colonnes
new_df=df[['Type de domicile','Nom', 'Revenu']]
new_df.head(4)
# Connaitre les valeurs uniques d'une variable
df['Type de domicile'].unique()
### Sélectionner des lignes
#Sélectionner des lignes qui respectent une condition uniquement  (Personnes donc le travail est CDI)
new_cdi=df[df['Travail']=="CDI"]
new_cdi.head(5)
#Sélectionner des lignes qui respectent plusieurs condiditions  (Personnes donc le travail est CDI & grade=C)
new_pret=df[(df['Travail']=="CDI") & (df['Grade du pret']=="D")]
new_pret.head(5)
### Indexation avec iloc (Index location)
# Séléction de la premère ligne
df.iloc[0]
# Sélectionner la dernière colonne
df.iloc[-1]
# Séléctonner les deux premières lignes et les deux premieres colonnes
df.iloc[0:2,0:2]
### Indexation avec loc (Accéder aux éléments à partir des labels)
# Création d'un index dans le dataframe df_etudiant
#df = df.set_index("Nom")
df
df.loc["Akono"]
## Statistiques descriptives
### Obtenir des statistiques de base (Moyenne, médiane, écart-type)
# Descriptions des variables quantitatives
df.describe()
# Descriptions des variables qualitative
df.describe(include="object")
#Compter les valeurs manquantes par variable
df.isnull().mean()
### Modifier les données
# Supprimer une colonne
df = df.drop("Revenu", axis=1)
df
### Création d'un nouvelle colonne calculer à partir d'autres
#Création d'une nouvelle variable comme étant la multiplication de deux colonnes du tableau
df["test"] = df["Montant du prêt"] * df["Taux_interet"]
df
### Mettre à jour une colonne
# Mettre à jour avec une valeur pour toutes les lignes
df["test"] = 100
df
### Mettre à jour une valeur
#Mise à jour de la dernière colonne de la première ligne
df.iloc[0,-1]=100000
df
### Mettre à jour les valeurs qui respectent une condition
#Modifier la valeur de la colonne d'une ligne en fonction d'une condition (remplacer D par F loan_grade)
df.loc[df["Travail"]=="CDI", "Travail"] ="CDD"
df
# Fusion et jointure de Data Frames
# Création des DataFrames exemple
data1 = {
    "ID": [1, 2, 3, 4],
    "Prénom": ["Alice", "Bob", "Charlie", "David"]
}

data2 = {
    "ID": [3, 4, 5, 6],
    "Ville": ["Paris", "Lyon", "Marseille", "Toulouse"]
}

df1=pd.DataFrame(data1)
df2=pd.DataFrame(data2)

# Effectuer une jointure interne (inner join)
inner_join = df1.merge(df2, on="ID", how="inner")

# Effectuer une jointure externe (outer join)
outer_join = df1.merge(df2, on="ID", how="outer")

# Effectuer une jointure gauche (left join)
left_join = df1.merge(df2, on="ID", how="left")

# Effectuer une jointure droite (right join)
right_join = df1.merge(df2, on="ID", how="right")

# Afficher les résultats
print("Inner join:")
print(inner_join)
print("\nOuter join:")
print(outer_join)
print("\nLeft join:")
print(left_join)
print("\nRight join:")
print(right_join)
# Enregistrer la base
### Enregistrer en csv
# enregistrer en csv
df.to_csv("test.csv")
### Enregistrer en JSON
# Exporter en fichier json
df.to_json("test.json")
