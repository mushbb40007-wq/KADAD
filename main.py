import streamlit as st
import pandas as pd
import numpy as np
import time

# إعدادات الصفحة
st.set_page_config(page_title="KADAD AI - Live", layout="wide")

st.title("🚀 نظام كداد - مراقبة حية بـ AI")

# --- لوحة التحكم الجانبية ---
st.sidebar.header("التحكم في الأسطول")
delivery_count = st.sidebar.slider("عدد المناديب النشطين", 1, 10, 3)
speed = st.sidebar.select_slider("سرعة التحديث", options=["هادئ", "سريع", "Blazing Speed"])

# --- عدادات الأرباح ---
col1, col2 = st.columns(2)
col1.metric("الطلبات النشطة الآن", delivery_count)
col2.metric("هدف اليوم", "5,000 SAR")

# --- الخريطة المتحركة ---
st.subheader("📍 مواقع المناديب في الدمام (Live)")
placeholder = st.empty() # مكان محجوز للتحديث

# حلقة التحديث التلقائي
for i in range(100):
    with placeholder.container():
        # توليد نقاط عشوائية حول الدمام تتحرك بسيط كل مرة
        random_points = np.random.randn(delivery_count, 2) / [150, 150] + [26.4207, 50.0888]
        df = pd.DataFrame(random_points, columns=['lat', 'lon'])
        
        st.map(df)
        
        # سرعة التحديث بناءً على اختيارك
        if speed == "Blazing Speed":
            time.sleep(1)
        else:
            time.sleep(3)
