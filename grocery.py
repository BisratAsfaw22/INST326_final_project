import csv
import re

class InventoryClass:
    """ This is the main class of the program having the following attributes:
    
    Attributes:
        inventory_dictionary (dictionary): values are list of tuples
        found (list): list of tuples
        not_found (list): list of tuples
        t_amount (float): Total amount
        t_qty (int): total quantity
    """
        
    
    def __init__(self):
        """ This method establish the following attributes of the class:
        
        Attributes:
            
            inventory_dictionary (dictionary): values are list of tuples
            found (list): list of tuples
            not_found (list): list of tuples
            t_amount (float): Total amount
            paid_by_customer(float): Total cost with tax
        """
        
        self.inventory_dictionary = dict()
        self.found = list()
        self.not_found = list()
        self.t_amount = 0.0
        self.t_qty = 0
        self.paid_by_customer = 0.0
        
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
            
        with open(file2, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split("\t")
                parts2 = parts[0], parts[1]
                if parts[0] in self.inventory_dictionary:
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
         
        for item in self.found:
            
            item_key = item[0]
            item_qty = int(item[1])
            self.t_qty += item_qty
            hj = self.inventory_dictionary.get(item_key)
            for q in hj:
                if q[0] == 'Price':
                    self.t_amount += float(q[1]) * float(item_qty)
        return f'Total cost: ${self.t_amount}, Total qty: {self.t_qty}' 

    def Totalpaid(self):
        """ It provides the total amount paid by the customer with tax.

        Side effects: 
            It update the total amount paid by the customer.
        """
        state_tax = 0.10

        state_tax = float(self.t_amount * state_tax)

        self.paid_by_customer = (self.t_amount + state_tax) 

    def veteran_discount(self):
        """ It provides the total amount paid by the customer with tax and after 
        the veteran discount if the customer qualify.

        Side effects: 
            It update the total amount paid by the customer by applying the veteran discount.
            prints total payment after veteran discount.
        """
        customer_input = input("Are you a veteran? YES or NO: ")

        vet_discount = float(input("How many years did you serve your country:\n"))

        total_payment = (self.t_amount*1.1) - vet_discount

        if customer_input == "YES":
            print("Total Paid By Customer after the Veteran Discount:" + str(total_payment))

        else:
            print("No veteran discount applied.")
            pass
    
    def suggest_price(self):
        """ Suggests items with similar prices.

        Side effects:
            Modifies the variables item_key, ej, item_key2, kj, tuple_pair, and
                suggestions
            Prints string statement with suggestions list containing item pairs with
                similar prices (within $1 range)
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
                            if b[0] == 'Price' and \
                            ((float(r[1]) - 1) <= float(b[1]) <= \
                            (float(r[1]) + 1)) and ((float(b[1]) - 1) <= \
                            float(r[1]) <= (float(b[1]) + 1)):
                                if item_key != item_key2:
                                    tuple_pair = item_key, item_key2
                                    suggestions.append(tuple_pair)
        print("Item pairs with similar prices: " + str(suggestions))
    
    def suggest_category(self):
        """ Suggests items of the same food categories.

        Side effects:
            Modifies the variables item_key3, wj, item_key4, uj, tuple_pair2, and
                suggestions2
            Prints string statement with suggestions list containing item pairs
                with the same food categories
        """
        suggestions2 = []
        for item3 in self.found:
            item_key3 = item3[0]
            wj = self.inventory_dictionary.get(item_key3)
            for t in wj:
                if t[0] == 'Food Category':            
                    for key2 in self.inventory_dictionary:
                        item_key4 = key2
                        uj = self.inventory_dictionary.get(item_key4)
                        for y in uj:
                            if y[0] == 'Food Category' and y[1] == t[1]:
                                if item_key3 != item_key4:
                                    tuple_pair2 = item_key3, item_key4
                                    suggestions2.append(tuple_pair2)
        print("Item pairs with the same food categories: " + str(suggestions2))

    def display(self):
        """Displays the output for the grocery simulator.
        
        Side effects: 
            Prints out the total items that are found/not found in the shopping list and store, along
            with the costs and quantites. 
        """
        
        i = self.not_found[0]
        prod = i[0]
        
        print ("Welcome to our grocery store simulator!")
        print ("Based on your shopping list, here is what we have gathered for you. ")
        print(f'Total number of item(s) in your list: {len(self.found)+len(self.not_found)}')
        print(f'Total item(s) on your list that are found in the store: {len(self.found)}')
        for i in self.found:
            q = i[1]
            c = 0.0
            p = i[0]
            j = self.inventory_dictionary.get(p)
            for x in j:
                if x[0] == "Price":
                    c += float(x[1])
            print(f'Name: {i}, Price: {c}, Quantity: {q}')
        print(f'Total number of item(s) not found in store: {len(self.not_found)}')
        for i in self.not_found:
            print(i[0])
        print(f'Total cost: ${self.t_amount}, Total qty: {self.t_qty}')
        print(f'Total including tax: ${self.paid_by_customer}')
        
    
    def review(self):
        """ Allows the user to leave a review and view those left by others.

        Side Effects:
            Modifies values of review, customer_reviews, and review_stored
            Modifies content of reviews.txt
            Prints reviews_stored
        """
        customer_reviews = []
        with open("reviews.txt","a", encoding="utf-8") as f:
            review = input("Please leave a review of this application:")
            customer_reviews.append(str(review))
            for n in range(len(customer_reviews)):
                f.write(str(customer_reviews[n]))
                f.write("\n")
        with open("reviews.txt","r", encoding="utf-8") as f:
            print("Thank you! These are the reviews that we have received so" + 
                  " far:")
            reviews_stored = f.read().splitlines()
            print (reviews_stored)
        
    def Search(self):
        """Allows user to serach/look for any additinal items not included in their shopping list.
        
        Side Effects:
            Print:
                (str):"Search for additional items:"
                      Gives out the name of the item and its price
                (str):"Item not found."
        """
        s = input("Search for any additional items: ")
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
        print(f'Please rate your general experience following the rating scale below.')
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
        


if __name__ == "__main__": 

    p = InventoryClass() 
    k = p.UpdateInventory('grocery_store.csv')
    n = p.UpdateLists('sample_items.txt') 
    ll = p.TotalCalc() 
    S = p.Totalpaid() 
    d = p.display()
    v = p.veteran_discount()
    pr = p.suggest_price()
    c = p.suggest_category()
    r = p.ratings() 
    re = p.review()
    a = p.Search() 
