# %% [markdown]
# <h2><b> Beautiful Soup Project </h2></b>

# %% [markdown]
# This is a web scraping project using Beautiful Soup library. <br>
# Objective: to retrieve data from "wuzzuf.net" with specific search criteria (Data analyst)

# %% [markdown]
# import modules

# %%
import requests
from bs4 import BeautifulSoup
import pandas as pd

# %% [markdown]
# Use requests to fetch the url

# %%
result = requests.get("https://wuzzuf.net/search/jobs/?q=data+analyst&a=hpb")

# %% [markdown]
# Save page content/markup

# %%
src= result.content
#src

# %% [markdown]
# Create soup object to parse the content

# %%
soup=BeautifulSoup(src,"lxml")
#soup

# %% [markdown]
# Find the elements that contain the needed info:<br>
# Job title, company name, location, skills, date, job description, and requirements

# %%
job_titles_html=soup.find_all("h2",{"class":"css-m604qf"})
#job_titles

# %%
company_names_html=soup.find_all("a",{"css-17s97q8"})
#company_names

# %%
locations_html=soup.find_all("span",{"class":"css-5wys0k"})
#locations

# %%
dates_html=soup.find_all("div", {"class":["css-do6t5g","css-4c4ojb"]})
#dates_html

# %%
shift_types_html=soup.find_all("span",{"class":"css-1ve4b75 eoyjyou0"})
#shift_type

# %% [markdown]
# Loop over returned lists to extract needed info into other lists

# %%
job_titles_txt=[]
company_names_txt=[]
locations_txt=[]
dates_txt=[]
shift_types_txt=[]

# %%
for i in range(len(dates_html)):
    job_titles_txt.append(job_titles_html[i].text)
    company_names_txt.append(company_names_html[i].text)
    locations_txt.append(locations_html[i].text)
    dates_txt.append(dates_html[i].text)
    shift_types_txt.append(shift_types_html[i].text)


# %% [markdown]
# Create Dictionary

# %%
dict1={"Job Title":job_titles_txt,
       "Company":company_names_txt,
       "Location":locations_txt,
       "Date":dates_txt,
       "Type":shift_types_txt}
#dict11

# %% [markdown]
# Create Pandas DataFrame

# %%
df=pd.DataFrame(dict1)
df

# %% [markdown]
# Export DataFrame to CSV file

# %%
df.to_csv("jobs.csv", index=False)


