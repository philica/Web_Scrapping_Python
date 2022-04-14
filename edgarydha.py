import requests
from bs4 import BeautifulSoup

base_url = r"https://www.sec.gov/Archives/edgar/data"

# defining CIK number of Fidelity bank located in Virginia 
# Fudelity bank base url = https://www.sec.gov/Archives/edgar/data/0001028336/

cik_number="/0001028336"

# now let's create filings url
filings_url = base_url + cik_number + "/index.json"
print(filings_url)

#requesting url
headers = {'user-agent': 'sample text'}
content = requests.get(filings_url,headers=headers)
decoded_content = content.json()
print(decoded_content)
# create a single filing url 

filing_number = decoded_content['directory']['item'][0]['name']

filing_url = base_url + cik_number + filing_number + "/index.json"
