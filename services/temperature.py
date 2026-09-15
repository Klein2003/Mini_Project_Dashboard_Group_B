def classify_temperature(celsius: float) -> str:
    """
    Contract:
    Input: อุณหภูมิ (°C) ต้องอยู่ในช่วง -20 ถึง 80
    Output: "NORMAL" | "WARNING" | "CRITICAL"
    Error: ถ้าค่านอกช่วง -20..80 -> ValueError
    """
    if not -20 <= celsius <= 80:
        raise ValueError("อุณหภูมิต้องอยู่ระหว่าง -20 ถึง 80 °C")

    if celsius <= 30:
        return "NORMAL"
    elif celsius <= 35:
        return "WARNING"
    else:
        return "CRITICAL"