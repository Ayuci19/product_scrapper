from bs4 import BeautifulSoup
import requests

def scrape_search_page(url):
    #saves all the links in a list
    link = url 
    
    links_in_page , temp = [] , []

    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}

    page = requests.get(link, headers = header)

    soup = BeautifulSoup(page.content , "html.parser")

    soup1 = BeautifulSoup(soup.prettify(), "lxml")

    links = soup.find_all("a", attrs={'class':'a-link-normal s-no-outline'})    

    for link in links:
        temp.append(link.get('href'))

    #cleaning an filtering links and crap links
    for i in temp:
        i = i.strip()
        if('sspa' not in i):
            links_in_page.append(i)

    return links_in_page


def create_text_file(list,name):
    #prints list of links in txt file of user defined name line by line
    with open(f'{name}.txt', 'w') as f:
        for item in list:
            f.write("https://www.amazon.in" + item + "\n")



#OPERATOR CODE 


output_name = input("Enter the name of the output txt file (without extension) : ")

base_page = "https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_1"


#generate links for further scraping 
input_links = []

for i in range(2,9):
    query = base_page[:-1]+str(i)
    input_links.append(query)
for i in range(1,10):
    query = base_page[:]+str(i)
    input_links.append(query)

#https://www.amazon.in/s?k=pendrive&page=7

#saving ALL the links in one single list 
final = []

for i in input_links:
    print(f"Currently on page number : {input_links.index(i) + 1}")
    temp = scrape_search_page(i)
    final.extend(temp)

#genrating txt file
create_text_file(final, output_name)


