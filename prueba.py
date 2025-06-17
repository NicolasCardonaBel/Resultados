import streamlit as st
import numpy as np
from colour import Lab_to_XYZ, XYZ_to_sRGB

st.set_page_config(page_title="Ajuste interactivo de L*a*b*", layout="centered")

st.title("🎨 Ajuste interactivo de color en L*a*b*")

st.markdown("Ajusta los valores manualmente o con los sliders:")

# ==================================
# INTERFAZ: Entrada manual + slider
# ==================================
def lab_slider_input(label, value, minval, maxval, step):
    col1, col2 = st.columns([1, 3])
    with col1:
        val_input = st.number_input(label, value=value, min_value=minval, max_value=maxval, step=step, key=f"{label}_input")
    with col2:
        val_slider = st.slider(f"{label}", minval, maxval, value=val_input, step=step, key=f"{label}_slider", label_visibility="collapsed")
    return val_slider

L = lab_slider_input("L", 36.0, 0.0, 100.0, 0.1)
a = lab_slider_input("a", 45.0, -128.0, 127.0, 0.1)
b = lab_slider_input("b", 27.0, -128.0, 127.0, 0.1)

lab = np.array([L, a, b])

# ==================================
# CONVERSIÓN: LAB → sRGB
# ==================================
xyz = Lab_to_XYZ(lab)
rgb = XYZ_to_sRGB(xyz)
rgb_clipped = np.clip(rgb, 0, 1)
rgb_255 = (rgb_clipped * 255).astype(np.uint8)
hex_color = '#%02x%02x%02x' % tuple(rgb_255)

# ==================================
# VISUALIZACIÓN DEL COLOR
# ==================================
st.markdown(f"""
<div style='width:300px; height:150px; background-color:{hex_color}; border:2px solid black; margin:auto'></div>
""", unsafe_allow_html=True)

# ==================================
# MOSTRAR VALORES
# ==================================
st.write(f"**L*a*b***: {np.round(lab, 2)}")
st.write(f"**sRGB [0-1]**: {np.round(rgb_clipped, 3)}")
st.write(f"**sRGB [0-255]**: {rgb_255}")
st.code(hex_color, language='bash')

# import streamlit as st
# import numpy as np
# from colour import Lab_to_XYZ, XYZ_to_sRGB

# st.set_page_config(page_title="Ajuste interactivo de L*a*b*", layout="centered")

# st.title("🎨 Ajuste interactivo de color en L*a*b*")

# # Sliders para L, a, b
# L = st.slider("L (luminosidad)", min_value=0.0, max_value=100.0, value=36.0, step=0.1)
# a = st.slider("a (verde ↔ rojo)", min_value=-128.0, max_value=127.0, value=45.0, step=0.1)
# b = st.slider("b (azul ↔ amarillo)", min_value=-128.0, max_value=127.0, value=27.0, step=0.1)

# lab = np.array([L, a, b])

# # Convertir a sRGB
# xyz = Lab_to_XYZ(lab)
# rgb = XYZ_to_sRGB(xyz)
# rgb_clipped = np.clip(rgb, 0, 1)
# rgb_255 = (rgb_clipped * 255).astype(np.uint8)

# # Mostrar patch de color
# hex_color = '#%02x%02x%02x' % tuple(rgb_255)

# st.markdown(f"""
# <div style='width:200px; height:200px; background-color:{hex_color}; border:2px solid black; margin:auto'></div>
# """, unsafe_allow_html=True)

# # Mostrar valores
# st.write(f"**L*a*b***: {lab}")
# st.write(f"**sRGB [0-1]**: {np.round(rgb_clipped, 3)}")
# st.write(f"**sRGB [0-255]**: {rgb_255}")
# st.code(hex_color, language='bash')
