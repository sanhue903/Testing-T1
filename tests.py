import pytest
import ohce_kata as ok
from datetime import time

def test_reverse():
    assert ok.ohce("hola") == "aloh"
    assert ok.ohce("oto") == "oto"
    assert ok.ohce("sebas") == "sabes"
    assert ok.ohce("chao") == "oahc"

def test_is_polindrome():
    string = "¡Bonita palabra!"
    assert ok.palindrome("oto", ok.ohce("oto")) == string
    assert ok.palindrome("ana", ok.ohce("ana")) == string
    assert ok.palindrome("reconocer", ok.ohce("reconocer")) == string
    assert ok.palindrome("oro", ok.ohce("oro")) == string
    
def test_is_not_polindrome():
    assert ok.palindrome("sebas", ok.ohce("sebas")) == None
    assert ok.palindrome("hola", ok.ohce("hola")) == None
    assert ok.palindrome("chao", ok.ohce("chao")) == None
    assert ok.palindrome("python", ok.ohce("python")) == None
    
def test_salute():
    name = "Seba"
    assert ok.salute(name, time(9,20)) == f"Buenos días {name}!"
    assert ok.salute(name, time(11,59)) == f"Buenos días {name}!"
    assert ok.salute(name, time(6,0)) == f"Buenos días {name}!"
    
def test_salute_afternoon():
    name = "Seba"
    assert ok.salute(name, time(12,0)) == f"Buenas tardes {name}!"
    assert ok.salute(name, time(19,59)) == f"Buenas tardes {name}!"
    assert ok.salute(name, time(16,0)) == f"Buenas tardes {name}!"
    
    
