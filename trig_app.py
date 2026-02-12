import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import math

# Page setup
st.set_page_config(
    page_title="مشروع يوسف - الدوال المثلثية",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- MODERN STYLING (CSS) ---
st.markdown("""
<style>
    /* Main background */
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        color: #f8fafc;
    }
    
    /* Card design for inputs */
    .main-card {
        background: rgba(255, 255, 255, 0.05);
        padding: 2rem;
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        margin-bottom: 20px;
    }
    
    /* Background math pattern */
    .math-pattern {
        position: fixed;
        top: 10%;
        left: 5%;
        font-size: 150px;
        font-weight: bold;
        color: rgba(255,255,255,0.02);
        z-index: -1;
        user-select: none;
    }
    
    /* Title styling */
    h1 {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        background: -webkit-linear-gradient(#3b82f6, #8b5cf6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
        text-align: center;
    }
    
    /* Style buttons */
    .stButton>button {
        border-radius: 10px;
        transition: all 0.3s ease;
        width: 100%;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.3);
    }
</style>

<div class="math-pattern">f(x) = sin(θ)</div>
""", unsafe_allow_html=True)

# --- SESSION STATE ---
if "expr" not in st.session_state:
    st.session_state.expr = "sin(x)"

# --- SIDEBAR SETTINGS ---
with st.sidebar:
    st.markdown("## ⚙️ التحكم في الرسم")
    x_min = st.number_input("بداية المحور (x من)", value=-10.0)
    x_max = st.number_input("نهاية المحور (x إلى)", value=10.0)
    
    st.divider()
    
    color = st.color_picker("🎨 اختر لون المنحنى", "#3b82f6")
    line_width = st.slider("✏️ سمك الخط", 1, 10, 3)
    grid_on = st.checkbox("إظهار الشبكة", value=True)

# --- MAIN CONTENT ---
st.markdown("<h1>📊 راسم الدوال المثلثية الاحترافي</h1>", unsafe_allow_html=True)

# Preset Buttons Section
st.markdown("### ⚡ اختصارات ذكية")
examples = {
    "Sin(x)": "sin(x)",
    "Cos(x)": "cos(x)",
    "Tan(x)": "tan(x)",
    "Wave Mixed": "sin(x)+cos(x*2)",
    "Complexity": "sin(x)*cos(x/2)",
    "Harmonic": "sin(x)+sin(3*x)/3+sin(5*x)/5"
}

# Create row of buttons
cols_examples = st.columns(len(examples))
for i, (name, val) in enumerate(examples.items()):
    if cols_examples[i].button(name):
        st.session_state.expr = val

# Input Section with Modern Container
with st.container():
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    expr = st.text_input("✍️ أدخل المعادلة الرياضية (استخدم x كمتغير):", value=st.session_state.expr, key="eq_input")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("❌ مسح"):
            st.session_state.expr = ""
            st.rerun()
    with c2:
        save_plot = st.button("💾 حفظ صورة")
    with c3:
        st.button("🔄 تحديث")
    st.markdown('</div>', unsafe_allow_html=True)

# Calculations
x = np.linspace(x_min, x_max, 1000) # Increased density for smoother curves
safe = {"x": x, "sin": np.sin, "cos": np.cos, "tan": np.tan, "pi": math.pi, "sqrt": np.sqrt}

if expr:
    try:
        # Evaluate math logic
        y = eval(expr.replace("^", "**"), {"__builtins__": {}}, safe)
        y = np.clip(y, -50, 50) # Prevent infinity from breaking the visual

        # --- MATPLOTLIB STYLING ---
        plt.style.use('dark_background')
        fig, ax = plt.subplots(figsize=(10, 5))
        fig.patch.set_facecolor('#1e293b') # Match app bg
        ax.set_facecolor('#1e293b')
        
        ax.plot(x, y, color=color, linewidth=line_width, label=f"y = {expr}")
        
        # Axis labels and ticks
        ax.tick_params(colors='white', which='both')
        ax.spines['bottom'].set_color('#64748b')
        ax.spines['left'].set_color('#64748b')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        
        if grid_on:
            ax.grid(True, linestyle="--", alpha=0.2, color="#94a3b8")
        
        ax.axhline(0, color='white', linewidth=0.5) # x-axis line
        ax.axvline(0, color='white', linewidth=0.5) # y-axis line
        
        st.pyplot(fig)

        if save_plot:
            fig.savefig("my_graph.png", dpi=300)
            st.success("🎉 تم حفظ الرسم بنجاح!")

    except Exception as e:
        st.error(f"⚠️ خطأ في المعادلة: تأكد من كتابتها بشكل صحيح. مثال: sin(x)")

# Footer Section
st.markdown("---")
footer_col1, footer_col2 = st.columns(2)
with footer_col1:
    st.markdown(f"""
    **👨‍💻 المبرمج:** يوسف  
    **🏫 الصف:** عاشر (ب)
    """)
with footer_col2:
    st.markdown("""
    <div style='text-align: left; opacity: 0.6;'>
    تم التطوير باستخدام Python & Streamlit 🚀
    </div>
    """, unsafe_allow_html=True)
