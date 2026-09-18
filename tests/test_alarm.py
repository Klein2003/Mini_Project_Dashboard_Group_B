import pytest
from services.alarm import generate_alarms

def test_all_normal():
    # 1. ทุกโมดูลเป็น NORMAL และต้องได้ []
    assert generate_alarms("NORMAL", "NORMAL", "NORMAL") == []

def test_one_warning():
    # 2. มี 1 โมดูลเป็น WARNING
    assert generate_alarms("WARNING", "NORMAL", "NORMAL") == ["WARNING: Temperature requires attention"]
    assert generate_alarms("NORMAL", "WARNING", "NORMAL") == ["WARNING: Humidity requires attention"]
    assert generate_alarms("NORMAL", "NORMAL", "WARNING") == ["WARNING: Power consumption is high"]

def test_warning_and_critical():
    # 3. มี WARNING และ CRITICAL พร้อมกัน
    alarms = generate_alarms("NORMAL", "CRITICAL", "WARNING")
    assert alarms == [
        "CRITICAL: Humidity is unsafe",
        "WARNING: Power consumption is high"
    ]

def test_all_critical():
    # 4. ทุกโมดูลเป็น CRITICAL
    alarms = generate_alarms("CRITICAL", "CRITICAL", "CRITICAL")
    assert alarms == [
        "CRITICAL: Temperature is unsafe",
        "CRITICAL: Humidity is unsafe",
        "CRITICAL: Power consumption is unsafe"
    ]

def test_invalid_input():
    # 5. มี Input ที่ไม่ใช่ NORMAL, WARNING หรือ CRITICAL และต้องเกิด ValueError
    with pytest.raises(ValueError):
        generate_alarms("OK", "NORMAL", "NORMAL")
        
    with pytest.raises(ValueError):
        generate_alarms("NORMAL", "ERROR", "NORMAL")
        
    with pytest.raises(ValueError):
        generate_alarms("NORMAL", "NORMAL", "BAD")