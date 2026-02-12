import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import math

# Page setup
st.set_page_config(page_title="Yousef's Math Lab", page_icon="📉", layout="wide")

# --- ADVANCED PREMIUM STYLING ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    html, body, [class*="css"] { font-family: 'Cairo', sans-serif; }
    .stApp { background: radial-gradient(circle at top right, #1e293b, #0f172a); color: #f8fafc; }
    .glow-text {
        text-align: center; font-size: 3rem; font-weight: 800;
        background: linear-gradient(90deg, #3b82f6, #8b5cf6, #3b82f6);
        background-size: 200% auto; -webkit-background-clip: text;
        -webkit-text-fill-color: transparent; animation: gradient 3s linear infinite;
    }
    @keyframes gradient { 0% { background-position: 0% center; } 100% { background-position: 200% center; } }
    .metric-card {
        background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 15px; border-radius: 15px; text-align: center;
    }
</style>
""", unsafe_allow_html=True)

if "current_expr" not in st.session_state:
    st.session_state.current_expr = "sin(x)"

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("## ⚙️ الإعدادات")
    x_min = st.number_input("x من", value=-10.0)
    x_max = st.number_input("x إلى", value=10.0)
    line_color = st.color_picker("🎨 لون الخط", "#3b82f6")
    grid_on = st.checkbox("إظهار الشبكة", value=True)

st.markdown("<div class='glow-text'>راسم الدوال الذكي</div>", unsafe_allow_html=True)

# --- PRESETS ---
cols = st.columns(4)
presets = {"Sin(x)": "sin(x)", "Cos(x)": "cos(x)", "Tan(x)": "tan(x)", "Square": "x^2"}
for i, (name, formula) in enumerate(presets.items()):
    if cols[i%4].button(name, use_container_width=True):
        st.session_state.current_expr = formula
        st.rerun()

expr_input = st.text_input("✍️ أدخل المعادلة:", value=st.session_state.current_expr)

# --- PLOTTING ---
try:
    x = np.linspace(x_min, x_max, 1000)
    safe_dict = {"x": x, "sin": np.sin, "cos": np.cos, "tan": np.tan, "pi": np.pi, "sqrt": np.sqrt}
    y = eval(expr_input.replace("^", "**"), {"__builtins__": {}}, safe_dict)
    
    # Create Matplotlib Figure
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(10, 4))
    fig.patch.set_facecolor('#0f172a')
    ax.set_facecolor('#0f172a')
    
    y_masked = np.ma.masked_where(np.abs(y) > 20, y) # Fix Tan(x) lines
    ax.plot(x, y_masked, color=line_color, linewidth=3)
    
    if grid_on:
        ax.grid(alpha=0.2)
    
    st.pyplot(fig)

    # --- STATS ---
    st.markdown("### 📊 تحليل البيانات")
    c1, c2, c3 = st.columns(3)
    c1.markdown(f"<div class='metric-card'>Max<br><h2>{np.nanmax(y):.2f}</h2></div>", unsafe_allow_html=True)
    c2.markdown(f"<div class='metric-card'>Min<br><h2>{np.nanmin(y):.2f}</h2></div>", unsafe_allow_html=True)
    c3.markdown(f"<div class='metric-card'>Mean<br><h2>{np.nanmean(y):.2f}</h2></div>", unsafe_allow_html=True)

except Exception as e:
    st.error("صيغة غير صحيحة")

# --- FOOTER ---
st.markdown("<br><hr>", unsafe_allow_html=True)
f1, f2 = st.columns(2)
with f1:
    st.write("👤 **إعداد الطالب:** يوسف")
    st.write("🏫 **الصف:** عاشر - ب")
with f2:
    st.markdown("<div style='text-align:left'>2024 © مختبر الرياضيات الرقمي</div>", unsafe_allow_html=True)
