import requests
from bs4 import BeatifulSoup

# getting links to each of the industry pages needed for analysis.
rt_url = "https://www.bls.gov/iag/tgs/iag44-45.htm"
wt_url = "https://www.bls.gov/iag/tgs/iag42.htm"
mfg_url = "https://www.bls.gov/iag/tgs/iag31-33.htm"
fin_url = "https://www.bls.gov/iag/tgs/iag50.htm"

rt_html = requests.get(rt_url)
wt_html = requests.get(wt_url)
mfg_html = requests.get(mfg_url)
fin_html = requests.get(fin_url)

rt_soup = BeautifulSoup(rt_html.content, 'html.parser')
wt_soup = BeautifulSoup(wt_html.content, 'html.parser')
mfg_soup = BeautifulSoup(mfg_html.content, 'html.parser')
fin_soup = BeautifulSoup(fin_html.content, 'html.parser')

