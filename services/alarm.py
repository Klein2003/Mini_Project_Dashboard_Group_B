from services.temperature import classify_temperature

def generate_alarms(
    temp_status: str,
    humid_status: str,
    power_status: str
) -> list[str]:
    """คืน list ข้อความเตือน; ถ้าปกติทั้งหมดคืน []"""
    valid_statuses = {"NORMAL", "WARNING", "CRITICAL"}
    
    if temp_status not in valid_statuses or humid_status not in valid_statuses or power_status not in valid_statuses:
        raise ValueError("Invalid status. Only 'NORMAL', 'WARNING', or 'CRITICAL' are allowed.")
        
    alarms = []
    
    # Check Temperature
    if temp_status == "WARNING":
        alarms.append("WARNING: Temperature requires attention")
    elif temp_status == "CRITICAL":
        alarms.append("CRITICAL: Temperature is unsafe")
        
    # Check Humidity
    if humid_status == "WARNING":
        alarms.append("WARNING: Humidity requires attention")
    elif humid_status == "CRITICAL":
        alarms.append("CRITICAL: Humidity is unsafe")
        
    # Check Power
    if power_status == "WARNING":
        alarms.append("WARNING: Power consumption is high")
    elif power_status == "CRITICAL":
        alarms.append("CRITICAL: Power consumption is unsafe")
        
    return alarms