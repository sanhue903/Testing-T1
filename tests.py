import pytest
import ohce_kata as ok

def test_reverse():
    assert ok.ohce("hola") == "aloh"
    assert ok.ohce("oto") == "oto"
    assert ok.ohce("sebas") == "sabes"
    assert ok.ohce("chao") == "oahc"

    