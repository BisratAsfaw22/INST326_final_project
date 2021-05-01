<<<<<<< HEAD

import csv

class IventoryClass:
    """ This is the main class of the program having the following attributes:
    
    Attributes:
        inventory_dictionary (dictionary): values are list of tuples
        found (list): list of tuples
        not_found (list): list of tuples
        t_amount (float): Total amount
        t_qty (int): total quantity
    """
        
    
    def __init__(self, inventory_dictionary=dict(), found=list(), not_found=list(), t_amount=0.0, t_qty=0):
        """ This method establish the following attributes of the class:
        
        Attributes:
            
            inventory_dictionary (dictionary): values are list of tuples
            found (list): list of tuples
            not_found (list): list of tuples
            t_amount (float): Total amount
        """
        
        self.inventory_dictionary = inventory_dictionary
        self.found = found 
        self.not_found = not_found
        self.t_amount = t_amount
        self.t_qty = t_qty
        
    
    def UpdateInventory(self, file1):
        """ This method reads and updates the inventory_dictionary attribute
        with data from the csv file. 
        
        Args:
            file1 (str): csv
        
        Side effects:
            update the inventory_dictionary attribute
        """
        
        t = open(file1, 'r')
        reader = csv.reader(t)
        
        for row in reader:
            self.inventory_dictionary.update(
                                                {row[0]:[('Food Category', row[1]), 
                                                         ('Aisle Number', row[2]), 
                                                         ('Price', row[3]), 
                                                         ('On Sale', row[4]), 
                                                         ('QTY On Shelf', row[5]), 
                                                         ('In Stock', row[6])
                                                        ]
                                                 }
                                            )
     
    def UpdateLists(self, file2):
        """ This method reads a text file and updates
        "found" and "not_found" attributes accordingly
        
        Args:
            file2 (str): text file
        
        Side effects:
            Update "found" and "not_found" attributes
        """
            
        #print(self.inventory_dictionary)
        with open(file2, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split("\t")
                parts2 = parts[0], parts[1]
                #print(parts2)
                if parts[0] in self.inventory_dictionary:
                    ##print(parts2)
                    self.found.append(parts2)
                else:
                    self.not_found.append(parts2)
        
        
    def TotalCalc(self):
        """ This method updates the t_amount attribute accordingly.
        
        Side effects:
            Update the t_amount attribute
            update the t_qty attribute
        
        Returns:
            Returns the t_amount and t_qty attributes as tuples 
        """
        
        print(f'The following are the item(s) on your list that was found.') # For testing
        for item in self.found:
            
            item_key = item[0]
            item_qty = int(item[1])
            self.t_qty += item_qty
            hj = self.inventory_dictionary.get(item_key)
            print(f'Item name: {item_key}') # for testing
            print(f'Informatin about the item: {hj}') # for testing
            for q in hj:
                if q[0] == 'Price':
                    self.t_amount += float(q[1]) * float(item_qty)
        return f'Total cost: ${self.t_amount}, Total qty: {self.t_qty}' # "Total cost: $" & Total qty:" will be removed
        
    def Totalitem(self):
        """It gives the total items on the users list and the total items that were found.
        
            
            Side effects:
                Prints to the console  
        """
        list_file = open('sample_items.txt', "r")
        count = 0
        list1 = list_file.read()
        shopping_list = list1.split("\n")
        for i in shopping_list:
            if i:
                count += 1
        print (f'Total item(s) on your list: {count}')
        i in self.found
        return f'Total item(s) of your list found in the store: {count-1}'
                    
## Replace this comment with method(s) that display the following information
        #   Total items(s) not fund: 1
                # Display the names(key) of the item(s)
                    # This should be in a constructive sentence
        #   Total coast including inclusding tax:
                # This should be in a constructive sentence
        

## Replace this comment with a method(s) that displace the following information

        # Display items that are on sale based on items note found
            # It can be item(s) on sale that share similar key term in name (eg. eggs)
            
            
## Replace This comment with folliwng information 

        # an if __name__ == "__main__": statement and the proceeding information
    
p = IventoryClass() # for testing
k = p.UpdateInventory('inst326_project.csv') # for testing
n = p.UpdateLists('sample_items.txt') # for testing
ll = p.TotalCalc() # for testing
t = p.Totalitem() # for testing
print(t) # for testing
print(ll) # for testing
=======
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
>>>>>>> 0d040835a93ada92b0167db9ee5a2664007cf916
