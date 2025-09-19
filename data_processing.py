from bs4 import BeautifulSoup
import pandas as pd

def clean_description(desc):
    """Nettoie la description HTML, la tronque, et supprime les espaces inutiles."""
    if pd.isna(desc):
        return "Contact us for more details!"
    text = BeautifulSoup(str(desc), 'html.parser').get_text()
    cleaned_text = ' '.join(text.split())
    return cleaned_text[:5000]

def process_brand(brand_column):
    """Traite la colonne 'brand'."""
    return brand_column.fillna('MICPARTSONLINE').str[:50]

def process_mpn(mpn_column):
    """Traite la colonne 'mpn'."""
    return mpn_column.str[:50]

def process_condition(condition_column):
    """Traite la colonne 'condition'."""
    return condition_column.astype(str).str.lower()

def process_title(condition, title_column, brand_column, mpn_column):
    """Traite la colonne 'title'."""
    if str(condition).lower() == "new parts":
        return (str(brand_column)+' '+ str(title_column))[:150]
    else:
        return (str(brand_column)+' '+ str(mpn_column)+' '+ str(title_column))[:150]

def process_description(brand_column, mpn_column, description_propre_column):
    """Traite la colonne 'description'."""
    return (brand_column.astype(str) + ' - ' + mpn_column.astype(str)+ ' - ' + description_propre_column.astype(str)).str[:5000]

def process_id(pays, lang, id_column):
    """Traite la colonne 'id'."""
    return pays + lang + id_column.astype(int).astype(str)

def process_link(domaine, link_column):
    """Traite la colonne 'link'."""
    return domaine + link_column.astype(str)

def process_image_link(id_column):
    """Traite la colonne 'image_link'."""
    return 'https://www.micpartsonline.com/web/image/product.product/' + id_column.astype(int).astype(str) + '/image_1024'

def process_additional_image_link(additional_image_link_column):
    """Traite la colonne 'additional_image_link'."""
    return additional_image_link_column

def process_availability():
    """Traite la colonne 'availability'."""
    return 'in_stock'

def process_store_code():
    """Traite la colonne 'availability'."""
    return 'entrepot-lévis'

def process_google_product_category():
    """Attribue l'ID de la catégorie de produits Google par défaut."""
    return '8038'

def format_price(price, remise):
    """Formate le prix en tenant compte de la remise et du cas où le prix est 0."""
    if price == 0:
        return "9999.99 CAD"
    else:
        return "{:.2f} CAD".format(price * remise)

def format_sale_price(price):
    """Formate le prix de vente en tenant compte du cas où le prix est 0."""
    if price == 0:
        return "9999.99 CAD"
    else:
        return "{:.2f} CAD".format(price)


