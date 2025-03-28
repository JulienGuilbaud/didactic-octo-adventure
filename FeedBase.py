import pandas as pd
from data_processing import (
    clean_description,
    process_brand,
    process_mpn,
    process_title,
    process_description,
    process_id,
    process_link,
    process_image_link,
    process_additional_image_link,
    process_availability,
    process_store_code,
    process_condition,
    format_price,
    format_sale_price
)



def creer_flux_merchant_center(fichier_entree, fichier_sortie, domaine, pays, lang, remise):
    """
    Crée le flux de produits pour Google Merchant Center.

    Args:
        fichier_entree: Chemin du fichier CSV d'entrée.
        fichier_sortie: Chemin du fichier CSV de sortie.
        domaine: Domaine du site web.
        pays: Code pays pour le flux.
        lang: langue du flux
        remise: coefficient de remise
    """
    try:
        df = pd.read_csv(fichier_entree, encoding='utf-8')

        # Validation initiale
        df = df.dropna(subset=['Product/ID'])
        print(f"Nombre de lignes après suppression des lignes sans Product/ID: {len(df)}")

        # Traitement des données
        df['brand'] = process_brand(df['Brand'])
        print(f"Traitement de la colonne 'brand' terminé. Nombre de lignes: {len(df)}")

        df['mpn'] = process_mpn(df['Internal Reference'])
        print(f"Traitement de la colonne 'mpn' terminé. Nombre de lignes: {len(df)}")

        df['condition'] = process_condition(df['Product Category'])
        print(f"Traitement de la colonne 'condition' terminé. Nombre de lignes: {len(df)}")

        df['title'] = df.apply(lambda row: process_title(row['condition'], row['Name'], row['brand'], row['mpn']), axis=1)
        print(f"Traitement de la colonne 'title' terminé. Nombre de lignes: {len(df)}")

        df['description_propre'] = df['Description for the website'].apply(clean_description)
        print(f"Traitement de la colonne 'description_propre' terminé. Nombre de lignes: {len(df)}")

        df['description'] = process_description(df['brand'], df['mpn'], df['description_propre'])
        print(f"Traitement de la colonne 'description' terminé. Nombre de lignes: {len(df)}")

        df['id'] = process_id(pays, lang, df['Product/ID'])
        print(f"Traitement de la colonne 'id' terminé. Nombre de lignes: {len(df)}")

        df['link'] = process_link(domaine, df['Website URL'])
        print(f"Traitement de la colonne 'link' terminé. Nombre de lignes: {len(df)}")

        df['image_link'] = process_image_link(df['Product/ID'])
        print(f"Traitement de la colonne 'image_link' terminé. Nombre de lignes: {len(df)}")

        df['additional_image_link'] = process_additional_image_link(df['Product Images/Image URL'])
        print(f"Traitement de la colonne 'additional_image_link' terminé. Nombre de lignes: {len(df)}")

        df['availability'] = process_availability()
        print(f"Traitement de la colonne 'availability' terminé. Nombre de lignes: {len(df)}")

        df['store_code'] = process_store_code()
        print(f"Traitement de la colonne 'store_code' terminé. Nombre de lignes: {len(df)}")

        df['price'] = df.apply(lambda row: format_price(row['Google Sales Price'], remise), axis=1)
        print(f"Traitement de la colonne 'price' terminé. Nombre de lignes: {len(df)}")

        df['sale_price'] = df['Google Sales Price'].apply(format_sale_price)
        print(f"Traitement de la colonne 'sale_price' terminé. Nombre de lignes: {len(df)}")



        # Écriture du fichier de sortie
        output_columns = ['id', 'brand', 'mpn', 'title', 'description', 'link', 'image_link', 'additional_image_link', 'price', 'sale_price', 'availability', 'store_code', 'condition']
        df[output_columns].to_csv(fichier_sortie, index=False, encoding='utf-8')
        print(f"Fichier de sortie '{fichier_sortie}' créé avec succès. Nombre de lignes: {len(df)}")

    except FileNotFoundError:
        print(f"Error: Input file '{fichier_entree}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
