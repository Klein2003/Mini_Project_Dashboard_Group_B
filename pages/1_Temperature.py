import streamlit as st
from services.temperature import classify_temperature

st.title("🌡 Temperature Monitoring")

temp = st.slider("อุณหภูมิ (°C)", -20.0, 80.0, 28.0, 0.5)

status = classify_temperature(temp)

st.metric("อุณหภูมิปัจจุบัน", f"{temp:.1f} °C")

status_display = {
    "NORMAL": st.success,
    "WARNING": st.warning,
    "CRITICAL": st.error,
}
status_display[status](f"สถานะ: {status}")

with st.expander("เกณฑ์การจำแนกสถานะ"):
    st.write("""
    - **NORMAL**: ≤ 30 °C
    - **WARNING**: > 30 ถึง 35 °C
    - **CRITICAL**: > 35 °C
    - ค่านอกช่วง -20 ถึง 80 °C จะเกิด error
    """)