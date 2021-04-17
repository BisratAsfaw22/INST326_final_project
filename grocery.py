class Inventory:
	""" Generates an inventory.
   	Attributes:
       inventory (dict): inventory of all grocery store products
   	"""
    def __init__(self, list_of_products):
    	""" Creates an inventory by reading through the products CSV file and
 				adding each product to a dictionary, where the product name
     			serves as the key and a dictionary containing the other
        		attributes servea as the value.
        Args:
        	list_of_products (str): file path to CSV file with all grocery store
           		products
        Side Effects:
            Creates and modifies values of tokens and key/value pairs of
           		dictionary of inventory atrribute line by line.
        """
    def get_product(self, product):
        """ Returns information about the product.
	
	Args:
	    product (str): represents the product including its name and other
     		information
		
	Returns:
		A dictionary with the product information
	"""
    def suggest(self,product):
	"""recommend three alternate products to the customer.
	Args: 
		Product(str): represent the names of the products.
	Returns: 
		The names (str) of three products recommended according to the
  			attributes of the designated product.
	"""

class User:
	""" It asks the user for an input of a product's name of their interest and
 			finds it. Adds product into the cart or removes unwanted product
    		from the cart.

	Attributes:
		product(str): indicates information of the product
		cart(str): contains information on what is in the user's cart
	""" 
    def __init__(self,name, cart):
        """ It generates a grocery store application user where it asks the user
        		for an input of a product name.
	
	Args:
	    name(string): the name of the product
	    cart: represents the user's cart and includes the products in the cart
	    
	Returns:
	    Asks the user to input a product of their interest
	"""
	def search_product(self, query):
        """ It looks up a specific product through entry a search term, which
        		then shows ten results accoording to relevance through Pandas
	    
	Args:
	    query: finds products
	"""
	def add_product_to_cart(self, product, quantity=1):
        """ Adds a specific amount of a particular product to the customer cart.
        Args: 
			product (str): represent the name key value of the product that the
   				customer has in the cart.
   			quantity (int): represents the exact amount of each product that
      			will be added to the cart. 
      	Returns:
			Returns the quantity of product in the customer cart after the
   				specified quantity of product was removed.
		"""
    def remove_product_from_cart(self, product, quantity=1):
	""" Remove a specific amount of a particular product from the customer cart.
	
	Args: 
		product(str): represent the list of the product name that the customer
  			has in his cart.
		
		Quantity(int): represent the exact amount of each product that will be
  			removed from the cart. 
		
	Returns:
		returns the list of product left in the customer cart after the quantity
  			of product was removed.
	"""
 
	###def check_out:
        # Determines the total cost of the items in the cart
    ###def print_receipt:
        # Prints out a list of the items using Pandas, along with the total cost
if __name__ == "__main__":
    """ Runs specific order of function calls when program is operated (will
    		be more fleshed out later on).
    """
    args = parse_args(sys.argv[1:])
