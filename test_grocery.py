import pytest
import grocery as g
import builtins
from unittest import mock

## The following test below are for Levis Forbang's section ##

@pytest.fixture
def IVClass():
    return g.InventoryClass()

def test_IVClass(IVClass):
    
    assert IVClass.inventory_dictionary == dict()
    

def test_updateinventory(IVClass):
    
    IVClass.UpdateInventory("grocery_store.csv")
    
    assert len(IVClass.inventory_dictionary) == 11
    
    assert "Eggland's Best Eggs, Large - 12 eggs, 24 oz" in IVClass.inventory_dictionary
    
def test_updatelist(IVClass):
    
    IVClass.UpdateInventory("grocery_store.csv")
    
    IVClass.UpdateLists("sample_items.txt")
    
    assert len(IVClass.found) == 2

## The following test below are for Bisrat Asfaw's section ##
def test_search(IVClass):
    "Does search() print the name of the item and price?"
    with mock.patch("builtins.input", side_effect = [('Calue Corner Whole Milk , 1 Gallon, 4.99')]):
        assert builtins.input() == 'Calue Corner Whole Milk , 1 Gallon, 4.99'

## The following test below are for Anani Adjanor's section ##
# def test_veteran_discount(IVClass):
#     "Does Totalpaid() correctly return the total amount paid by the customer?"
#     with mock.patch("builtins.input", side_effect = ['YES', '10']):
#         assert builtins.input() == 18.094
     
## The following test below are for Tyler Perlstein's section ##
def test_review(IVClass):
    """Does the review() method of the Inventory Class properly write out the 
        user review input to the reviews.txt file?"""
    with mock.patch("builtins.input", side_effect=["Well designed!"]):
        IVClass.review()
        with open('reviews.txt') as f:
            lines = f.readlines()
            assert "Well designed!\n" in lines


