from rdflib import Graph, Namespace, URIRef, Literal
from rdflib.namespace import RDF, RDFS, SKOS, FOAF, DCTERMS, XSD

# === Initialisation du graphe RDF
g = Graph()

# === Namespaces
CIDOC = Namespace("http://www.cidoc-crm.org/cidoc-crm/")
GEO = Namespace("http://www.geonames.org/ontology#")
EX = Namespace("http://example.org/PCI/")
g.bind("cidoc", CIDOC)
g.bind("geo", GEO)
g.bind("skos", SKOS)
g.bind("foaf", FOAF)
g.bind("ex", EX)

# === Données fictives de l'entrée Baserow
nom = "Jean Dupont"
memoire = "J’ai appris à réparer les murs de pierres avec mon grand-père dans les vignes de Lavaux."
lat = 46.5005
lon = 6.7010
activite = "réparation des murs en pierres sèches"

# === URI unique pour ce répondant
respondant_uri = EX["jean-dupont"]

# === Description de la personne
g.add((respondant_uri, RDF.type, FOAF.Person))
g.add((respondant_uri, FOAF.name, Literal(nom)))

# === Pratique patrimoniale (activité)
activite_uri = EX["murs-pierres-seches"]
g.add((activite_uri, RDF.type, CIDOC["E55_Type"]))
g.add((activite_uri, RDFS.label, Literal(activite)))
g.add((respondant_uri, CIDOC["P72_has_language"], Literal("fr")))

# === Lien entre la personne et la pratique
g.add((respondant_uri, CIDOC["P14_carried_out_by"], activite_uri))

# === Mémoire liée à la pratique (SKOS note + lien)
memoire_node = EX["memoire-jean"]
g.add((memoire_node, RDF.type, SKOS.Note))
g.add((memoire_node, SKOS.note, Literal(memoire, lang="fr")))
g.add((activite_uri, SKOS.related, memoire_node))

# === Lien géographique via coordonnées (GeoNames non résolu ici, mais spatialisé)
geo_blank = URIRef(f"https://sws.geonames.org/7285009/")  
g.add((respondant_uri, GEO["location"], geo_blank))

# === Export RDF
g.serialize(destination="pci_exemple_memoire.rdf", format="turtle")
print("RDF sauvegardé : pci_exemple_memoire.rdf")
