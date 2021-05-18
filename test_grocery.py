import pytest
import grocery as g
import builtins
from unittest import mock

## The following test below are for Levis Forbang's section ##

@pytest.fixture
def IVClass():
    return g.IventoryClass()

def test_IVClass(IVClass):
    
    assert IVClass.inventory_dictionary == dict()
    
    

def test_updateinventory(IVClass):
    
    IVClass.UpdateInventory("inst326_project.csv")
    
    assert len(IVClass.inventory_dictionary) == 11
    
    assert "Eggland's Best Eggs, Large - 12 eggs, 24 oz" in IVClass.inventory_dictionary
    
def test_updatelist(IVClass):
    
    IVClass.UpdateInventory("inst326_project.csv")
    
    IVClass.UpdateLists("sample_items.txt")
    
    assert len(IVClass.found) == 2

def test_Totalitem(IVClass):
    "Does Totalitem() correctly calculate the total items in the list & the total items found."
    assert sum([len(IVClass.found), len(IVClass.not_found)]) == 3
    assert len(IVClass.found) == 2
    assert IVClass.not_found == [('Oscar Mayer Hardwood Smoked Bacon - 16oz', '3')]

def test_Totalitem(capsys):
     "Does Totalitem() give out the correct output?"
     print("Total number of item(s) in your list: 3 \n"
            "Total item(s) of your list found in the store: 2 \n"
            "Items in your list that are not found in the store : Oscar Mayer Hardwood Smoked Bacon - 16oz")
     outerr = capsys.readouterr()
     out = outerr.out
     assert out == ("Total number of item(s) in your list: 3 \n"
                    "Total item(s) of your list found in the store: 2 \n"
                    "Items in your list that are not found in the store : Oscar Mayer Hardwood Smoked Bacon - 16oz\n")

def test_search(IVClass):
    "Does search() print the name of the item and price?"
    with mock.patch("builtins.input", side_effect = [('Calue Corner Whole Milk , 1 Gallon, 4.99')]):
        assert builtins.input() == 'Calue Corner Whole Milk , 1 Gallon, 4.99'
        
def test_review(IVClass):
    """Does the review() method of the Inventory Class properly write out the 
        user review input to the reviews.txt file?"""
    with mock.patch("builtins.input", side_effect=["Well designed!"]):
        IVClass.review()
        with open('reviews.txt') as f:
            lines = f.readlines()
            assert "Well designed!\n" in lines

