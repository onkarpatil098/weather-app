import requests

res = requests.get("https://api.cowin.gov.in/api/v1/reports/v2/getPublicReports?state_id=21&district_id=375&date=2021-09-27")
data = res.json().get('getBeneficiariesGroupBy')
print(len(data))