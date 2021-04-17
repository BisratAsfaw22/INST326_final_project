class Inventory:
	""" Generates an inventory.
   	Attributes:
       inventory (dict): inventory of all grocery store products
   	"""
    def __init__(self, list_of_products):
    	""" Creates an inventory by reading through the products CSV file and
 				adding each product to a dictionary, where the product name
     			serves as the key and a dictionary containing the other
        		characteristics serves as the value.
        Args:
        	list_of_products (str): file path to CSV file with all grocery store
           		products
        Side Effects:
            Creates and modifies values of tokens and key/value pairs of
           		dictionary for inventory atrribute line by line.
        """
    def get_information(self, product):
        """ Returns information about the product.
		Args:
	    	product (str): name (dictionary key) of product
		Returns:
			characteristics (dict): dictionary value associated with name key
   				containing rest of product information (i.e. price, aisle).
		"""
    def suggest(self, product):
		""" Recommends three alternative products to the customer.
		Args: 
			product (str): name (dictionary key) of product
		Returns: 
			results (list): list of names (strings) of three alternative
   				products recommended according to the characteristics of the
     			specified product.
		"""

class User:
	""" Generates a user.
	Attributes:
 		name (str): name of user
		cart (dict): container which stores products
	""" 
    def __init__(self, name, cart):
        """ Generates a grocery store application user who can search for a
        		product, as well as add products to a cart or remove unwanted
          		products from the cart. When finished, the user can check out.
        Args:
	    	name (str): name of user
	    	cart (dict): container which stores product names (strings) as
      			keys and quantities (integers) as associated values
        Side Effects:
            Modifies values of name and cart.
    	"""   
	def search_product(self, query):
        """ Looks up a specific product through entry of a search term, which
        		then shows ten results accoording to relevance through Pandas.
	    Args:
     		query (str): search term
		Side Effects:
			Modifies values of query and results.
		Returns:
			results (list): list of ten product names (strings) which match the
   				query
		"""
	def add_product_to_cart(self, product, amount=1):
        """ Adds a specific amount of a particular product to the cart.
        Args: 
			product (str): name (dictionary key) of product
   			amount (int): exact amount of product that will be added to the
      			cart
        Side Effects:
			Modifies values of quantity and stock key/value pairs of
           		dictionary for cart attribute.
        Raises:
			ValueError: amount is less than 1.
      	Returns:
			cart_status (str): statement of the quantity (integer) of product in
   				the customer cart after the specified amount of product was
       			added.
		"""
    def remove_product_from_cart(self, product, amount=1):
		""" Removes a specific amount of a particular product from the cart.
  		Args: 
			product (str): name (dictionary key) of product
     		amount (int): exact amount of product that will be added to the
      			cart
        Side Effects:
			Modifies values of quantity and stock key/value pairs of
           		dictionary for cart attribute.
        Raises:
			ValueError: amount is less than 1.
     	Returns:
			cart_status (str): statement of the quantity (integer) of product in
   				the customer cart after the specified amount of product was
       			removed.
		"""
    def print_receipt(self):
        """ Prints statement of all products, amounts, and total cost using
        		Pandas.
        Side Effects:
			Prints dictionary of all product names and associated quantities
   				as part of cart dictionary.
   			Prints total cost (float) of all products.
		"""
    ###def check_out:
    	# Determines the total cost of the products in the cart
if __name__ == "__main__":
    """ Runs specific order of function calls when program is operated (will
    		be more fleshed out later on).
    """
    User.name = input("What is your name?")
    print ("Welcome, " + User.name + " .")
    User.search_product("What are you looking for?")
