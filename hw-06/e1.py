# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 21:18:06 2016

@author: Lim Cheng Yee
"""

import requests
from bs4 import BeautifulSoup

elec_add = "http://historical.elections.virginia.gov/elections/search/year_from:1924/year_to:2015/office_id:1/stage:General"

resp = requests.get(elec_add)
soup = BeautifulSoup(resp.content , "html.parser")
tables = soup.find("table")

with open("ELECTION_ID", "w") as out:
    for i in soup.find_all("tr", "election_item"):
        el_id = int(i["id"].split("-")[-1])
        year = int(i.find("td", "year").string)
        out.write("{} {} ".format(year, el_id))