import streamlit as st
from services.humidity import classify_humidity

st.title("💧 Humidity Monitoring")

humidity = st.slider("ความชื้น (%)", 0.0, 100.0, 50.0, 0.5)

status = classify_humidity(humidity)

st.metric("ความชื้นปัจจุบัน", f"{humidity:.1f} %")

status_display = {
    "NORMAL": st.success,
    "WARNING": st.warning,
    "CRITICAL": st.error,
}
status_display[status](f"สถานะ: {status}")

with st.expander("เกณฑ์การจำแนกสถานะ"):
    st.write("""
    - **NORMAL**: 40–60 %
    - **WARNING**: 30–70 % (ที่ไม่ใช่ NORMAL)
    - **CRITICAL**: น้อยกว่า 30 % หรือมากกว่า 70 %
    - ค่านอกช่วง 0–100 % จะเกิด error
    """)