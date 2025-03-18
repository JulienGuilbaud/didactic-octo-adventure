import pandas as pd

def validate_data(df):
    """Valide les données du DataFrame."""
    df = df.dropna(subset=['Product/ID'])
    return df
