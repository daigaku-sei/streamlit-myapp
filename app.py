import streamlit as st
from sympy import symbols, integrate, latex
import numpy as np
import matplotlib.pyplot as plt

# Define the functions
x = symbols('x')

functions = {
    latex(x): x,
    latex(x**2): x**2,
    latex(2*x**3-7*x+4): 2*x**3-7*x+4
}

def main():
    st.title("Интегрируем")

    # Create a container to center-align the widgets
    container = st.container()
    col1, col2, col3 = container.columns(3)

    # Function selection
    with col1:
        selected_function = st.selectbox("Выбор функции", list(functions.keys()), format_func=lambda func: func)
        st.latex(f"f(x) = {latex(functions[selected_function])}")

    # Bounds selection
    with col2:
        left_bound = st.number_input("Левая граница", value=0.0)
    with col3:
        right_bound = st.number_input("Правая граница", value=1.0)

    # Calculate the integral
    integral = integrate(functions[selected_function], (x, left_bound, right_bound))

    # Display the LaTeX name of the function
    st.latex(f"Выбрана: {latex(functions[selected_function])}")

    # Button for drawing the function with integral area
    if st.button("Нарисовать график"):
        x_vals = np.linspace(left_bound, right_bound, 100)
        y_vals = [functions[selected_function].subs(x, val) for val in x_vals]

        plt.plot(x_vals, y_vals, label=selected_function)
        plt.fill_between(x_vals, y_vals, 0, where=(x_vals >= left_bound) & (x_vals <= right_bound), alpha=0.3)

        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend()
        st.pyplot()

    # Display the result
    st.write(f"Интеграл найден! Он равен {integral:.4f}")

if __name__ == "__main__":
    main()
