"""Module conatins all method for mongodb"""

from pymongo import MongoClient

client = MongoClient('localhost', 27017)

mydb = client.mydb

shopping_cart = mydb.shopping_cart


def create_cart_document(cart):

    """create shopping cart document"""

    cart_doc = {
            "cart_id": cart["cart_id"],
            "cart_items": cart["cart_items"]
            }

    is_cart_exist = is_document_existed(cart_doc)

    if is_cart_exist:

        return {"message": "cart with this id alraedy exist"}

    result = mydb.shopping_cart.insert_one(cart_doc)

    return {"message": "cart created successfuly"}


def delete_cart_via_cart_id(cart_id):

    """delete a cart via cart_id"""

    cart = shopping_cart.find_one({"cart_id": cart_id})

    if cart is None:
        return {"message": "cart does not exist"}

    mydb.shopping_cart.remove({"cart_id": cart_id})

    return {"message": "cart deleted successfuly"}


def fetch_particular_cart_details(cart_id):

    """fetch the cart via the cart_id"""

    doc = shopping_cart.find_one({"cart_id": cart_id})

    if doc is None:
        return {"message": "cart with this id does not exist"}

    cart = {
            "cart_id": cart_id,
            "cart_items": doc['cart_items']
        }

    return cart


def add_item_to_cart(cart_id, item):

    """Add an item to cart via cart_id"""

    doc = shopping_cart.find_one({"cart_id": cart_id})

    is_item_exist = is_an_item_exists(doc['cart_items'], item['item_id'])

    if is_item_exist:
        return {"message": "This item already exist"}

    item_details = {
        "item_id": str(item['item_id']),
        "item_desc":
            {
                    "item_name": item["item_name"],
                    "item_price": item["price"],
                    "item_quantity": item["quantity"]
            }
    }

    mydb.shopping_cart.update_one(
        {"cart_id": cart_id},
        {"$addToSet": {"cart_items": item_details}}
    )

    return {"message": "item inserted succesfully"}


def update_an_item_to_cart(cart_id, item_id, item):

    """update an item"""

    doc = shopping_cart.find_one({"cart_id": cart_id})

    is_item_exist = is_an_item_exists(doc['cart_items'], item_id)

    if is_item_exist:

        item_details = {

            "item_name": item["item_name"],
            "item_price": item["price"],
            "item_quantity": item["quantity"]
        }

        mydb.shopping_cart.update_one(
            {"cart_id": cart_id, "cart_items.item_id": str(item_id)},
            {"$set": {"cart_items.$.item_desc": item_details}}
        )

        return {"message": "Item updated successfully"}

    return {"message": "item does not exist in cart list"}


def delete_an_item_from_cart(cart_id, item_id):

    """"delete an item from shopping cart"""

    doc = shopping_cart.find_one({"cart_id": cart_id})

    is_item_exist = is_an_item_exists(doc['cart_items'], item_id)

    if is_item_exist:
        mydb.shopping_cart.update(
            {"cart_id": cart_id},
            {"$pull": {"cart_items": {"item_id": str(item_id)}}}
        )

        return {"message": "Item deleted successfully"}

    return {"message": "provided item does not exist in given cart"}


def is_an_item_exists(cart_items, item_id):

    """check whether particular item exist or not"""

    for item in cart_items:
        if item["item_id"] == str(item_id):
            return True

    return False


def is_document_existed(cart):

    """Is document already exist"""

    doc = shopping_cart.find_one({"cart_id": cart["cart_id"]})

    if doc is None:
        return False

    return True
