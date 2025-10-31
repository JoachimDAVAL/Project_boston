import pandas as pd
from pathlib import Path

def load(df: pd.DataFrame) -> None:
    """Enregistre df en CSV dans BostonSalary/reports/boston_salaries_clean.csv"""
    filepath = Path('BostonSalary/reports/boston_salaries_clean.csv')  
    filepath.parent.mkdir(parents=True, exist_ok=True)  
    df.to_csv(filepath, index=False)
