class Product:
    def __init__(self, name, type, aisle, price, quantity, stock):

class Inventory:
    def __init__(self, list_of_products):
        *** Generates an inventory by reading through the products CSV file and adding each product to a dictionary, where the product name serves as the key
    def get_product(self, product):
        """ This method has two parameters and it searches for the given product name through the dictionary.
	
	Args:
	     product: represents the product including its name and other information
		
	Returns:
		The product with its information
	"""
    def suggest(self,product):
        *** Suggests three products relevant to a designated product according to a specified attribute (type, aisle, etc.)

class User:
    def __init__(self,name, cart):
        """ This method takes three parameters and it generates a grocery store application user where it asks the user for an input.
	
	Args:
	    name(string): the name of the product
	    cart: represents the users cart information
	    
	Returns:
	    The user's input
	"""
	def search_product(self, query):
        """ This method takes two parameters and looks up a specific product through entry a search term, which then shows ten results accoording
	    to relevance through Pandas.
	    
	Args:
	    query: searches product
	"""
    def examine(self, product):
        *** Examines a product and returns its attributes as given in its dictionary entry
	def add_product_to_cart(self, product, quantity=1):
        *** Adds a specific amount of a particular product to the cart
    def remove_product_from_cart(self, product, quantity=1):
        *** Removes a specific amount of a particular product from the cart
	def check_out:
        *** Determines the total cost of the items in the cart
    def print_receipt:
        *** Prints out a list of the items using Pandas, along with the total cost

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
