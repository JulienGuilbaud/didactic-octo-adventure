import csv
from bs4 import BeautifulSoup
from datetime import date

def FeedBase():
    """
    Fonction principale pour convertir les données produits en un flux pour Google Merchant Center.
    """
    print("DÉBUT conversion des données en flux de produit Google Merchant Center")

    fichier_csv_entree = "INPUTSOURCE/Product Template (product.template).csv"  # Fichier CSV d'entrée
    aujourdhui = date.today().strftime("%d-%m-%Y")  # Date du jour au format JJ-MM-AAAA
    domaine = "https://www.micpartsonline.com"  # Domaine du site web
    pays = "FR"  # Code pays
    etat = "NEW" #condition de l'article
    fichier_csv_sortie = f"FLUX_{pays}_{etat}_{aujourdhui}.csv"  # Nom du fichier CSV de sortie
    creer_flux_merchant_center(fichier_csv_entree, fichier_csv_sortie, domaine, pays, etat)

    print(f"FIN conversion des données en flux de produit Google Merchant Center '{fichier_csv_sortie}'")

def creer_flux_merchant_center(fichier_entree, fichier_sortie, domaine, pays, etat):
    """
    Crée un flux de produits pour Google Merchant Center à partir d'un fichier CSV.

    Args:
        fichier_entree: Chemin du fichier CSV d'entrée.
        fichier_sortie: Chemin du fichier CSV de sortie.
        domaine: Domaine du site web.
        pays: Code pays.
        etat: État de l'article (neuf, occasion, etc.). # Ajout de la description pour état

    """

    try:
        with open(fichier_entree, 'r', encoding='utf-8') as fichier_in, \
                open(fichier_sortie, 'w', newline='', encoding='utf-8') as fichier_out:

            lecteur = csv.DictReader(fichier_in)
            noms_champs = ['id', 'brand','npm', 'title', 'description', 'link', 'image_link', 'availability', 'price', 'condition']
            # Configuration de l'écriture du fichier CSV avec les noms de champs spécifiés
            ecrivain = csv.DictWriter(fichier_out, fieldnames=noms_champs)
            ecrivain.writeheader()

            for ligne in lecteur:
                if ligne['ID'].strip():  # Vérifie si l'ID n'est pas vide ou ne contient que des espaces

                    brand =  ligne.get('Brand', '').strip() or 'MICPARTSONLINE', # Gère les marques manquantes, y compris les espaces indésirables.
                    internal_ref = ligne.get('Internal Reference', "")
                    name = ligne.get('Name', "")
                    description = ligne.get('Description for the website', "")                    
                    if description:  # Check if description is not empty
                        soup = BeautifulSoup(description, 'html.parser')
                        description = soup.get_text() # Extracts text content without HTML tags

                    ligne_descriptif = f"{brand}-{internal_ref}-{name}-{description}"
                    
                    ligne_descriptif = ligne_descriptif.replace("--", "-") #handles consecutive missing fields
                    ligne_descriptif = ligne_descriptif.strip("-") # remove leading/trailing hyphens


                    ligne_merchant = {
                        'id': pays + etat.lower() + ligne['ID'], #ID avec code pays et condition de l'article

                        'title': name[:150],  # Titre du produit (limité à 150 caractères)

                        'brand': brand,

                        'npm': internal_ref,

                        'description': ligne_descriptif.strip('"')[:5000],  # Description du produit (limitée à 5000 caractères)

                        'link': domaine + ligne['Website URL'],  # URL du produit

                        'image_link': ligne['Product Images/Image URL'] if ligne['Product Images/Image URL'] else 'https://www.canva.com/design/DAGXtCWMDlU/nKItgvtsjC-dcrxFS_J2Gg/view?utm_content=DAGXtCWMDlU&utm_campaign=designshare&utm_medium=link&utm_source=editor',  # URL de l'image du produit
                        
                        'availability': 'in_stock',  # Disponibilité du produit

                        'price': "{:.2f} CAD".format(float(ligne['Google Sales Price'])),  # Prix du produit (formaté à deux décimales)

                        'condition': etat.lower()  # État du produit
                    }
                    ecrivain.writerow(ligne_merchant)  # écrit la ligne formaté

    except FileNotFoundError:
        print(f"Erreur : Fichier d'entrée '{fichier_entree}' introuvable.")
    except Exception as e:
        print(f"Une erreur est survenue : {e}")




