import requests
from bs4 import BeautifulSoup
import streamlit as st
import random


url = "https://www.mcdonalds.co.jp/menu/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

lineup = [item.text for item in soup.find_all(class_="product-list-card-name font-bold mt-2 mb-2 mb-4:md")]
price =  [item.text.replace("~","") for item in soup.find_all(class_="product-list-card-price-number text-2xl font-extrabold")] 
products =[]

for i in range(len(price)):
    products.append({"name":lineup[i],"price":int(price[i])})
    
    



st.sidebar.title("商品一覧")
for product in products:
    st.sidebar.markdown(f"- {product['name']}: {product['price']}円")


button = st.button("Choice!")



if button:
    selected_products = random.sample(products, len(products))
    total_price = 0
    for product in selected_products:
        if total_price + product["price"] <= 1000:
            total_price += product["price"]
        else:
            break
    for product in selected_products:
        if total_price <= 0:
            break
        st.write(f"- {product['name']}: {product['price']}円")
        total_price -= product["price"]
    
