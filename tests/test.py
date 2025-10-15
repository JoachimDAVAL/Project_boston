import pandas as pd
import pytest
from BostonSalary.utils.helpers import extract_boston_salary
from unittest.mock import patch, Mock
from etl.models.user import analyse
from BostonSalary.utils.transform import transform


def test_extract_boston_salary():
    url = "https://data.boston.gov/api/3/action/datastore_search?resource_id=31358fd1-849a-48e0-8285-e813f6efbdf1"

    # On mock la réponse afin de simuler un appel API
    mock_response = Mock()

    # On définit le JSON que la réponse mockée doit retourner
    mock_response.json.return_value = {
        "result": {
            "records": [
                {"id": 1, "name": "John Doe", "total_earnings": 50000},
                {"id": 2, "name": "Jane Smith", "total_earnings": 60000}
            ]
        }
    }

    # On utilise patch pour remplacer requests.get par notre mock
    with patch("requests.get") as mock_get:

        mock_get.return_value = mock_response


        # Appel de la fonction à tester
        df = extract_boston_salary(url)

        # On vérifie que le DataFrame est correct
        assert isinstance(df, pd.DataFrame)

        expected_columns = ['id', 'name', 'total_earnings']
        assert all(column in df.columns for column in expected_columns)

        assert len(df) == 2

    pass

def test_transform_converts_total_earnings():

    data_example = {
        "NAME": ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace"],
         "TOTAL EARNINGS": ["1,200.50", "3000", None, "1,200.50", "4000", "abc", "5,000"]
    }

    df_test = pd.DataFrame(data_example)
    df_result = transform(df_test)

    # Vérifie qu'il n'y a plus de NaN
    assert df_result["TOTAL EARNINGS"].isna().sum() == 0

    # Vérifie que le type est float
    assert df_result["TOTAL EARNINGS"].dtype == float

    # Vérifie qu'il n'y a plus de doublons
    assert df_result.duplicated().sum() == 0

    # Vérifie que certaines valeurs sont correctes
    assert 1200.50 in df_result["TOTAL EARNINGS"].values
    assert 5000.0 in df_result["TOTAL EARNINGS"].values

    
    pass


def test_analyse_returns_dict():

    # Création d'un DataFrame de test
    data_example = {
        "department": ["Finance", "Finance", "IT", "IT", "HR", "HR"],
        "total_earnings": [50000, 60000, 70000, 65000, 40000, 45000]
    }
    df_test = pd.DataFrame(data_example)

    # Appel de la fonction analyse
    stats = analyse(df_test)

    # Vérification que le résultat est un DataFrame
    expected_columns = ["department", "mean", "median", "min", "max"]
    for col in expected_columns:
        assert col in stats.columns

    # Vérification de la moyenne calculée pour le département "Finance"
    finance_mean_expected = (50000 + 60000) / 2
    assert stats.loc[stats['department'] == "Finance", 'mean'].values[0] == finance_mean_expected

    # Vérification de la médiane calculée pour le département "Finance"
    finance_median_expected = 55000
    assert stats.loc[stats['department'] == "Finance", 'median'].values[0] == finance_median_expected
