import request
from bs4 import BeautifulSoup

def extract_legal_terms():
    url = "https://www.planalto.gov.br/ccivil_03/_Ato2015-2018/2015/Lei/L13146.htm"
    response = request.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    terms = [tag.text.strip() for tag in soup.find_all('span', class_='termo') if tag.text.strip()]
    return terms
