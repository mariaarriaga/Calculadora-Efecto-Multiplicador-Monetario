import streamlit as st

# Título
st.markdown("<h1 style='text-align:center; color:darkblue;'>Calculadora Efecto Multiplicador Monetario</h1>", unsafe_allow_html=True)
st.markdown("---")
st.subheader("Ingresá los valores:")

# Inputs
R = st.number_input("Reservas R:", step=0.1, format="%.2f")
E = st.number_input("Efectivo E:", step=0.1, format="%.2f")
D = st.number_input("Depósitos D:", step=0.1, format="%.2f")
B = st.number_input("Base B:", step=0.1, format="%.2f")

# Función de cálculo
def calcular_M(R, E, D, B):
    if D == 0:
        return "❌ Error: D no puede ser 0.", None, None
    e = E / D
    r = R / D
    if e < 0:
        return "❌ Error: e debe ser mayor o igual a 0 (E/D ≥ 0).", None, None
    if not (0 < r <= 1):
        return "❌ Error: r debe estar entre 0 (exclusivo) y 1 (inclusivo).", None, None
    M = ((e + 1) / (e + r)) * B
    return f"✅ Resultado: M = {M:.4f}", e, r

# Botón
if st.button("Calcular M"):
    resultado, e, r = calcular_M(R, E, D, B)
    st.write(resultado)
    if e is not None and r is not None:
        st.write(f"Coeficiente e = E/D = {e:.4f}")
        st.write(f"Coeficiente r = R/D = {r:.4f}")
