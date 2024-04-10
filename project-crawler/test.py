from bs4 import BeautifulSoup
import requests
import re

#open link
def open_link(str_url):
    respone = requests.get(str_url)
    soup = BeautifulSoup(respone.content,'html.parser')
    return soup

#crawler
def get_context(source_content):
    get_contents =[]
    new_contents=[]
    get_content = source_content.find_all('td',class_='confname')

    for item in get_content:
        
        get_contents.append(item)
    
    for item in get_contents:
        get_tag = item.find_all('a')
        for new_item in get_tag:
            new_contents.append(new_item.get_text()) 
    return new_contents

str_url = 'https://www.lix.polytechnique.fr/~hermann/conf.php'
source =open_link(str_url)
get_contents = []
get_contents = get_context(source)

for item in get_contents:
    print(item)
