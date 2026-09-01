import streamlit as st

# পেজ কনফিগারেশন
st.set_page_config(page_title="বিজ্ঞান একাডেমি", page_icon="🔬", layout="wide")

st.title("🔬 বিজ্ঞান একাডেমি (Science Academy)")
st.write("নবম-দশম এবং একাদশ-দ্বাদশ শ্রেণীর পদার্থবিজ্ঞান ও রসায়ন শেখার ডিজিটাল প্ল্যাটফর্ম।")

# সাইডবার নেভিগেশন (শ্রেণী এবং বিষয় সিলেকশন)
st.sidebar.header("🎯 ফিল্টার করুন")
selected_class = st.sidebar.selectbox("আপনার শ্রেণী বেছে নিন:", ["নবম-দশম (Class 9-10)", "একাদশ-দ্বাদশ (Class 11-12)"])
selected_subject = st.sidebar.radio("বিষয় বেছে নিন:", ["পদার্থবিজ্ঞান (Physics)", "রসায়ন (Chemistry)"])

# ট্যাব বিভাজন
tab1, tab2 = st.tabs(["📚 লেকচার নোট ও গাণিতিক সমাধান", "🧠 কুইজ টেস্ট"])

# ==============================================================================
# ১. নবম-দশম শ্রেণী (Class 9-10)
# ==============================================================================
if selected_class == "নবম-দশম (Class 9-10)":
    
    if selected_subject == "পদার্থবিজ্ঞান (Physics)":
        with tab1:
            st.header("⚡ অধ্যায়: গতি (Motion)")
            st.markdown("### **গুরুত্বপূর্ণ সূত্রাবলী:**")
            st.latex(r"v = u + at")
            st.latex(r"s = \frac{u+v}{2} \times t")
            
            # গাণিতিক সমাধান টুল
            st.subheader("🧮 গাণিতিক সমস্যার সমাধানকারী (Calculator)")
            st.write("আদিবেগ ($u$), ত্বরণ ($a$) এবং সময় ($t$) দিয়ে শেষ বেগ ($v$) বের করো:")
            
            u = st.number_input("আদিবেগ (u in m/s):", value=0.0)
            a = st.number_input("ত্বরণ (a in m/s²):", value=2.0)
            t = st.number_input("সময় (t in seconds):", value=5.0)
            
            if st.button("শেষ বেগ (v) হিসাব করো"):
                v = u + (a * t)
                st.success(f"📊 শেষ বেগ, $v = {v}$ m/s")
                
        with tab2:
            st.header("📝 গতি অধ্যায়ের কুইজ")
            q1 = st.radio("১. সময়ের সাথে অসম বেগের পরিবর্তনের হারকে কী বলে?", ["মন্দন", "ত্বরণ", "দ্রুতি", "বেগ"])
            if st.button("উত্তর যাচাই করুন", key="q1_9"):
                if q1 == "ত্বরণ":
                    st.success("সঠিক উত্তর! 🎉")
                else:
                    st.error("ভুল উত্তর। সঠিক উত্তর: ত্বরণ")

    elif selected_subject == "রসায়ন (Chemistry)":
        with tab1:
            st.header("🧪 অধ্যায়: পদার্থের গঠন (Structure of Matter)")
            st.info("💡 **মনে রেখো:** পরমাণুর কেন্দ্রে থাকে নিউক্লিয়াস (প্রোটন ও নিউট্রন থাকে) এবং বাইরে ইলেকট্রন ঘোরে।")
            
            # পরমাণুর কণা হিসাব
            st.subheader("🔢 ইলেকট্রন, প্রোটন ও নিউট্রন সংখ্যা বের করো")
            atomic_number = st.number_input("পারমাণবিক সংখ্যা (Z):", min_value=1, max_value=118, value=11)
            mass_number = st.number_input("ভর সংখ্যা (A):", min_value=1, max_value=294, value=23)
            
            if st.button("কণা সংখ্যা হিসাব করো"):
                protons = atomic_number
                electrons = atomic_number
                neutrons = mass_number - atomic_number
                st.write(f"🔹 **প্রোটন সংখ্যা:** {protons}")
                st.write(f"🔹 **ইলেকট্রন সংখ্যা:** {electrons}")
                st.write(f"🔹 **নিউট্রন সংখ্যা:** {neutrons}")
                
        with tab2:
            st.header("📝 রসায়ন কুইজ")
            q2 = st.radio("১. সোডিয়াম (Na) এর পারমাণবিক সংখ্যা কত?", ["১০", "১১", "১২", "১৩"])
            if st.button("উত্তর যাচাই করুন", key="q2_9"):
                if q2 == "১১":
                    st.success("সঠিক উত্তর! 🎉")
                else:
                    st.error("ভুল উত্তর। সঠিক উত্তর: ১১")

