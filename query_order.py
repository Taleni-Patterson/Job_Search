
import re
import requests
from bs4 import BeautifulSoup
import pandas as pd
# Site dictionary
d = {
    "indeed" : {"site":"http://au.indeed.com/jobs?q=TERM&l=LOCATION&start=PAGE",
                "replacements" : ["SEP","TERM","PAGE", "LOCATION"],
                "SEP" :"+",
                "PAGE_ITERATOR" : 10,
                "LOCATION": "Sydney+NSW",
                "DOMAIN":"http://au.indeed.com"}

}
site = "au.indeed.com"
term = "analyst"

indeed = pd.DataFrame()
for s in d.keys():
    if s in site:
        page = 0

        while
        # Setting the required variables.
        site_dict = d[s]
        site_dict["TERM"] = term
        site_dict["PAGE"] = str(page*site_dict["PAGE_ITERATOR"])

        # Substituting them into the string
        pattern = re.compile("|".join(site_dict["replacements"]))
        site_search = pattern.sub(lambda m: site_dict[re.escape(m.group(0))],site_dict["site"])
        req = requests.get(site_search)
        soup = BeautifulSoup(req.text, 'html.parser')
        div = soup.find_all('div', {'class':'title'})
        list_of_pages = [site_dict["DOMAIN"] + d.a['href'] for d in div]

        # Crawling through each page
        for p in list_of_pages:
            req = requests.get(p)
            soup = BeautifulSoup(req.text,'html.parser')
            main_text = soup.find('div', {'id':'jobDescriptionText'})
            print(main_text.find_all('p'))
            break
        # Getting the html


        # print(soup.prettify)
