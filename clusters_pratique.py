"""
Analyse spatiale automatisée des répondants à un questionnaire patrimonial.
Ce script utilise un clustering hiérarchique agglomératif et visualise les groupes sur une carte Folium.
"""

import requests
import pandas as pd
from sklearn.cluster import AgglomerativeClustering
import folium

# === 1. RÉCUPÉRATION DES DONNÉES DEPUIS BASEROW
TOKEN = "oF4ZhbO62oPoeUpVVrbjCuf8s3Jaxe3v"  
TABLE_ID = "510775"
API_URL = f"https://api.baserow.io/api/database/rows/table/{TABLE_ID}/?user_field_names=true"

headers = {
    "Authorization": f"Token {TOKEN}"
}

print("Récupération des données depuis Baserow...")
response = requests.get(API_URL, headers=headers)

if response.status_code != 200:
    raise Exception(f"Erreur API : {response.status_code} – {response.text}")

data = response.json()["results"]
df = pd.DataFrame(data)
print(f"Données reçues : {len(df)} lignes")

# === 2. FILTRAGE DES RÉPONDANTS PRATIQUANTS
df = df[df["role"].isin(["pratique", "lesdeux"])]

# === 3. NETTOYAGE DES COORDONNÉES
df = df.dropna(subset=["user_lieu_lat", "user_lieu_lon"])
df["lat"] = df["user_lieu_lat"].astype(float)
df["lon"] = df["user_lieu_lon"].astype(float)

if df.empty:
    raise ValueError("Aucune donnée géographique exploitable après filtrage.")

# === 4. CLUSTERING HIÉRARCHIQUE
coords = df[["lat", "lon"]].values
clustering = AgglomerativeClustering(n_clusters=3).fit(coords)  # Ajuster n_clusters selon les cas des données du PCI
df["cluster"] = clustering.labels_

# === 5. VISUALISATION SUR CARTE INTERACTIVE
m = folium.Map(location=[46.5, 6.7], zoom_start=12)
colors = ["red", "blue", "green", "purple", "orange", "pink", "darkred", "lightblue"]

for _, row in df.iterrows():
    label = f"{row.get('nom', 'Inconnu')} – Cluster {row['cluster']}"
    color = colors[row["cluster"] % len(colors)]
    folium.CircleMarker(
        location=(row["lat"], row["lon"]),
        radius=6,
        popup=label,
        color=color,
        fill=True,
        fill_opacity=0.8
    ).add_to(m)

# === 6. EXPORT FINAL
df.to_csv("donnees_lavaux_auto.csv", index=False)
m.save("carte_clusters_pratique.html")

print("Données sauvegardées : donnees_lavaux_auto.csv")
print("Carte générée : carte_clusters_pratique.html")
