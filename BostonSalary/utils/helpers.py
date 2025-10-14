import pandas as pd
import requests

def extract_boston_salary(url: str) -> pd.DataFrame:
    """Extrait les données brutes depuis l'API Boston."""
    response = requests.get(url)
    data = response.json()
    if "result" not in data  or "records" not in data["result"]:
        raise ValueError("Structure inattendue dans la réponse de l’API Boston")
    records = data["result"]["records"]
    df = pd.DataFrame(records)
    return df
    