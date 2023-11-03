import streamlit as st
import sympy as sym
from scipy.optimize import fsolve
import numpy as np

st.title("Nonlinear Equation Solver")

st.write("Enter a system of equations in the form of F(x, y, w) = 0")

# User input for the equations
equation1 = st.text_input("Equation 1 (e.g., 'x**2 + y**2 - 20'):")
equation2 = st.text_input("Equation 2 (e.g., 'y - x**2'):")
equation3 = st.text_input("Equation 3 (e.g., 'w + 5 - x*y'):")

if not all([equation1, equation2, equation3]):
    st.warning("Please enter valid equations in all fields.")
else:
    # Define symbolic variables
    x, y, w = sym.symbols('x y w')

    # Define the system of equations using sympy
    equation1_sym = sym.Eq(sym.sympify(equation1), 0)
    equation2_sym = sym.Eq(sym.sympify(equation2), 0)
    equation3_sym = sym.Eq(sym.sympify(equation3), 0)

    def myFunction(z):
        x, y, w = z

        F = np.empty((3))
        F[0] = equation1_sym.subs({x: x, y: y, w: w}).rhs  # Extract the right-hand side
        F[1] = equation2_sym.subs({x: x, y: y, w: w}).rhs
        F[2] = equation3_sym.subs({x: x, y: y, w: w}).rhs
        return F

    zGuess = np.array([1, 1, 1])

    if st.button("Solve Equations"):
        z = fsolve(myFunction, zGuess)
        st.write(f"Solutions for x, y, w: {z}")
