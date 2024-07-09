from fastapi import FastAPI
from product import Product
from jsondb import JsonDB

app = FastAPI()

productDB = JsonDB(path='./data/products.json')

@app.get('/products')
def get_products():
    products = productDB.read()
    return { 'Products': products }

@app.post('/products')
def create_products(product: Product):

    productDB.insert(product)
    
    return { "status": "sucess" }