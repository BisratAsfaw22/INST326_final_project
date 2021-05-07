import pytest
import grocery2 as g2


@fixture
def IVClass():
    return g2.IventoryClass()

def test_IVClass(IVClass):
    
    assert IVClass.inventory_dictionary == dict()
    
    

def test_updateinventory(IVClass):
    
    IVClass.UpdateInventory("inst326_project.csv")
    
    
    