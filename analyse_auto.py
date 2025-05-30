import os

# D'abord récupérer les données
os.system("python get_data_baserow.py")

# Ensuite lancer l'analyse
os.system("python clusters_pratique.py")
