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
            
            Returns:
                The total items of the list that are found 
        """
        list_items = len(self.found) + len(self.not_found)
        print (f'Total item(s) in your list: {list_items}')

        items_found = len(self.found)
        return f'Total item(s) of your list found in the store: {items_found}'
    
    def suggest(self):
        """ Suggests items that have the same price.
        Side effects:
            Modifies the variables item_key, ej, item_key2, kj, tuple_pair, and suggestion
        Returns:
            String statement with suggestions list containing items with the same price.
        """
        suggestions = []
        for item2 in self.found:
            item_key = item2[0]
            ej = self.inventory_dictionary.get(item_key)
            for r in ej:
                if r[0] == 'Price':            
                    for key in self.inventory_dictionary:
                        item_key2 = key
                        kj = self.inventory_dictionary.get(item_key2)
                        for b in kj:
                            if b[0] == 'Price' and b[1] == r[1]:
                                if item_key != item_key2:
                                    tuple_pair = item_key, item_key2
                                    suggestions.append(tuple_pair)
        return f'These are items with the same prices: {suggestions}'
            
    

                    
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

if __name__ == "__main__": #statement and the proceeding information
    
    p = IventoryClass() # for testing
    k = p.UpdateInventory('inst326_project.csv') # for testing
    n = p.UpdateLists('sample_items.txt') # for testing
    ll = p.TotalCalc() # for testing
    t = p.Totalitem() # for testing
    z = p.suggest() # for testing
    print(t) # for testing
    print(ll) # for testing
    print (z) # for testing
