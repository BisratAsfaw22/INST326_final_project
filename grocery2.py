###### Levis Forbang's section: "import csv" to "def TotalCalc(self):"

import csv

class IventoryClass:
    
    def __init__(self, inventory_dictionary=dict(), found=list(), not_found=list(), t_amount=0.0):
        
        self.inventory_dictionary = inventory_dictionary
        self.found = found 
        self.not_found = not_found
        self.t_amount = t_amount
        
    
    def UpdateInventory(self, file1):
        
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
        
        print(f'The following are the item(s) on your list that was found.') # For testing
        for item in self.found:
            
            item_key = item[0]
            item_qty = item[1]
            hj = self.inventory_dictionary.get(item_key)
            print(f'Item name: {item_key}') # for testing
            print(f'Informatin about the item: {hj}') # for testing
            for q in hj:
                if q[0] == 'Price':
                    self.t_amount += float(q[1]) * float(item_qty)
        return f'Total cost without taxt: ${self.t_amount}' # "Total cost without taxt: $" will be removed
    
## Replace this comment with a Method that display the following information.

        #   Total item(s) on your list: 3
        #   Total item(s) found: 2
                # Display the names(key) of the item(s) and the values next to them
                    # This shoud be in a constructive sentence.
                    
## Replace this comment with a method that display the following information
        #   Total items(s) not fund: 1
                # Display the names(key) of the item(s)
                    # This should be in a constructive sentence
        #   Total coast including inclusding tax:
                # This should be in a constructive sentence
        

## Replace this comment with a method that displace the following information

        # Display items that are on sale based on items note found
            # It can be item(s) on sale that share similar term in name
            
            
## Replace This comment with folliwng information 

        # an if __name__ == "__main__": statement and the proceeding information
    
p = IventoryClass() # for testing
k = p.UpdateInventory('inst326_project.csv') # for testing
n = p.UpdateLists('sample_items.txt') # for testing
ll = p.TotalCalc() # for testing
print(ll) # for testing
