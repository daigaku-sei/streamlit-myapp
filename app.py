import streamlit as st
from sympy import symbols, integrate, latex
import numpy as np
#import matplotlib.pyplot as plt

# Define the functions
x = symbols('x')

functions = {
    '/': x,
    'U': x**2,
    '2*x**3-7*x+4': 2*x**3-7*x+4
}

def main():
    st.title("Интегрируем")

    # Create a container to center-align the widgets
    container = st.container()
    col1, col2, col3 = container.columns(3)

    # Function selection
    with col1:
        selected_function = st.selectbox("Select a function", list(functions.keys()))

    # Bounds selection
    with col2:
        left_bound = st.number_input("Enter the left bound", value=0.0)
    with col3:
        right_bound = st.number_input("Enter the right bound", value=1.0)

    # Steps selection
    #steps = st.number_input("Enter the number of steps", value=100)

    # Calculate the integral
    integral = integrate(functions[selected_function], (x, left_bound, right_bound))

    # Display the LaTeX name of the function
    st.latex(f"Выбрана: {latex(functions[selected_function])}")

    # Plot the function with the integral area
    #x_vals = np.linspace(left_bound, right_bound, 100)
    #y_vals = [functions[selected_function].subs(x, val) for val in x_vals]

    #plt.plot(x_vals, y_vals, label=selected_function)
    #plt.fill_between(x_vals, y_vals, 0, where=(x_vals >= left_bound) & (x_vals <= right_bound), alpha=0.3)

    #plt.xlabel('x')
    #plt.ylabel('y')
    #plt.legend()
    #st.pyplot()

    # Display the result
    st.write(f"Интеграл найден! Он равен {integral}")

if __name__ == "__main__":
    main()
