import json
import urllib.request
import pandas as pd
import numpy as np

def transform(df_clean: pd.DataFrame) -> pd.DataFrame:
    """Nettoie et transforme les données de salaires."""
    # Retire la virgule, passe en float
    df_clean["TOTAL EARNINGS"] = df_clean["TOTAL EARNINGS"].astype(str).str.replace(r",", "", regex=True)
    df_clean["TOTAL EARNINGS"] = df["TOTAL EARNINGS"].astype(float, errors='ignore')

    # Supprime toutes les valeurs erronées dans Total Earnings
    df_clean = df_clean.dropna(subset=["TOTAL EARNINGS"])

    #Supprime tout les doublons
    df_clean = df_clean.drop_duplicates(keep='last')
    
    #Réindexe le tableau
    df_clean = df_clean.reset_index(drop=True)
    return df_clean
