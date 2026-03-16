from app import celcius_ke_fahrenheit, celcius_ke_kelvin

def test_perhitungan_suhu():
    # Test Celcius ke Fahrenheit
    assert celcius_ke_fahrenheit(0) == 32
    assert celcius_ke_fahrenheit(100) == 212
    # Test Celcius ke Kelvin
    assert celcius_ke_kelvin(0) == 2