# ==============================================================================
# ২. একাদশ-দ্বাদশ শ্রেণী (Class 11-12)
# ==============================================================================
else:
    if selected_subject == "পদার্থবিজ্ঞান (Physics)":
        with tab1:
            st.header("📐 অধ্যায়: ভেক্টর (Vector)")
            st.markdown("### **দুটি ভেক্টরের লব্ধির মান ($R$) নির্ণয়:**")
            st.latex(r"R = \sqrt{P^2 + Q^2 + 2PQ\cos\alpha}")
            
            # লব্ধি ক্যালকুলেটর
            st.subheader("🧮 লব্ধি নির্ণায়ক ক্যালকুলেটর")
            import math
            p = st.number_input("প্রথম ভেক্টর (P):", value=3.0)
            q = st.number_input("দ্বিতীয় ভেক্টর (Q):", value=4.0)
            alpha = st.number_input("মধ্যবর্তী কোণ (Alpha in degree):", value=90.0)
            
            if st.button("লব্ধি (R) হিসাব করো"):
                alpha_rad = math.radians(alpha)
                r = math.sqrt(p**2 + q**2 + 2*p*q*math.cos(alpha_rad))
                st.success(f"📊 লব্ধির মান, $R = {round(r, 4)}$")
                
        with tab2:
            st.header("📝 ভেক্টর কুইজ")
            q3 = st.radio("১. দুটি ভেক্টরের স্কেলার (ডট) গুণন শূন্য হলে ভেক্টরদ্বয়ের মধ্যবর্তী কোণ কত?", ["0°", "45°", "90°", "180°"])
            if st.button("উত্তর যাচাই করুন", key="q3_11"):
                if q3 == "90°":
                    st.success("সঠিক উত্তর! 🎉")
                else:
                    st.error("ভুল উত্তর। সঠিক উত্তর: 90°")

    elif selected_subject == "রসায়ন (Chemistry)":
        with tab1:
            st.header("⚗️ অধ্যায়: পরিমাণগত রসায়ন (Quantitative Chemistry)")
            st.markdown("### **মোলারিটি ও দ্রবণ সূত্র:**")
            st.latex(r"W = \frac{SMV}{1000}")
            st.caption("এখানে, W = দ্রবের ভর (g), S = মোলারিটি (M), M = আণবিক ভর, V = আয়তন (mL)")
            
            # ভর ক্যালকুলেটর
            st.subheader("🧮 প্রয়োজনীয় দ্রবের ভর (W) নির্ণয়")
            s = st.number_input("ঘনমাত্রা বা মোলারিটি (S in M):", value=0.1)
            m_molecular = st.number_input("দ্রবের আণবিক ভর (M) [যেমন NaOH = 40]:", value=40.0)
            v_volume = st.number_input("দ্রবণের আয়তন (V in mL):", value=250.0)
            
            if st.button("ভর (W) হিসাব করো"):
                w = (s * m_molecular * v_volume) / 1000
                st.success(f"⚖️ প্রয়োজনীয় দ্রবের ভর, $W = {w}$ গ্রাম")
                
        with tab2:
            st.header("📝 পরিমাণগত রসায়ন কুইজ")
            q4 = st.radio("১. সেমিমোলার দ্রবণের ঘনমাত্রা কত?", ["1.0 M", "0.5 M", "0.1 M", "0.01 M"])
            if st.button("উত্তর যাচাই করুন", key="q4_11"):
                if q4 == "0.5 M":
                    st.success("সঠিক উত্তর! 🎉")
                else:
                    st.error("ভুল উত্তর। সঠিক উত্তর: 0.5 M")
