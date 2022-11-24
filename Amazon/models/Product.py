from json import JSONEncoder

class Product:
    def __init__(self, name, description, price, image_url):
        self.name =  name
        self.description = description
        self.price = price
        self.image_url = image_url

class ProductJSONEncoder(JSONEncoder):
    def default(self, obj):
        return obj.__dict__
