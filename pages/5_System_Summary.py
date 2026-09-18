import streamlit as st

st.set_page_config(page_title="System Summary", page_icon="📋")

st.title("📋 System Summary")
st.markdown("---")

st.header("🎯 ภาพรวมของ Dashboard")
st.write("Engineering Monitoring Dashboard คือระบบจำลองการติดตามสถานะของระบบวิศวกรรม โดยแบ่งออกเป็น 4 โมดูลหลัก ดังนี้:")

st.markdown("""
- **Temperature Monitoring**: ตรวจสอบอุณหภูมิของระบบ (-20 ถึง 80 °C)
- **Humidity Monitoring**: ตรวจสอบความชื้นสัมพัทธ์ (0 ถึง 100 %)
- **Power Monitoring**: ตรวจสอบการใช้พลังงานไฟฟ้า (คำนวณจากแรงดันและกระแส)
- **Safety Alarm**: ระบบแจ้งเตือนความปลอดภัยรวมจากสถานะของทั้ง 3 โมดูลข้างต้น
""")

st.info("💡 **คำแนะนำ**: คุณสามารถเลือกทดสอบแต่ละโมดูลได้จากแถบเมนูด้านซ้ายมือ")

st.markdown("---")

st.header("📊 สรุปเกณฑ์สถานะ (NORMAL / WARNING / CRITICAL)")

st.markdown("""
| โมดูล | NORMAL (ปกติ) | WARNING (แจ้งเตือน) | CRITICAL (อันตราย) |
| :--- | :--- | :--- | :--- |
| **Temperature** | ≤ 30 °C | > 30 ถึง 35 °C | > 35 °C |
| **Humidity** | 40 – 60 % | 30 – 70 % (ที่ไม่ใช่ NORMAL) | < 30 % หรือ > 70 % |
| **Power** | < 500 W | 500 – 1000 W | > 1000 W |
| **Safety Alarm** | ไม่มีข้อความเตือน | แสดงข้อความเตือนของโมดูลนั้นๆ | แสดงข้อความเตือนของโมดูลนั้นๆ |
""")

st.markdown("---")

st.header("👥 สมาชิกและบทบาทในทีม")
st.markdown("""
* **คนที่ 1**: Temperature Monitoring (ดูแล Logic และ UI ของอุณหภูมิ)
* **คนที่ 2**: Humidity Monitoring (ดูแล Logic และ UI ของความชื้น)
* **คนที่ 3**: Power Monitoring (ดูแล Logic และ UI ของพลังงานไฟฟ้า)
* **คนที่ 4**: Safety Alarm (ดูแล Logic การแจ้งเตือนรวม และ UI แสดงผล) + Summary + QA + README (ดูแลภาพรวม, ตรวจสอบคุณภาพโค้ด และจัดทำเอกสาร)
""")