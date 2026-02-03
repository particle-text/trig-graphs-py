import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import math

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="مشروع الرياضيات التفاعلي",
    layout="wide"
)

# ---------- SESSION ----------
if "expr" not in st.session_state:
    st.session_state.expr = "cos(x)"

# ---------- STYLE ----------
st.markdown("""
<style>
body {
    background-color: #0e1117;
    color: white;
}

.block-container {
    padding-top: 1.5rem;
}

.card {
    background-color: #161b22;
    padding: 20px;
    border-radius: 14px;
}

input {
    font-size: 18px !important;
}
</style>
""", unsafe_allow_html=True)

# ---------- SIDEBAR ----------
st.sidebar.markdown("## ⚙️ الإعدادات")

x_min = st.sidebar.number_input("x من", value=-10.0)
x_max = st.sidebar.number_input("x إلى", value=10.0)

color = st.sidebar.selectbox(
    "🎨 لون الرسم",
    ["blue", "red", "green", "purple", "orange"]
)

line_width = st.sidebar.slider("✏️ سمك الخط", 1, 5, 2)

# ---------- TITLE ----------
st.markdown(
    "<h1 style='text-align:center;'>📊 مشروع الرياضيات التفاعلي</h1>",
    unsafe_allow_html=True
)

# ---------- INPUT CARD ----------
st.markdown("<div class='card'>", unsafe_allow_html=True)

expr = st.text_input("✍️ y =", value=st.session_state.expr)

c1, c2 = st.columns(2)
with c1:
    if st.button("❌ مسح المعادلة"):
        st.session_state.expr = ""
        st.experimental_rerun()

with c2:
    clear_plot = st.button("🧹 مسح الرسم")

st.markdown("</div>", unsafe_allow_html=True)

# ---------- CALC ----------
x = np.linspace(x_min, x_max, 500)

safe = {
    "x": x,
    "sin": np.sin,
    "cos": np.cos,
    "tan": np.tan,
    "pi": math.pi
}

def calc(expr):
    return eval(expr.replace("^", "**"), {"__builtins__": {}}, safe)

# ---------- PLOT ----------
if expr and not clear_plot:
    try:
        y = calc(expr)
        y = np.clip(y, -20, 20)

        fig, ax = plt.subplots(figsize=(6.5, 3.2))  # 👈 حجم مناسب بدون Scroll
        ax.plot(x, y, color=color, linewidth=line_width)

        ax.set_title(f"y = {expr}")
        ax.grid(True, linestyle="--", alpha=0.6)

        st.pyplot(fig)

    except:
        st.error("❌ المعادلة غير صحيحة")

# ---------- FOOTER ----------
st.markdown("---")
st.markdown("""
**الاسم:** يوسف  
**الصف:** عاشر (ب)
""")
