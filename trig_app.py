import streamlit as st
import numpy as np
import plotly.graph_objects as go  # <--- THIS WAS MISSING
import math

# Page setup
st.set_page_config(
    page_title="Yousef's Math Lab",
    page_icon="📉",
    layout="wide",
    initial_sidebar_state="expanded"
)

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

# --- MATH LOGIC ---
def solve_math(expr, x_range):
    safe_dict = {
        "x": x_range, "sin": np.sin, "cos": np.cos, "tan": np.tan,
        "pi": np.pi, "sqrt": np.sqrt, "exp": np.exp, "abs": np.abs
    }
    clean_expr = expr.replace("^", "**")
    return eval(clean_expr, {"__builtins__": {}}, safe_dict)

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("<h2 style='text-align:center;'>🛠️ المختبر الرياضي</h2>", unsafe_allow_html=True)
    x_min = st.number_input("x من", value=-6.28)
    x_max = st.number_input("x إلى", value=6.28)
    st.divider()
    line_color = st.color_picker("🎨 لون المنحنى", "#6366f1")
    fill_area = st.checkbox("تظليل المساحة", value=True)
    grid_alpha = st.slider("شفافية الشبكة", 0.0, 1.0, 0.3)

# --- HEADER ---
st.markdown("<div class='glow-text'>راسم الدوال الذكي</div>", unsafe_allow_html=True)

# --- PRESET EXAMPLES ---
if "current_expr" not in st.session_state:
    st.session_state.current_expr = "sin(x)"

st.markdown("##### 🚀 نماذج سريعة")
cols = st.columns(6)
presets = {
    "Sin Wave": "sin(x)",
    "Cos Wave": "cos(x)",
    "Tan Graph": "tan(x)",
    "Complex": "sin(x)*cos(x*2)",
    "Pulse": "sin(x)*exp(-abs(x)/5)",
    "Square": "x^2"
}

for i, (name, formula) in enumerate(presets.items()):
    if cols[i].button(name, use_container_width=True):
        st.session_state.current_expr = formula
        st.rerun() # Refresh to update input box

# --- MAIN INPUT ---
expr_input = st.text_input("✍️ اكتب دالتك الرياضية (مثال: sin(x) + cos(x/2))", 
                          value=st.session_state.current_expr)

# --- CALCULATION & PLOT ---
try:
    x = np.linspace(x_min, x_max, 1000)
    y = solve_math(expr_input, x)
    y_plot = np.copy(y)
    y_plot[np.abs(y_plot) > 20] = np.nan 

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=x, y=y_plot, mode='lines',
        line=dict(color=line_color, width=4),
        fill='tozeroy' if fill_area else None,
        fillcolor=f"rgba(99, 102, 241, 0.1)",
        name=expr_input
    ))

    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(gridcolor=f'rgba(255,255,255,{grid_alpha})', zerolinecolor='white'),
        yaxis=dict(gridcolor=f'rgba(255,255,255,{grid_alpha})', zerolinecolor='white'),
        font=dict(color="white"), height=450
    )

    st.plotly_chart(fig, use_container_width=True)

    # --- ANALYSIS ---
    st.markdown("### 📊 تحليل البيانات")
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.markdown(f"<div class='metric-card'><b>أعلى قيمة</b><br><h2 style='color:#10b981'>{np.nanmax(y):.2f}</h2></div>", unsafe_allow_html=True)
    with m2:
        st.markdown(f"<div class='metric-card'><b>أدنى قيمة</b><br><h2 style='color:#ef4444'>{np.nanmin(y):.2f}</h2></div>", unsafe_allow_html=True)
    with m3:
        st.markdown(f"<div class='metric-card'><b>المتوسط</b><br><h2>{np.nanmean(y):.2f}</h2></div>", unsafe_allow_html=True)
    with m4:
        st.markdown(f"<div class='metric-card'><b>المجال x</b><br><h2>{x_max - x_min:.1f}</h2></div>", unsafe_allow_html=True)

except Exception as e:
    st.error(f"⚠️ خطأ في الصيغة: {e}")

st.markdown("<br><hr>", unsafe_allow_html=True)
st.write("👤 **إعداد الطالب:** يوسف | عاشر - ب")
