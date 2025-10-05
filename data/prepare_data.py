import pandas as pd
import json

def prepare_data():
    # Lire le CSV déjà préparé
    df = pd.read_csv("data/prepared_exoplanets.csv")
    
    # Remplacer les valeurs NaN par 0
    df = df.fillna(0)

    # Ajouter une colonne source si elle n'existe pas
    if "source" not in df.columns:
        df["source"] = "unknown"

    # Garder les colonnes essentielles
    df = df[["toi", "pl_rade", "pl_orbper", "pl_trandurh", "source"]]

    # Convertir en JSON
    planets = df.to_dict(orient="records")
    with open("data/planets.json", "w") as f:
        json.dump(planets, f, indent=4)

    print("planets.json généré avec succès !")

if __name__ == "__main__":
    prepare_data()