def analyse(df):
    """
    Calcule les statistiques de base sur les salaires par département.
    """
    stats = df.groupby("department")["total_earnings"].agg(['mean','median','min','max']).reset_index()
    return stats
# user.py

import pandas as pd

def analyse(df):
    """
    Calcule les statistiques de base sur les salaires par département.
    """
    stats = df.groupby("department")["total_earnings"].agg(['mean','median','min','max']).reset_index()
    return stats