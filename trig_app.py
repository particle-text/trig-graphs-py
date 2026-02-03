import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import math

# ======================
# إعداد الصفحة
# ======================
st.set_page_config(
    page_title="Interactive Math Graph",
    layout="wide"
)

# ======================
# إخفاء الـ Sidebar
# ======================
st.markdown("""
<style>
[data-testid="stSidebar"] {
    display: none;
}
</style>
""", unsafe_allow_html=True)

# ======================
# اللغة (Session State)
# ======================
if "lang" not in st.session_state:
    st.session_state.lang = "ar"

def t(ar, en):
    return ar if st.session_state.lang == "ar" else en

# ======================
# الهيدر + الشعار
# ======================
col1, col2 = st.columns([1, 6])

with col1:
    st.image("logo.png", width=120)

with col2:
    st.markdown(
        f"<h1 style='text-align:right'>{t('مشروع الرياضيات التفاعلي','Interactive Math Project')}</h1>",
        unsafe_allow_html=True
    )

# زر تغيير اللغة
if st.button(t("English 🌍", "العربية 🌍")):
    st.session_state.lang = "en" if st.session_state.lang == "ar" else "ar"
    st.rerun()

st.divider()

# ======================
# إدخال المعادلة والمجال
# ======================
c1, c2, c3 = st.columns(3)

with c1:
    x_min = st.number_input(t("من x =", "From x ="), value=-10.0)

with c2:
    x_max = st.number_input(t("إلى x =", "To x ="), value=10.0)

with c3:
    color = st.selectbox(
        t("لون الرسم", "Graph Color"),
        ["blue", "red", "green", "purple", "orange"]
    )

equation = st.text_input(
    t("أدخل المعادلة (مثال: sin(x)+cos(x))",
      "Enter equation (example: sin(x)+cos(x))"),
    value="cos(x)"
)

line_width = st.slider(
    t("سماكة الخط", "Line Width"),
    1, 5, 2
)

# ======================
# أزرار التحكم
# ======================
b1, b2 = st.columns(2)

with b1:
    clear_eq = st.button(t("🧹 مسح المعادلة", "🧹 Clear Equation"))

with b2:
    clear_plot = st.button(t("🎨 مسح الرسم", "🎨 Clear Plot"))

if clear_eq:
    st.rerun()

# ======================
# الرسم
# ======================
if equation and not clear_plot:
    try:
        x = np.linspace(x_min, x_max, 1000)

        allowed = {
            "sin": np.sin,
            "cos": np.cos,
            "tan": np.tan,
            "pi": np.pi,
            "x": x
        }

        y = eval(equation, {"__builtins__": {}}, allowed)

        fig, ax = plt.subplots(figsize=(8, 4))
        ax.plot(x, y, color=color, linewidth=line_width)

        ax.set_title(f"y = {equation}")
        ax.grid(True)

        st.pyplot(fig)

    except Exception as e:
        st.error(t("خطأ في المعادلة ❌", "Equation Error ❌"))
