from flask import Flask, render_template, request
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import logging
import requests
import pymongo

app=Flask(__name__)
FLIPKART_URL="https://www.flipkart.com/search?q="

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/review',methods=["GET","POST"])
def web_scraper():
    if request.method=="POST":
        data=request.form['content']
        search_url=FLIPKART_URL+data

        data_html=bs(urlopen(search_url).read(),'html.parser')
        data_box=data_html.find_all("div",{"class":"_1AtVbE col-12-12"})
        data_link=data_box.div.div.div.a["href"]

        product_html=bs(urlopen(data_link).read(),'html.parser')
        
        try:
            product_class=product_html.find_all("div",{"class":"_1AtVbE col-12-12"})
            print("*"*50,product_class,"*"*50)
            product_name=(product_class.div.div)[0].text
            print("*"*50,product_name,"*"*50)
        except Exception as e:
            print(e)

        # Product=data
        # Name=
        # Rating=
        # Comment=
        # Heading=
        # mycomment=
        # Comments=        

    return search_url#render_template('result.html',review=data)
        

if __name__=="__main__":
    app.debug='on'
    app.run(host="0.0.0.0")
    