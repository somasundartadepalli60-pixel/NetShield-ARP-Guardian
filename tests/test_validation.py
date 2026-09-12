import pytest
from app.core.validation import normalize_mac, validate_ip

def test_mac_normalization():
    assert normalize_mac("AA-BB-CC-DD-EE-FF")=="aa:bb:cc:dd:ee:ff"

@pytest.mark.parametrize("value",["not-an-ip","999.999.1.1",""])
def test_invalid_ip(value):
    with pytest.raises(ValueError): validate_ip(value)
