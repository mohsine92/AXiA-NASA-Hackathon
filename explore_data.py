# explore_data.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Lire le fichier préparé
df = pd.read_csv("data/prepared_exoplanets.csv")

# Afficher les premières lignes
print("Aperçu des données :")
print(df.head())

# Statistiques descriptives
print("\nStatistiques descriptives :")
print(df.describe())

# Diagrammes : histogrammes pour pl_rade, pl_orbper, pl_trandurh
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
sns.histplot(df['pl_rade'], bins=30, kde=True)
plt.title('Distribution de pl_rade (rayon planètes)')

plt.subplot(1, 3, 2)
sns.histplot(df['pl_orbper'], bins=30, kde=True)
plt.title('Distribution de pl_orbper (période orbitale)')

plt.subplot(1, 3, 3)
sns.histplot(df['pl_trandurh'], bins=30, kde=True)
plt.title('Distribution de pl_trandurh (durée transit)')

plt.tight_layout()
plt.show()

# Diagramme comparatif TESS vs Kepler si colonne 'source' existe
if 'source' in df.columns:
    plt.figure(figsize=(10,5))
    sns.boxplot(x='source', y='pl_rade', data=df)
    plt.title('Comparaison des rayons planétaires : TESS vs Kepler')
    plt.show()