from flask import Flask, Response, json
from flask_restful import Api, Resource
from NorgesGruppen.norgesgruppen import Store
from NorgesGruppen.norgesgruppen import Product

""" 
Wrapper around NG api to get a product. Use get with a query to retrieve product information.
"""


app = Flask(__name__)
api = Api(app)


meny = Store(1300)


class ProductResource(Resource):
    def get(self, product_query):
        product = Product(meny, product_query)
        try:
            return Response(json.dumps(product.fetch_product_source()), status=200, mimetype='application/json')
        except:
            return Response(json.dumps({'message': 'product not found'}), status=404, mimetype='application/json')


api.add_resource(ProductResource, "/product/<string:product_query>")


if __name__ == "__main__":
    app.run(debug=True)
