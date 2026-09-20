import streamlit as st
import pandas as pd

def main():
    # ตั้งค่าหน้า Page
    st.set_page_config(page_title="System Summary", page_icon="📊", layout="wide")

    st.title("📊 สรุปภาพรวมของระบบ (System Summary)")
    st.info("👈 **คำแนะนำ:** คุณสามารถเปิดหน้าแต่ละโมดูลเพื่อดูรายละเอียดและการทำงานได้จากเมนูด้านซ้ายมือ")
    
    st.divider()

    # 1. คำอธิบายว่า Dashboard มีโมดูลใดบ้าง
    st.header("📌 โมดูลภายใน Dashboard")
    st.markdown("""
    ระบบ Monitoring Dashboard ของกลุ่ม B ประกอบไปด้วย 4 โมดูลหลัก ดังนี้:
    1. **🌡 Temperature Monitoring:** ระบบติดตามอุณหภูมิ
    2. **💧 Humidity Monitoring:** ระบบติดตามความชื้น
    3. **⚡ Power Monitoring:** ระบบจำลองการคำนวณและติดตามกำลังไฟฟ้า
    4. **🚨 Safety Alarm:** ระบบตรวจสอบและแจ้งเตือนสถานะความปลอดภัยรวมของทุกระบบ
    """)

    # 2. สรุปเกณฑ์ NORMAL / WARNING / CRITICAL
    st.header("🚦 สรุปเกณฑ์การจำแนกสถานะ (Thresholds)")
    
    # สรุปเกณฑ์ตาม Contract จริงของแต่ละไฟล์
    threshold_data = {
        "ระบบ (Module)": ["Temperature (°C)", "Humidity (%)", "Power (W)"],
        "🟢 NORMAL": ["≤ 30", "40 – 60", "< 500"],
        "🟡 WARNING": ["> 30 ถึง 35", "30 – 39 หรือ 61 – 70", "500 – 1000"],
        "🔴 CRITICAL": ["> 35", "< 30 หรือ > 70", "> 1000"]
    }
    st.table(pd.DataFrame(threshold_data))

    st.divider()

    col1, col2 = st.columns(2)
    # 3. รายชื่อสมาชิกและบทบาท
    with col1:
        st.header("👥 รายชื่อสมาชิกและบทบาทในทีม")
        st.markdown("""
        - **สมาชิกคนที่ 1 (นายรพีพงศ์ ลิ้มชวพันธนกุล):** ผู้รับผิดชอบ Module Temperature
        - **สมาชิกคนที่ 2 (นายเมฆา สีม่วงคำ):** ผู้รับผิดชอบ Module Humidity
        - **สมาชิกคนที่ 3 (นายวุฒิไกร ร่มพนาธรรม):** ผู้รับผิดชอบ Module Power
        - **สมาชิกคนที่ 4 (นายรชต ปานงาม):** ผู้รับผิดชอบ Module Safety Alarm
        - **สมาชิกคนที่ 5 (นายณัฐนันท์ เชาว์เกษตร):** จัดทำหน้า System Summary และหน้าที่ QA
        """)

    # 4. หน้าที่ QA
    with col2:
        st.header("✅ หน้าที่และมาตรฐานการตรวจสอบคุณภาพ (QA)")
        st.markdown("""
        ในฐานะ QA ของทีม มีหน้าที่รับผิดชอบตรวจสอบความถูกต้องก่อนรวมโค้ด ดังนี้:
        1. 🧪 **ตรวจ Unit Test:** ตรวจสอบ Pull Request (PR) ของเพื่อนว่ามี Unit Test รองรับฟังก์ชันใหม่
        2. 🤝 **ตรวจ Contract:** ตรวจสอบโค้ดว่าตรงกับงานและเงื่อนไขที่ตกลงกันไว้
        3. 🚀 **ตรวจสถานะโค้ด:** รันคำสั่ง `pytest -q` ต้องผ่านทั้งหมด 100% ก่อนกดอนุมัติ PR
        4. 📖 **ตรวจ Documentation:** ช่วยดูไฟล์ `README.md` ให้มีวิธีติดตั้งและวิธีรันโปรเจกต์ที่ชัดเจน
        """)

if __name__ == "__main__":
    main()