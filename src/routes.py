"""Route Module"""

from flask import request, json
from src.shopping_cart import Cart
from src import app

cart = Cart()


@app.route('/cart/', methods=['POST'])
def create_cart():

    """Creating cart"""

    cart_details = json.loads((request.data).decode('utf-=8'))

    message = cart.create_shopping_cart(cart_details)

    return json.dumps(message)


@app.route('/cart/<int:cart_id>/', methods=['GET'])
def get_cart(cart_id):

    """Get cart via cart_id"""

    cart_details = cart.get_shopping_cart_via_cart_id(cart_id)

    return json.dumps(cart_details)


@app.route('/cart/<int:cart_id>/', methods=['DELETE'])
def delete_cart(cart_id):
    """delete a cart"""

    message = cart.delete_cart_using_cart_id(cart_id)

    return json.dumps(message)


@app.route('/cart/<int:cart_id>/item/', methods=['POST'])
def add_item(cart_id):

    """Adding item to cart"""

    item = json.loads((request.data).decode('utf-=8'))

    message = cart.add_item_to_cart(cart_id, item)

    return json.dumps(message)


@app.route('/cart/<int:cart_id>/item/<int:item_id>/', methods=['PUT'])
def update_item(cart_id, item_id):

    """"Updating item to cart"""

    item = json.loads((request.data).decode('utf-=8'))

    message = cart.update_item_to_cart(cart_id, item_id, item)

    return json.dumps(message)


@app.route('/cart/<int:cart_id>/item/<int:item_id>/', methods=['DELETE'])
def delete_item(cart_id, item_id):

    """delete an item from cart"""

    message = cart.delete_item_from_cart(cart_id, item_id)

    return json.dumps(message)
