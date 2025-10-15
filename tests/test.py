import pandas as pd
import pytest
from BostonSalary.utils.helpers import extract_boston_salary
from unittest.mock import patch, Mock
from etl.models.user import analyse


def test_extract_boston_salary():
    url = "https://data.boston.gov/api/3/action/datastore_search?resource_id=31358fd1-849a-48e0-8285-e813f6efbdf1"
    mock_response = Mock()
    mock_response.json.return_value = {
        "result": {
            "records": [
                {"id": 1, "name": "John Doe", "total_earnings": 50000},
                {"id": 2, "name": "Jane Smith", "total_earnings": 60000}
            ]
        }
    }

    with patch("requests.get") as mock_get:
        mock_get.return_value = mock_response
        df = extract_boston_salary(url)

        assert isinstance(df, pd.DataFrame)

        expected_columns = ['id', 'name', 'total_earnings']
        assert all(column in df.columns for column in expected_columns)

        assert len(df) == 2

    pass



def test_analyse_returns_dict():

    data_example = {
        "department": ["Finance", "Finance", "IT", "IT", "HR", "HR"],
        "total_earnings": [50000, 60000, 70000, 65000, 40000, 45000]
    }
    df_test = pd.DataFrame(data_example)

    stats = analyse(df_test)

    expected_columns = ["department", "mean", "median", "min", "max"]
    for col in expected_columns:
        assert col in stats.columns


    finance_mean_expected = (50000 + 60000) / 2
    assert stats.loc[stats['department'] == "Finance", 'mean'].values[0] == finance_mean_expected


    finance_median_expected = 55000
    assert stats.loc[stats['department'] == "Finance", 'median'].values[0] == finance_median_expected
