import streamlit as st
import pandas as pd
import numpy as np
import time

# 1. إعدادات الصفحة والستايل
st.set_page_config(page_title="KADAD AI - Empire", layout="wide")

# التحقق من تشغيل النظام
if "system_active" not in st.session_state:
    st.session_state.system_active = False
if "db_workers" not in st.session_state:
    st.session_state.db_workers = []

# --- واجهة طلب الصلاحيات والربط ---
if not st.session_state.system_active:
    st.title("🛡️ تفعيل نظام كداد والربط الذكي")
    st.warning("النظام يتطلب صلاحيات الوصول لملفات التعريف لربط تطبيقات التوصيل بسيرفرات Google Cloud.")
    if st.button("✅ منح الصلاحيات وربط هنقرستيشن/جاهز (Blazing Speed)"):
        with st.spinner("جاري تهيئة الاتصال بالسيرفرات السحابية..."):
            time.sleep(2)
            st.session_state.system_active = True
            st.success("تم الربط بنجاح! جاري فتح لوحة التحكم...")
            time.sleep(1)
            st.rerun()
    st.stop()

# --- لوحة التحكم الرئيسية (بعد التفعيل) ---
st.title("🏎️ لوحة تحكم إمبراطورية كداد")

# صف العمال والخريطة
col_left, col_right = st.columns([1, 2])

with col_left:
    st.header("👥 إدارة الأسطول")
    with st.form("add_worker"):
        email = st.text_input("إيميل المندوب")
        password = st.text_input("كلمة المرور", type="password")
        submitted = st.form_submit_button("إضافة للنظام (Add Person)")
        if submitted and email:
            st.session_state.db_workers.append({"الإيميل": email, "الحالة": "نشط"})
            st.success(f"تم تسجيل {email}")

    if st.button("🗑️ تصفير النظام"):
        st.session_state.db_workers = []
        st.session_state.system_active = False
        st.rerun()

    # عرض الأهداف
    st.divider()
    st.metric("الميزانية المستهدفة للبيت", "4.5M - 6M SAR")
    st.info("الهدف: كراج يتسع لـ 10 سيارات فاخرة (مكلارين، روز رايز...)")

with col_right:
    st.header("📍 مراقبة المناديب (Live AI Map)")
    placeholder = st.empty()
    
    # محاكاة حركة المناديب (إذا فيه عمال مضافين)
    num_dots = len(st.session_state.db_workers) if st.session_state.db_workers else 1
    
    with placeholder.container():
        # توليد نقاط في الدمام
        points = np.random.randn(num_dots, 2) / [150, 150] + [26.4207, 50.0888]
        df = pd.DataFrame(points, columns=['lat', 'lon'])
        st.map(df)
        if num_dots > 0:
            st.write(f"يتم الآن تعقب {num_dots} مناديب بـ Blazing Speed...")

# جدول البيانات في الأسفل
if st.session_state.db_workers:
    st.subheader("📋 سجل الموظفين الحالي")
    st.table(pd.DataFrame(st.session_state.db_workers))
    import streamlit as st
import pandas as pd
import numpy as np
import time

# 1. إعدادات الإمبراطورية
st.set_page_config(page_title="KADAD AI - Real Location", layout="wide")

if "system_active" not in st.session_state:
    st.session_state.system_active = False
if "db_workers" not in st.session_state:
    st.session_state.db_workers = []

# --- واجهة الدخول بحساب قوقل والربط ---
if not st.session_state.system_active:
    st.title("🛡️ تسجيل الدخول وربط الموقع الحي")
    st.write("مرحباً بك في حي بدر، الدمام! 📍") # إشارة لموقعك الحالي
    st.info("النظام يحتاج ربط حسابك في قوقل لتحديد موقعك الحالي ومراقبة الأسطول بـ Blazing Speed.")
    
    if st.button("🔗 تسجيل الدخول بحساب Google ومنح صلاحية الموقع"):
        with st.spinner("جاري التحقق من الهوية وربط الـ GPS..."):
            time.sleep(2)
            st.session_state.system_active = True
            st.success("تم تسجيل الدخول! موقعك الآن مرتبط بالسيرفر.")
            st.rerun()
    st.stop()

# --- لوحة التحكم بعد الربط ---
st.title("🏎️ لوحة عمليات كداد - البث الحي")

col_left, col_right = st.columns([1, 2])

with col_left:
    st.header("👥 إضافة مندوب جديد")
    with st.form("add_worker"):
        email = st.text_input("إيميل المندوب (حساب قوقل)")
        password = st.text_input("كلمة المرور", type="password")
        submitted = st.form_submit_button("إضافة الشخص (Add Person)")
        if submitted and email:
            st.session_state.db_workers.append({"الإيميل": email, "الحالة": "متصل"})
            st.success(f"تمت إضافة {email} للأسطول!")

    st.divider()
    st.write("🏁 **الهدف الاستراتيجي:**")
    st.write("- منزل فخم (4.5M - 6M SAR)")
    st.write("- كراج السيارات الرياضية")
    if st.button("🗑️ خروج وتصفير"):
        st.session_state.db_workers = []
        st.session_state.system_active = False
        st.rerun()

with col_right:
    st.header("📍 موقعك الحالي ومواقع المناديب")
    
    # إحداثيات موقعك الفعلي (الدمام - حي بدر)
    my_lat, my_lon = 26.4192, 50.0261
    
    # توليد نقاط للمناديب حول موقعك
    num_workers = len(st.session_state.db_workers)
    worker_points = np.random.randn(num_workers if num_workers > 0 else 1, 2) / [100, 100] + [my_lat, my_lon]
    
    # دمج موقعك مع مواقع المناديب
    map_data = pd.DataFrame(worker_points, columns=['lat', 'lon'])
    
    st.map(map_data)
    st.write(f"مركز العمليات: حي بدر، الدمام. يتم تعقب {num_workers} مناديب حالياً.")

if st.session_state.db_workers:
    st.subheader("📋 قائمة الأسطول")
    st.table(pd.DataFrame(st.session_state.db_workers))
