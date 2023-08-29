import pytest
import ohce_kata as ok

def test_reverse():
    assert ok.ohce("hola") == "aloh"
    assert ok.ohce("oto") == "oto"
    assert ok.ohce("sebas") == "sabes"
    assert ok.ohce("chao") == "oahc"

def test_is_polindrome():
    string = "!Bonita palabra!"
    assert ok.palindrome("oto", ok.ohce("oto")) == string
    assert ok.palindrome("ana", ok.ohce("ana")) == string
    assert ok.palindrome("reconocer", ok.ohce("reconocer")) == string
    assert ok.palindrome("oro", ok.ohce("oro")) == string
    
def test_is_not_polindrome():
    assert ok.palindrome("sebas", ok.ohce("sebas")) == None
    assert ok.palindrome("hola", ok.ohce("hola")) == None
    assert ok.palindrome("chao", ok.ohce("chao")) == None
    assert ok.palindrome("python", ok.ohce("python")) == None
    
    
