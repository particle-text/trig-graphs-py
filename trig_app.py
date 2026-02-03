import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import math

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="مشروع الرياضيات التفاعلي",
    layout="wide"
)

# ---------------- SIDEBAR ----------------
st.sidebar.title("⚙️ الإعدادات")

dark_mode = st.sidebar.checkbox("🌙 وضع ليلي", value=True)

x_min = st.sidebar.number_input("x من =", value=-10.0)
x_max = st.sidebar.number_input("x إلى =", value=10.0)

color = st.sidebar.selectbox(
    "🎨 لون الرسم",
    ["blue", "red", "green", "purple", "orange", "black"]
)

line_width = st.sidebar.slider("✏️ سمك الخط", 1, 5, 2)

# ---------------- STYLE ----------------
if dark_mode:
    bg = "#0e1117"
    fg = "white"
else:
    bg = "white"
    fg = "black"

st.markdown(f"""
<style>
body {{
    background-color: {bg};
    color: {fg};
}}
</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown(
    "<h1 style='text-align:center;'>📊 مشروع الرياضيات التفاعلي</h1>",
    unsafe_allow_html=True
)

# ---------------- INPUT ----------------
expr = st.text_input("✍️ y =", value="cos(x)")

col1, col2 = st.columns(2)
with col1:
    clear_expr = st.button("❌ مسح المعادلة")
with col2:
    clear_plot = st.button("🧹 مسح الرسم")

if clear_expr:
    st.experimental_rerun()

# ---------------- CALCULATION ----------------
x = np.linspace(x_min, x_max, 600)

safe_dict = {
    "x": x,
    "sin": np.sin,
    "cos": np.cos,
    "tan": np.tan,
    "sqrt": np.sqrt,
    "log": np.log,
    "pi": math.pi,
    "abs": np.abs
}

def safe_eval(expr):
    return eval(expr.replace("^", "**"), {"__builtins__": {}}, safe_dict)

# ---------------- PLOT ----------------
if expr and not clear_plot:
    try:
        y = safe_eval(expr)

        # منع تخبيص tan
        y = np.clip(y, -20, 20)

        fig, ax = plt.subplots()
        ax.plot(x, y, color=color, linewidth=line_width)

        ax.set_title(f"y = {expr}")
        ax.set_xlabel("x")
        ax.set_ylabel("y")

        ax.grid(True, linestyle="--", alpha=0.5)

        st.pyplot(fig)

    except:
        st.error("❌ المعادلة غير صحيحة")

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown("""
**الاسم:** يوسف  
**الصف:** عاشر (ب)
""")
