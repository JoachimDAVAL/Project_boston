import json
import urllib.request
import pandas as pd
from pathlib import Path

def load(df: pd.DataFrame)
    filepath = Path('BostonSalary/reports/boston_salaries_clean.csv')  
    filepath.parent.mkdir(parents=False, exist_ok=True)  
    df.to_csv(filepath) 
