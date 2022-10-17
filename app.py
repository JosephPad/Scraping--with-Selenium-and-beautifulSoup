from bs4 import BeautifulSoup
from selenium import webdriver
import time
from csv import writer


url1='https://webscraper.io/test-sites/e-commerce/scroll' #Home
url2='https://webscraper.io/test-sites/e-commerce/scroll/computers' #computers category
url3='https://webscraper.io/test-sites/e-commerce/scroll/computers/laptops' #computers/laptops
url4='https://webscraper.io/test-sites/e-commerce/scroll/computers/tablets' #computers/tablets
url5='https://webscraper.io/test-sites/e-commerce/scroll/phones' #phones category
url6='https://webscraper.io/test-sites/e-commerce/scroll/phones/touch' #phones touch
url_todas=[url1,url2,url3,url4,url5,url6]


#driver.get(url_todas)

# codigo for para el page de las url
page_todas=[]
soup_todas=[]
list_todas=[]
#driver= webdriver.Chrome('chromedriver')

for count1 in url_todas:
    driver = webdriver.Chrome('chromedriver')
    driver.get(count1)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    time.sleep(3)
    content=driver.page_source.encode('utf-8').strip()
    soup=BeautifulSoup(content,'lxml')
    list = soup.find_all('div', class_='thumbnail')
    #page_todas.append()
    list_todas.append(list)
    driver.quit()

with open('web_scraper.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['Titulo', 'Precio', 'Descripción']
    thewriter.writerow(header)


    for b in range(len(list_todas)):
        for c in list_todas[b]:
            titulo = c.find('a', class_='title').text
            precio = c.find('h4', class_='price').text
            descripcion = c.find('p', class_='description').text
            info = [titulo, precio, descripcion]
            print(info)
            thewriter.writerow(info)

