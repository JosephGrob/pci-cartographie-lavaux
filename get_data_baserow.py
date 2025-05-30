import requests
import pandas as pd

# === Paramètres
TOKEN = "oF4ZhbO62oPoeUpVVrbjCuf8s3Jaxe3v"
TABLE_ID = "510775"
API_URL = f"https://api.baserow.io/api/database/rows/table/{TABLE_ID}/?user_field_names=true"

headers = {
    "Authorization": f"Token {TOKEN}"
}

# === Requête API
print("📡 Récupération des données depuis Baserow...")
response = requests.get(API_URL, headers=headers)

if response.status_code != 200:
    raise Exception(f"❌ Erreur API : {response.status_code} – {response.text}")

data = response.json()["results"]

# === Convertir en DataFrame
df = pd.DataFrame(data)
print(f"✅ Données reçues : {len(df)} lignes")

# === Sauvegarde (optionnel)
df.to_csv("donnees_lavaux_auto.csv", index=False)
print("💾 Fichier sauvegardé sous donnees_lavaux_auto.csv")
