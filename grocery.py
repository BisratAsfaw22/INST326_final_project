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
        
    def Totalitem(self):
        """It gives the total items on the users list and the total items that were found.
        
            
            Side effects:
                Prints to the console  
            
            Returns:
                The total items of the list that are found 
        """
        i = self.not_found
        item = i[0]
        prod = item[0]
        list_items = len(self.found) + len(self.not_found)
        items_found = len(self.found)
        return f'Total number of item(s) in your list: {list_items} \nTotal item(s) of your list found in the store: {items_found} \nItems in your list that are not found in the store : {prod}'
        
    def Search(self):
        """   """
        s = input("Search for additional items: ")
        s= str(s)
        dic = self.inventory_dictionary
        
        for item in dic:
            i1 = self.inventory_dictionary.get(item)
            i2 = i1[2]
            if s in item:
                print(f'{item}, Price: ${i2[1]}')
                break
        else: 
            print("Item not found")
                

    def ratings(self):
        """   """
        ratingScale = [1,2,3,4,5]
        print(f'Please rate your general experience with us following the rating scale below.')
        print(f'{ratingScale[0]} = Unsuccessful \n{ratingScale[1]} = Not bad \n{ratingScale[2]} = Okay \n{ratingScale[3]} = Very good \n{ratingScale[4]} = Successful')
        rate = input('Insert rating: ')
        ra = int(rate)
        
        if ra in ratingScale:
            print('Thank you for your feedback!')  
        elif y not in ratingScale:
            raise KeyError("The input should be a number")
        else:
            i = input('Insert rating again: ')
            i = int(i)
            if i in ratingScale:
                print('Thank you for your feedback!')
            else:
                print("Exit")
        


# Add a method that suggests a nearby store for items not found maybe using a dictionary.
# add a delivery date for items not found
#calculate distance



                
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
r = p.ratings()
s = p.Search()
print(t) # for testing
#print(ll) # for testing
#print(s)
#print(r)
