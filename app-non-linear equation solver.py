import streamlit as st
from scipy.optimize import fsolve
import numpy as np

st.title("Nonlinear Equation Solver")

st.write("Enter a system of equations in the form of F(x, y, w) = 0")

# User input for the equations
equation1 = st.text_input("Equation 1 (e.g., 'x**2 + y**2 - 20 = 0'):")
equation2 = st.text_input("Equation 2 (e.g., 'y - x**2 = 0'):")
equation3 = st.text_input("Equation 3 (e.g., 'w + 5 - x*y = 0'):")

def myFunction(z):
    x = z[0]
    y = z[1]
    w = z[2]

    F = np.empty((3))
    F[0] = eval(equation1)  # Parse and evaluate user input as the first equation
    F[1] = eval(equation2)  # Parse and evaluate user input as the second equation
    F[2] = eval(equation3)  # Parse and evaluate user input as the third equation
    return F

zGuess = np.array([1, 1, 1])

if st.button("Solve Equations"):
    z = fsolve(myFunction, zGuess)
    st.write(f"Solutions for x, y, w: {z}")
