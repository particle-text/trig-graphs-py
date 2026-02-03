import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import math

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="مشروع الرياضيات التفاعلي",
    layout="wide"
)

# ---------- SIDEBAR ----------
st.sidebar.title("⚙️ الإعدادات")

dark_mode = st.sidebar.checkbox("🌙 وضع ليلي", value=True)

x_min = st.sidebar.number_input("x من =", value=-10.0)
x_max = st.sidebar.number_input("x إلى =", value=10.0)

color = st.sidebar.selectbox(
    "🎨 لون الرسم",
    ["blue", "red", "green", "purple", "orange", "black"]
)

line_width = st.sidebar.slider("✏️ سمك الخط", 1, 5, 2)

# ---------- STYLE ----------
if dark_mode:
    bg = "#0e1117"
    fg = "white"
    card = "#161b22"
else:
    bg = "#ffffff"
    fg = "black"
    card = "#f4f4f4"

st.markdown(f"""
<style>
body {{
    background-color: {bg};
    color: {fg};
}}
.math-bg {{
    position: fixed;
    top: 0;
    left: 0;
    opacity: 0.04;
    font-size: 80px;
    z-index: -1;
}}
.card {{
    background-color: {card};
    padding: 20px;
    border-radius: 15px;
}}
</style>

<div class="math-bg">
π sin cos ∫ tan √ x² log π sin cos ∫
</div>
""", unsafe_allow_html=True)

# ---------- TITLE ----------
st.markdown(
    "<h1 style='text-align:center;'>📊 مشروع الرياضيات التفاعلي</h1>",
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
    "√|x|": "sqrt(abs(x))"
}

cols = st.columns(len(examples))
for col, (name, val) in zip(cols, examples.items()):
    if col.button(name):
        st.session_state.expr = val

# ---------- INPUT ----------
if "expr" not in st.session_state:
    st.session_state.expr = "cos(x)"

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
    "sqrt": np.sqrt,
    "log": np.log,
    "abs": np.abs,
    "pi": math.pi
}

def calc(expr):
    return eval(expr.replace("^", "**"), {"__builtins__": {}}, safe)

# ---------- PLOT ----------
if expr and not clear_plot:
    try:
        y = calc(expr)
        y = np.clip(y, -20, 20)

        fig, ax = plt.subplots(figsize=(7, 3.5))  # 👈 رسم أصغر
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
