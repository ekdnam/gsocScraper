import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

years = ["2016", "2017", "2018", "2019", "2020"]

for year in years:
    # generate dynamic links using f-strings
    link = f"https://summerofcode.withgoogle.com/archive/{year}/organizations/"
    print(f"Accessing link: {link}")
    # get the page
    page = requests.get(link)
    # create BeautifulSoup object
    soup = BeautifulSoup(page.content, "html.parser")

    orgs = soup.find_all(name="h4", attrs="organization-card__name font-black-54")
    descs = soup.find_all(name="div", attrs="organization-card__tagline font-black-54")

    lenOrgs = len(orgs)

    # orgs list
    orgs_list = []
    for org in orgs:
        orgs_list.append(org.string)

    # desc list
    desc_list = []
    for desc in descs:
        desc_list.append(desc.string)

    # output dictionary
    out = {"Organization": orgs_list, "Description": desc_list}

    df = pd.DataFrame.from_dict(out)

    df.to_csv(f"data/{year}.csv", index=False)
