#importing all the required libraries

from bs4 import BeautifulSoup       #for scraping and making sense
import requests                     #for handling web requests
import csv                          #for csv operations 
import re
#FUNCTION DEFINITIONS

#making list of links by reading from file
def listofLinks(path,fname):
    url_list = []
    with open(f"{path}\{fname}", "r") as file:
        url_list = file.readlines()
    return url_list

#scraping (returns title and price)
def scrape(URL):
    URL = link

    header ={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}

    #getting page using requests module

    page = requests.get(URL, headers=header)


    #getting html content with proper formatting 

    soup1 = BeautifulSoup(page.content, "html.parser")

    #defining title and price
    title,price,rating,nreviews = " ", " ", " ", " "


    try:
        price=" "
        rating=" "
        nreviews=" "
        manufacture=" "
        des=" "
        asin=" "
        prod_des=" "
        title = soup1.find(id='productTitle').get_text()
        price = soup1.find('span', attrs={'class':'a-price-whole'}).get_text()

        #defining rating and number of reviews
        rating =  soup1.find('span', attrs={'class':'a-icon-alt'}).get_text()
        nreviews = soup1.find(id='acrCustomerReviewText').get_text()
        nreviews = soup1.find(id='acrCustomerReviewText').get_text()
        prod_des=""
        asin = re.findall('/[dg]p/([^/]+)',URL)
        if soup1.find(id='bylineInfo')!=None:
            manufacture =soup1.find(id='bylineInfo').get_text()
        else:
            manufacture=" "
        des=soup1.find(id='feature-bullets').get_text()
        prod_des=soup1.find(id='productDescription').get_text()

        title = title.strip()
        price = price.strip()

        price = price[:-1]

        #cleaning rating and nreviews 
        
        rating = rating.strip()
        nreviews = nreviews.strip()

        rating = rating[:3]
        
        i = nreviews.index('r')
        
        nreviews = nreviews[:i]
        
    except(UnboundLocalError,AttributeError,TypeError):
        print("Skipped due to formatting error on page")
    return (title,price,rating,nreviews,manufacture,des,prod_des,asin)

    


#OPERATOR CODE


#printing tool name
print("\n")
print("****************************")
print("WELCOME TO AMAZON SCRAPER !!")
print("****************************")
print("\n")


#taking input from user
name = input("Enter your Name : ")
path = input("Enter the path of text file of links : ")
fname = input("Enter the name of the text file (without ext) : ")
o_path = input("Enter the path of output file (Leave empty if same as above) : ")
o_name = input("Enter the name of the output csv file (without ext) : ")

#condition if output path same as input path

if (o_path == ''):
    o_path = path


#handling condition if user inputs extension with file names

if('.txt' not in fname):
    fname = fname + ".txt"
#adding .csv to new filename
if('.csv' not in o_name):
    o_name = o_name + ".csv"
#creating list of links 
linksList = (listofLinks(path,fname))


#finding number of lines
nLines = len(linksList)

print("\n")
print("Number of links found in txt file : ",end = "")
print(nLines)

print("The file will be created in maximum ",end = "")
print(f"{nLines*4} seconds.")
print("\n")

#creating csv file and writing header in first row
header = ['Title','Price','Rating','Number of Reviews','manufacture','des','prod_des','asin']

with open(f'{o_path}\\{o_name}','w', newline='', encoding='UTF') as f:
    writer = csv.writer(f)
    writer.writerow(header) 

#iterating over every link in list and apending title, price to csv file 
c=1
for link in linksList:
    print(f"Currently processing link number : {c}")
    title , price , rating, nreviews,manufacture,des,prod_des,asin = scrape(link)
    data = [title , price , rating, nreviews,manufacture,des,prod_des,asin]
    if None in data:
        continue
    with open(f'{o_path}\\{o_name}','a+',encoding='UTF',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(data)
        c = c+1
        
print("\n")
print(f"The csv file has been successfully created.")
print("\n")
print("Name of the file = ",end = "")
print(o_name)
print(f"Path of the file = ",end = "")
print(o_path)

print("\n")
print(f"Hey {name}, Thanks a lot for using the tool !!")
print(f"If you have any feedback, follow up here : ", end="")
print(f"https://github.com/adhirajpandey")
print("\n")



