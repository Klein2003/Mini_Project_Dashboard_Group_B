import pytest
from services.humidity import classify_humidity


def test_normal():
    assert classify_humidity(50) == "NORMAL"


def test_normal_boundary_low():
    assert classify_humidity(40) == "NORMAL"


def test_normal_boundary_high():
    assert classify_humidity(60) == "NORMAL"


def test_warning_low_side():
    assert classify_humidity(35) == "WARNING"


def test_warning_high_side():
    assert classify_humidity(65) == "WARNING"


def test_warning_boundary():
    assert classify_humidity(30) == "WARNING"
    assert classify_humidity(70) == "WARNING"


def test_critical_low():
    assert classify_humidity(20) == "CRITICAL"


def test_critical_high():
    assert classify_humidity(80) == "CRITICAL"


def test_invalid_too_high():
    with pytest.raises(ValueError):
        classify_humidity(150)


def test_invalid_too_low():
    with pytest.raises(ValueError):
        classify_humidity(-10)