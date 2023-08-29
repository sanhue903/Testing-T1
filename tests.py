import pytest
import ohce_kata as ok

def test_reverse():
    assert ok.ohce("hola") == "aloh"
    assert ok.ohce("oto") == "oto"
    assert ok.ohce("sebas") == "sabes"
    assert ok.ohce("chao") == "oahc"

def test_is_polindrome():
    string = "!Bonita palabra!"
    assert ok.palindrome("oto") == string
    assert ok.palindrome("ana") == string
    assert ok.palindrome("reconocer") == string
    assert ok.palindrome("oro") == string
    
    