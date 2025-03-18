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

def process_npm(npm_column):
    """Traite la colonne 'npm'."""
    return npm_column.str[:50]

def process_condition(condition_column):
    """Traite la colonne 'condition'."""
    return condition_column.str.lower()

def process_title(brand_column, npm_column, title_column, condition_column):
    """Traite la colonne 'title'."""
    if condition_column == "New Parts":
        return title_column.str[:150]
    else:
        return (brand_column.astype(str) + ' ' + npm_column.astype(str) + ' ' +
            title_column.astype(str)).str[:150]

def process_description(brand_column, npm_column, title_column, description_propre_column):
    """Traite la colonne 'description'."""
    return (brand_column.astype(str) + ' - ' + npm_column.astype(str) + ' - ' +
            title_column.astype(str) + ' - ' + description_propre_column.astype(str)).str[:5000]

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


