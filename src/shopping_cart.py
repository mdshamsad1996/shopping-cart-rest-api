"""Business logic"""

from src.MongoDb import db


class Cart():
    """shopping cart class"""

    def __init__(self):

        """shoping cart constructor"""
        pass

    def create_shopping_cart(self, cart_details):

        """Create shopping cart"""

        result = db.create_cart_document(cart_details)

        return result

    def delete_cart_using_cart_id(self, cart_id):

        """delete cart using cart_id"""

        result = db.delete_cart_via_cart_id(cart_id)

        return result

    def get_shopping_cart_via_cart_id(self, cart_id):

        """Get shopping cart via a cart_id"""

        result = db.fetch_particular_cart_details(cart_id)

        return result

    def add_item_to_cart(self, cart_id, item):

        """Add an item to cart"""

        result = db.add_item_to_cart(cart_id, item)

        return result

    def update_item_to_cart(self, cart_id, item_id, item):

        """update an item to particular cart"""

        result = db.update_an_item_to_cart(cart_id, item_id, item)

        return result

    def delete_item_from_cart(self, cart_id, item_id):

        """delete an item from shopping cart"""

        result = db.delete_an_item_from_cart(cart_id, item_id)

        return result
