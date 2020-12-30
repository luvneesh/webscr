import requests
import re
from bs4 import BeautifulSoup
page = requests.get('https://www.fogsi.org/')
# Create a BeautifulSoup object
soup = BeautifulSoup(page.content, 'html.parser')
objects=(soup.findAll(text=re.compile(' ')))
print(objects)
# for objecti in objects:
#     objecti.strip()
#     myset=objecti.split(' ')
#     # print(myset)
#     for element in myset:
#         email_pattern = re.compile("[-a-zA-z0-9.]+@[-a-zA-z0-9.]+.[-a-zA-z0-9_]+")
#         emails = re.findall(email_pattern, element)
#         for email in emails:
#             if len(email)>0:
#                 print(email)