import pandas as pd
from sklearn.cluster import DBSCAN
import folium

# === Étape 1 : Charger les données
df = pd.read_csv("donnees_lavaux_auto.csv") 

# === Étape 2 : Filtrer ceux qui pratiquent ou étudient et pratiquent
df = df[df["role"].isin(["pratique", "lesdeux"])]

# === Étape 3 : Nettoyer et convertir les coordonnées
df = df.dropna(subset=["user_lieu_lat", "user_lieu_lon"])
df["lat"] = df["user_lieu_lat"].astype(float)
df["lon"] = df["user_lieu_lon"].astype(float)

# === Étape 4 : Clustering spatial (DBSCAN)
coords = df[["lat", "lon"]].values
clustering = DBSCAN(eps=0.05, min_samples=1).fit(coords)
df["cluster"] = clustering.labels_

# === Étape 5 : Carte
m = folium.Map(location=[46.5, 6.7], zoom_start=12)

# Couleurs aléatoires pour clusters
colors = ["red", "blue", "green", "purple", "orange", "pink", "darkred", "lightblue"]

for _, row in df.iterrows():
    label = f"{row['nom']} – Cluster {row['cluster']}"
    color = "gray" if row["cluster"] == -1 else colors[row["cluster"] % len(colors)]
    folium.CircleMarker(
        location=(row["lat"], row["lon"]),
        radius=6,
        popup=label,
        color=color,
        fill=True,
        fill_opacity=0.8
    ).add_to(m)

# === Étape 6 : Sauvegarde
m.save("carte_clusters_pratique.html")
print("✅ Carte créée : carte_clusters_pratique.html")
