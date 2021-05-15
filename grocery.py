import csv
import re

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

    def Totalpaid(self):
        """ It provides the total amount paid by the customer with tax and after 
        deducting the customer coupon discount.
        Side effects: 
            It update the total amount paid by the customer.
        Returns: 
            Amount paid.
        """
        state_tax = 0.10
        discount_coupon = 0.02

        discount_coupon = float(self.t_amount*discount_coupon)
        state_tax = float(self.t_amount * state_tax)

        paid_by_customer = (self.t_amount + state_tax) - discount_coupon
        return f'Total Paid By Customer with tax: ${paid_by_customer}'
        
    def Totalitem(self):
        """It gives the total items on the users list and the total items that were found.
        
            Returns:
                Number of total items in the list, number of items found and the name of
                the item not found.
        """
        i = self.not_found
        item = i[0]
        prod = item[0]
        list_items = len(self.found) + len(self.not_found)
        items_found = len(self.found)
        return f'Total number of item(s) in your list: {list_items} \nTotal item(s) of your list found in the store: {items_found} \nItems in your list that are not found in the store : {prod}'

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
        
    def Search(self):
        """Allows user to serach/look for any additinal items not included in their shopping list.
        
            Side Effects:
                    Print:
                        (str):"Search for additional items:"
                              Gives out the name of the item and its price
                        (str):"Item not found."
        
        """
        s = input("Search for additional items: ")
        s= str(s.lower())
        dic = self.inventory_dictionary
        
        for item in dic:
            i1 = self.inventory_dictionary.get(item)
            i2 = i1[2]
            if s in item.lower():
                print(f'{item}, Price: ${i2[1]}')
                break
        else: 
            print("Item not found")
                

    def ratings(self):
        """Allows the user to rate his/her overall experience: enter a number based on the given
           rating scale, if input invalid then it asks the user to insert rating again or exit .

           Side Effects: 
                    Prints:
                        (str):"Please rate your general experience with us following the rating scale below."
                              "Insert rating: "
                        (str):"Thank you for your feedback!"
                              "Input should be an integer less than 6, please Insert again:"
        """
        rating_scale = ["1","2","3","4","5"]
        print(f'Please rate your general experience with us following the rating scale below.')
        print(f'{rating_scale[0]} = Unsuccessful\n{rating_scale[1]} = Not bad\n{rating_scale[2]} = Okay\n{rating_scale[3]} = Very good\n{rating_scale[4]} = Successful')
        rate = input('Insert rating:')
        
        if rate in rating_scale:
            print('Thank you for your feedback!')  
        else:
            rate = input('Input should be an integer less than 6, please Insert again:')
            if rate in rating_scale:
                print('Thank you for your feedback!')
            else:
                print("Exit")
        

if __name__ == "__main__": #statement and the proceeding information
    p = IventoryClass() # for testing
    k = p.UpdateInventory('inst326_project.csv') # for testing
    n = p.UpdateLists('sample_items.txt') # for testing
    t = p.Totalitem() # for testing
    ll = p.TotalCalc() # for testing
    S = p.Totalpaid() # for testing
    z = p.suggest() # for testing
    r = p.ratings()
    a = p.Search()
    print(t) # for testing
    print(ll) # for testing
    print(S)
    print(z)
    print(r)
    print(a)
