def classify_humidity(percent: float) -> str:
    """
    Contract:
    Input: ความชื้น (%) ต้องอยู่ในช่วง 0 ถึง 100
    Output: "NORMAL" | "WARNING" | "CRITICAL"
    Error: ถ้าค่านอกช่วง 0..100 -> ValueError

    เกณฑ์:
    - 40-60%      -> NORMAL
    - 30-70% ที่ไม่ใช่ NORMAL -> WARNING
    - < 30% หรือ > 70%       -> CRITICAL
    """
    if not 0 <= percent <= 100:
        raise ValueError("ความชื้นต้องอยู่ระหว่าง 0 ถึง 100 %")

    if 40 <= percent <= 60:
        return "NORMAL"
    elif 30 <= percent <= 70:
        return "WARNING"
    else:
        return "CRITICAL"