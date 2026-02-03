import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import math

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="مشروع يوسف - الدوال المثلثية",
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
.math-bg {
    position: fixed;
    top: 0;
    left: 0;
    opacity: 0.04;
    font-size: 90px;
    z-index: -1;
}
.card {
    background-color: #161b22;
    padding: 20px;
    border-radius: 15px;
}
</style>

<div class="math-bg">
π sin cos tan π sin cos tan
</div>
""", unsafe_allow_html=True)

# ---------- SIDEBAR ----------
st.sidebar.title("⚙️ الإعدادات")

x_min = st.sidebar.number_input("x من =", value=-10.0)
x_max = st.sidebar.number_input("x إلى =", value=10.0)

color = st.sidebar.selectbox(
    "🎨 لون الرسم",
    ["blue", "red", "green", "purple", "orange", "black"]
)

line_width = st.sidebar.slider("✏️ سمك الخط", 1, 5, 2)

# ---------- TITLE ----------
st.markdown(
    "<h1 style='text-align:center;'>📊 رسم الدوال المثلثية</h1>",
    unsafe_allow_html=True
)

# ---------- EXAMPLES ----------
st.markdown("### ⭐ معادلات جاهزة")
examples = {
    "sin(x)": "sin(x)",
    "cos(x)": "cos(x)",
    "tan(x)": "tan(x)",
    "sin(x)+cos(x)": "sin(x)+cos(x)",
    "sin(x)*cos(x)": "sin(x)*cos(x)",
    "x^2": "x^2",
    "sin(x)+sin(2*x)*cos(3*x)+sin(5*x)/5": "sin(x)+sin(2*x)*cos(3*x)+sin(5*x)/5"
}

cols = st.columns(len(examples))
for col, (name, val) in zip(cols, examples.items()):
    if col.button(name):
        st.session_state.expr = val

# ---------- INPUT ----------
st.markdown("<div class='card'>", unsafe_allow_html=True)
expr = st.text_input("✍️ y =", value=st.session_state.expr)

c1, c2, c3 = st.columns(3)
with c1:
    if st.button("❌ مسح المعادلة"):
        st.session_state.expr = ""
        st.experimental_rerun()
with c2:
    clear_plot = st.button("🧹 مسح الرسم")
with c3:
    save_plot = st.button("💾 حفظ الرسم")

st.markdown("</div>", unsafe_allow_html=True)

# ---------- EXPLANATION ----------
explanations = {
    "sin(x)": "دالة الجيب: دورها 2π، مداها من -1 إلى 1",
    "cos(x)": "دالة جيب التمام: تبدأ من 1",
    "tan(x)": "دالة الظل: غير معرفة عند π/2 + kπ",
    "x^2": "دالة تربيعية على شكل U"
}

if expr in explanations:
    st.info("📘 شرح المعادلة: " + explanations[expr])

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

        fig, ax = plt.subplots(figsize=(7, 3.5))
        ax.plot(x, y, color=color, linewidth=line_width)
        ax.set_title(f"y = {expr}")
        ax.grid(True, linestyle="--", alpha=0.6)

        st.pyplot(fig)

        if save_plot:
            fig.savefig("graph.png")
            st.success("✅ تم حفظ الرسم باسم graph.png")

    except:
        st.error("❌ المعادلة غير صحيحة")

# ---------- FOOTER ----------
st.markdown("---")
st.markdown("""
**الاسم:** يوسف  
**الصف:** عاشر (ب)
""")
