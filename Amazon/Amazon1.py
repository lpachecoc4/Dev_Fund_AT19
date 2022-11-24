#import requests
#import _sqlite3
#headers=  {'User-Agent':'Mozila/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
#result = requests.get("https://www.amazon.com/?&tag=googleglobalp-20&ref=pd_sl_7nnedyywlk_e&adgrpid=82342659060&hvpone=&hvptwo=&hvadid=585475370855&hvpos=&hvnetw=g&hvrand=6017720129362202613&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9069868&hvtargid=kwd-10573980&hydadcr=2246_13468515&gclid=Cj0KCQiA99ybBhD9ARIsALvZavXERf_S5AKvA26TCdxc-tLaWqEwJtpQNSeUJ8A6BYa6Inq0sk0RGSIaAg-tEALw_wcB", headers=headers)
#requests.head('')
#print(result.text)
#print(result.status_code)

from flask import Flask
from models.Product import Product
from models.Product import ProductJSONEncoder
import json
from flask_cors import CORS
from flask import request

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/time")
def my_time():
    return '<button>it is my time</button>'

#@app.route("/register")
#1def register():
    #return result.text
    #return result

@app.route("/product")
def get_products():
    text = request.args.get('text')
    print(text)
    # const productos = [
    #   {nombre: 'Platanos', valor : 500},
    #   {nombre: 'Pera', valor : 500},
    #   {nombre: 'Sandia', valor : 500},
    #   {nombre: 'Melon', valor : 500},
    #   {nombre: 'Frutillas', valor : 500},
    #   ]
    list_of_products = []
    list_of_products.append(Product('Wireless Mouse','TECKNET Pro 2.4G Ergonomic Wireless Optical Mouse with USB Nano Receiver for Laptop',500, 'https://m.media-amazon.com/images/I/61U4Qj2jqmL._AC_UY218_.jpg' ))
    list_of_products.append(Product('Pera','My Fruit',500 , 'https://m.media-amazon.com/images/I/61U4Qj2jqmL._AC_UY218_.jpg'))
    list_of_products.append(Product('Sandia','My Fruit',500, 'https://m.media-amazon.com/images/I/61U4Qj2jqmL._AC_UY218_.jpg'))
    list_of_products.append(Product('Melon','My Fruit',500 , 'https://m.media-amazon.com/images/I/61U4Qj2jqmL._AC_UY218_.jpg'))
    list_of_products.append(Product('Frutillas','My Fruit',500, 'https://m.media-amazon.com/images/I/61U4Qj2jqmL._AC_UY218_.jpg' ))
    

    return json.dumps(list_of_products, cls=ProductJSONEncoder)