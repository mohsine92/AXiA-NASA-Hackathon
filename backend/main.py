from fastapi import FastAPI
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Autoriser le front à accéder à l'API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Charger les données préparées
df = pd.read_csv("data/prepared_exoplanets.csv")

@app.get("/planets")
def get_planets(max_radius: float = None):
    planets = df.copy()
    if max_radius:
        planets = planets[planets["pl_rade"] <= max_radius]
    # On renvoie juste les colonnes utiles
    return planets[["toi", "pl_rade", "pl_orbper", "pl_trandurh", "pl_trandeplim"]].to_dict(orient="records")