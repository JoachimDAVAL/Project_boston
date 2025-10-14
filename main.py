import BostonSalary.utils.helpers

url = "https://data.boston.gov/api/3/action/datastore_search?resource_id=31358fd1-849a-48e0-8285-e813f6efbdf1"
df = BostonSalary.utils.helpers.extract_boston_salary(url)
print(df)
