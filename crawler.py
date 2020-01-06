# Libraries
import requests
from bs4 import BeautifulSoup
import query_order

url = "au.indeed.com"
term = "data analyst"

def crawl(site, term):
    search = get_search(site, term)
    requests.get(search)
