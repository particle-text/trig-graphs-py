import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import math

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Trigonometric Graph Visualizer",
    layout="centered"
)

# ---------------- STYLE ----------------
st.markdown("""
<style>
body {
    background-color: white;
    background-image:
        repeating-linear-gradient(
            45deg,
            rgba(0, 0, 0, 0.03),
            rgba(0, 0, 0, 0.03) 1px,
            transparent 1px,
            transparent 20px
        );
}
</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.title("📈 Trigonometric Graph Visualizer")
st.write("اكتب معادلة مثل: sin(x), cos(x), x^2 + 3*x")

# ---------------- INPUTS ----------------
expr = st.text_input("y =", value="sin(x)")

col1, col2 = st.columns(2)
with col1:
    x_min = st.number_input("من", value=-10.0)
with col2:
    x_max = st.number_input("إلى", value=10.0)

color = st.color_picker("اختر لون الرسم", "#1f77b4")

clear = st.button("🧹 مسح الرسم")

# ---------------- PLOT ----------------
x = np.linspace(x_min, x_max, 400)

allowed = {
    "x": x,
    "sin": np.sin,
    "cos": np.cos,
    "tan": np.tan,
    "sqrt": np.sqrt,
    "log": np.log,
    "pi": math.pi
}

if expr and not clear:
    try:
        y = eval(expr, {"__builtins__": {}}, allowed)

        fig, ax = plt.subplots()
        ax.plot(x, y, color=color)
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.grid(True)

        st.pyplot(fig)

    except Exception as e:
        st.error("❌ المعادلة غير صحيحة")

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown("**الاسم:** يوسف  \n**الصف:** عاشر (ب)")
