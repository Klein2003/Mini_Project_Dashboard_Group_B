import streamlit as st
from services.alarm import generate_alarms

st.title("🚨 Safety Alarm")

st.write("จำลองการเลือกสถานะของแต่ละระบบ เพื่อตรวจสอบการทำงานของ Safety Alarm")

options = ["NORMAL", "WARNING", "CRITICAL"]

col1, col2, col3 = st.columns(3)

with col1:
    temp_status = st.selectbox("Temperature", options)
    
with col2:
    humid_status = st.selectbox("Humidity", options)
    
with col3:
    power_status = st.selectbox("Power", options)

st.markdown("---")
st.subheader("ผลลัพธ์จาก Safety Alarm")

try:
    alarms = generate_alarms(temp_status, humid_status, power_status)
    
    if not alarms:
        st.success("✅ ระบบทั้งหมดอยู่ในสภาวะปกติ (NORMAL)")
    else:
        st.error(f"⚠️ พบการแจ้งเตือนทั้งหมด {len(alarms)} รายการ")
        for alarm in alarms:
            if alarm.startswith("CRITICAL"):
                st.error(alarm)
            else:
                st.warning(alarm)
                
except ValueError as e:
    st.error(f"เกิดข้อผิดพลาด: {e}")