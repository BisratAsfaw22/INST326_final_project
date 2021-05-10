import pytest
import grocery2 as g2

## The following test below are for Levis Forbang's section ##

@pytest.fixture
def IVClass():
    return g2.IventoryClass()

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
    
