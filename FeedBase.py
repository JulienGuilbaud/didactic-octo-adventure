import pandas as pd  # Importe la librairie pandas pour la manipulation des données
from bs4 import BeautifulSoup  # Importe BeautifulSoup pour le parsing HTML
from datetime import date  # Importe le module date pour obtenir la date actuelle

def FeedBaseNewFR():
    """
    Fonction principale pour convertir les données produits en un flux pour Google Merchant Center.
    """
    print("DÉBUT conversion des données en flux de produit Google Merchant Center")

    fichier_csv_entree = "INPUTSOURCE/Product Template (product.template).csv"  # Chemin du fichier CSV d'entrée
    aujourdhui = date.today().strftime("%d-%m-%Y")  # Obtient la date d'aujourd'hui au format JJ-MM-AAAA
    domaine = "https://www.micpartsonline.com"  # Domaine du site web
    pays = "FR"  # Code pays pour le flux (France)
    etat = "NEW"  # Condition des articles (neuf)
    remise = 1.25  # Remise pour les prix
    fichier_csv_sortie = f"FLUX_{pays}_{etat}_{aujourdhui}.csv"  # Nom du fichier CSV de sortie, incluant la date
    creer_flux_merchant_center(fichier_csv_entree, fichier_csv_sortie, domaine, pays, etat, remise)  # Appelle la fonction pour créer le flux

    print(f"FIN conversion des données en flux de produit Google Merchant Center '{fichier_csv_sortie}'")

def FeedBaseUsedFR():
    """
    Fonction principale pour convertir les données produits en un flux pour Google Merchant Center.
    """
    print("DÉBUT conversion des données en flux de produit Google Merchant Center")

    fichier_csv_entree = "INPUTSOURCE/Product Template (product.template).csv"  # Chemin du fichier CSV d'entrée
    aujourdhui = date.today().strftime("%d-%m-%Y")  # Obtient la date d'aujourd'hui au format JJ-MM-AAAA
    domaine = "https://www.micpartsonline.com"  # Domaine du site web
    pays = "FR"  # Code pays pour le flux (France)
    etat = "USED"  # Condition des articles (neuf)
    remise = 2  # Remise pour les prix
    fichier_csv_sortie = f"FLUX_{pays}_{etat}_{aujourdhui}.csv"  # Nom du fichier CSV de sortie, incluant la date
    creer_flux_merchant_center(fichier_csv_entree, fichier_csv_sortie, domaine, pays, etat, remise)  # Appelle la fonction pour créer le flux

    print(f"FIN conversion des données en flux de produit Google Merchant Center '{fichier_csv_sortie}'")

def creer_flux_merchant_center(fichier_entree, fichier_sortie, domaine, pays, etat, remise):
    """
    Crée le flux de produits pour Google Merchant Center.

    Args:
        fichier_entree: Chemin du fichier CSV d'entrée.
        fichier_sortie: Chemin du fichier CSV de sortie.
        domaine: Domaine du site web.
        pays: Code pays pour le flux.
        etat: Condition des articles.
    """
    try:
        df = pd.read_csv(fichier_entree, encoding='utf-8')  # Lit le fichier CSV d'entrée dans un DataFrame pandas
                # Filtre les lignes sans ID *avant* toute autre opération
        df = df.dropna(subset=['Product/ID'])  # Supprime les lignes où la colonne 'id' est NaN
        

        # Transformations des données avec pandas
        df['brand'] = df['Brand'].fillna('MICPARTSONLINE').str[:50]  # Remplit les valeurs manquantes de la marque avec "MICPARTSONLINE" et limite à 50 caractères
        df['npm'] = df['Internal Reference'].str[:50]  # limite à 50 caractères
        df['title'] = df['Name'].str[:150] # limite à 150 caractères

        # Traitement de la description
        def clean_description(desc):
            """Nettoie la description HTML, la tronque, et supprime les espaces inutiles."""
            if pd.isna(desc):
                return "Contact us for more details!"
            text = BeautifulSoup(str(desc), 'html.parser').get_text()
            cleaned_text = ' '.join(text.split())  
            return cleaned_text[:5000]

        df['description_propre'] = df['Description for the website'].apply(clean_description)  # Applique la fonction clean_description à la colonne des descriptions
        df['description'] = df['brand'].astype(str) + ' - ' + df['npm'].astype(str) + ' - ' + df['title'].astype(str) + ' - ' + df['description_propre'].astype(str) # Concatène les champs pour une description combinée.
        df['description'] = df['description'].str[:5000]  # Tronque la description combinée à 5000 caractères.


        df['id'] = etat + pays + df['Product/ID'].astype(int).astype(str)  # Crée l'ID en combinant le pays, l'état et l'ID du produit
        df['link'] = domaine + df['Website URL'].astype(str)  # Crée le lien en combinant le domaine et l'URL du produit
        df['image_link'] = 'https://www.micpartsonline.com/web/image/product.product/'+df['Product/ID'].astype(int).astype(str)+'/image_1024'    
        df['additional_image_link'] = df['Product Images/Image URL'] 
        df['availability'] = 'in_stock'  # Définit la disponibilité sur "en stock"
        df['price'] = (df['Google Sales Price'].astype(float) * remise ).map("{:.2f} CAD".format)
        df['sale_price'] = df['Google Sales Price'].astype(float).map("{:.2f} CAD".format)  # Formate le prix avec deux décimales et la devise CAD
        df['condition'] = etat.lower()  # Définit la condition en minuscules



        # Sélectionne et réordonne les colonnes pour le fichier de sortie
        output_columns = ['id', 'brand', 'npm', 'title', 'description', 'link', 'image_link','additional_image_link','price','sale_price','availability', 'condition']  # Liste des colonnes à inclure dans le fichier de sortie
        df[output_columns].to_csv(fichier_sortie, index=False, encoding='utf-8')  # Écrit le DataFrame dans le fichier CSV de sortie

    except FileNotFoundError:  # Gère l'erreur si le fichier d'entrée n'est pas trouvé
        print(f"Error: Input file '{fichier_entree}' not found.")
    except Exception as e:  # Gère les autres erreurs
        print(f"An error occurred: {e}")

