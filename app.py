# 1. ライブラリをインポートする
import requests
from bs4 import BeautifulSoup
import streamlit as st
import random

# 2. スクレイピングするWebサイトのURLを指定する
url = "https://www.mcdonalds.co.jp/menu/"

# 3. WebサイトからHTMLデータを取得し、適切な形式で保存する
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# 4. 取得したHTMLデータを解析し、商品名と料金を抽出する
lineup = [item.text for item in soup.find_all(class_="product-list-card-name font-bold mt-2 mb-2 mb-4:md")]
price =  [item.text.replace("~","") for item in soup.find_all(class_="product-list-card-price-number text-2xl font-extrabold")] 
products =[]

for i in range(len(price)):
    products.append({"name":lineup[i],"price":price[i]})
    
    



st.sidebar.title("商品一覧")
for product in products:
    st.sidebar.markdown(f"- {product['name']}: {product['price']}円")


button = st.button("Choice!")



if button:
    selected_products = []
    total_price = 0
    for product in products:
        if total_price + product["price"] <= 1000:
            selected_products.append(product)
            total_price += product["price"]
    for product in selected_products:
        st.write(f"- {product['name']}: {product['price']}円")
    st.write(f"合計金額: {total_price}円")
    
