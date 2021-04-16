###class Product:
    ###def __init__(self, name, type, aisle, price, quantity, stock):
    
### CHANGES:
# Modify docstring length to be shorter than 80 characters per line.
# Change class/method descriptions to be concise.
# Include type of variable (str, dict, etc.) when referenced in docstring.

class Inventory:
	""" Generates an inventory by reading through the products CSV file and adding each product to a dictionary, where the product name serves as the key.
   	Attributes:
       inventory (dict): inventory of all grocery store products
   	"""
    def __init__(self, list_of_products):
    	""" Initializes product entries for the inventory object.
        Args:
           list_of_products (str): file path to CSV file with all the products in the grocery store
        Side Effects:
           Creates and modifies value of tokens and key/value pairs of dictionary of inventory atrribute line by line.
        """
    def get_product(self, product):
        """ Returns informatoin about the product.
	
	Args:
	     product (str): represents the product including its name and other information
		
	Returns:
		A dictionary with the product information
	"""
    def suggest(self,product):
	""" This method has two parameter and it is use to recommend three alternate product to the customer.
	Args: 
		Product: which will represent the names of the recommend products.
	Returns: 
		It should return the name any product that the customer picked from the recommended products.
	"""

class User:
	""" It asks the user for an input of a product's name of their interest and finds it. Adds product into 
		the cart or removes unwanted product from the cart.

	Attributes:
		product(str): indicates information of the product
		cart(str): contains information on what is in the user's cart
	""" 
    def __init__(self,name, cart):
        """ It generates a grocery store application user where it asks the user for an input of a product 
			name.
	
	Args:
	    name(string): the name of the product
	    cart: represents the user's cart and includes the products in the cart
	    
	Returns:
	    Asks the user to input a product of their interest
	"""
	def search_product(self, query):
        """ It looks up a specific product through entry a search term, which then shows ten 
			results accoording to relevance through Pandas
	    
	Args:
	    query: finds products
	"""
    def examine(self, product):
    	""" Examines a product and returns its attributes as given in its dictionary entry.
       	Args:
           product: Product object which the user would like to obtain information from
      	Exceptions:
           NameError: product is not a product in the inventory
      	Returns:
           Returns string labels with corresponding variables (name, type, aisle, price, quantity, and stock) as part of the list associated with the product name key.
        """
	def add_product_to_cart(self, product, quantity=1):
        *** Adds a specific amount of a particular product to the cart
    def remove_product_from_cart(self, product, quantity=1):
	""" This methode has 3 parameters and it is use to a specific amount of a particular product from the customer cart.
	
	Args: 
		product: which represent the list of the product name that the customer has in his cart.
		
		Quantity: which represent the exact amount of each product that will be removed from the cart. 
		
	Returns:
		This should return the list of product left in the customer cart after the quantity of product was removed.
	"""
        
	def check_out:
        *** Determines the total cost of the items in the cart
    def print_receipt:
        *** Prints out a list of the items using Pandas, along with the total cost

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
