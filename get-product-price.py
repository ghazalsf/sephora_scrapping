import pandas as pd
import requests
import time
from bs4 import BeautifulSoup as bs

price_list = []
url_list = []

products_df = pd.read_csv('product-features.csv')
link_list = list(products_df['link'])
products_df = pd.read_csv('product-features.csv')
products_df['price']= ''

headers = {'User-agent': 'Mozilla/5.0'}

for i in range (len(link_list)):
    
    page = requests.get(link_list[i], headers=headers)
    bs_page = bs(page.content, 'lxml')

    try: 
        price_values = bs_page.find('b', class_="css-0")
        print(price_values)
        price = price_values.contents

        if price != None:
            price = " ".join(price)
            products_df['price'][i] = price


        else:
            products_df['price'][i] = "None"
            
        
    except:
        print(link_list[i])
    
    products_df.to_csv('product-features-priced.csv', index=False)
    time.sleep(5)
    
