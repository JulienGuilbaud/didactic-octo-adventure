#import des fonctions
import FeedBase
from datetime import date  # Importe le module date pour obtenir la date actuelle

def JGTEST():
    """
    Fonction principale pour convertir les données produits en un flux pour Google Merchant Center.
    """
    print("DÉBUT conversion des données en flux de produit Google Merchant Center")

    fichier_csv_entree = "INPUTSOURCE/Product Template (product.template).csv"  # Chemin du fichier CSV d'entrée
    aujourdhui = date.today().strftime("%d-%m-%Y")  # Obtient la date d'aujourd'hui au format JJ-MM-AAAA
    domaine = "https://www.micpartsonline.com"  # Domaine du site web
    pays = "FR" # Code pays pour le flux (France)

    langue = "fr"
   
    remise = 1.25  # Remise pour les prix
    fichier_csv_sortie = f"FLUX_{pays}{langue}_{aujourdhui}.csv"  # Nom du fichier CSV de sortie, incluant la date
    FeedBase.creer_flux_merchant_center(fichier_csv_entree, fichier_csv_sortie, domaine, pays, langue, remise)  # Appelle la fonction pour créer le flux

    print(f"FIN conversion des données en flux de produit Google Merchant Center '{fichier_csv_sortie}'")

def CAfr():
    """
    Fonction principale pour convertir les données produits en un flux pour Google Merchant Center.
    """
    print("DÉBUT conversion des données en flux de produit Google Merchant Center")

    fichier_csv_entree = "INPUTSOURCE/Product Template (product.template).csv"  # Chemin du fichier CSV d'entrée
    aujourdhui = date.today().strftime("%d-%m-%Y")  # Obtient la date d'aujourd'hui au format JJ-MM-AAAA
    domaine = "https://www.micpartsonline.com"  # Domaine du site web
    pays = "CA" # Code pays pour le flux (France)

    langue = "fr"
   
    remise = 1.33  # Remise pour les prix
    fichier_csv_sortie = f"FLUX_{pays}{langue}_{aujourdhui}.csv"  # Nom du fichier CSV de sortie, incluant la date
    FeedBase.creer_flux_merchant_center(fichier_csv_entree, fichier_csv_sortie, domaine, pays, langue, remise)  # Appelle la fonction pour créer le flux

    print(f"FIN conversion des données en flux de produit Google Merchant Center '{fichier_csv_sortie}'")