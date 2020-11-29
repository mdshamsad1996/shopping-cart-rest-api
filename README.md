# shopping cart api

#### Task
* create a shopping cart REST API(Use Python/Mongodb) that handles CRUD operations for a specific user like create cart, get items, add items and remove items.

Below Technologies has been used 

    Language: Python
    Database: NoSQL (MongoDb)
    Framework: Flask
 
 #### Endpoints
 ##### Create a new cart:
* Methods: POST
* Path:  http://127.0.0.1:5000/cart/
* Request Body:

        {  "cart_id": 1, "cart_items": [] }
##### add an item into cart:
* Methods: POST
* Path:  http://127.0.0.1:5000/cart/1/item/
* Request Body:
 
        { "item_id": 1,"item_name": "Bag","price": 500,"quantity": 1}
##### update an item to cart:
* Methods: PUT
* Path:  http://127.0.0.1:5000/cart/1/item/1/
* Request Body:
 
        {"item_name": "Book","price": 50,"quantity": 1}
##### delete an item to cart:
* Methods: DELETE
* Path:  http://127.0.0.1:5000/cart/1/item/1/

##### Get cart via id:
* Methods: GET
* Path:  http://127.0.0.1:5000/cart/1/

##### Delete cart via id:
* Methods: DELETE
* Path:  http://127.0.0.1:5000/cart/1/

           
### Steps
Make sure python (preferred python3.7) is added to path.

      python --version
       or		
     python3.7 --version
     
 Install virtualenv using pip.

     pip install virtualenv 
   
 First create a virtual environment for the project.
 
    virtualenv -p python3.7 venv or virtualenv venv
       . venv/bin/activate (Linux)
       . venv/Scripts/activate (windows)

Install dependencies
    
    pip install -r requirements.txt

set up linter:
 
     scripts/lint.sh
        
 To run app using below command
 
     python run.py