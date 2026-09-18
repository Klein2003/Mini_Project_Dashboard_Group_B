import streamlit as st
from services.power import calculate_power, classify_power

st.title("Power Monitoring Dashboard")
st.subheader("ระบบจำลองการคำนวณและติดตามกำลังไฟฟ้า")

col_input1, col_input2 = st.columns(2)

with col_input1:
    voltage = st.slider("แรงดันไฟฟ้า (Voltage: V)", 0.1, 400.0, 220.0, 1.0)
with col_input2:
    current = st.slider("กระแสไฟฟ้า (Current: I)", 0.0, 10.0, 2.5, 0.1)

try:
    power_watt = calculate_power(voltage, current)
    status = classify_power(power_watt)

    st.markdown("---")
    
    col_metric1, col_metric2, col_metric3 = st.columns(3)
    col_metric1.metric("Voltage", f"{voltage:.1f} V")
    col_metric2.metric("Current", f"{current:.1f} A")
    col_metric3.metric("Power Output", f"{power_watt:.1f} W")

    status_ui = {
        "NORMAL": st.success,
        "WARNING": st.warning,
        "CRITICAL": st.error
    }
    
    status_ui[status](f"🚨 สถานะกำลังไฟฟ้าในปัจจุบัน: **{status}**")

except ValueError as e:
    st.error(f"เกิดข้อผิดพลาดจากข้อมูลนำเข้า: {e}")
