# service/routes.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    # This should integrate with your model to fetch product
    return jsonify({'id': product_id, 'name': 'Sample Product'}), 200
