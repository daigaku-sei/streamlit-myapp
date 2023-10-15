import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols, sympify, integrate, latex

st.set_option('deprecation.showPyplotGlobalUse', False)

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
        function_type = st.radio("Выбор функции", ("Выбрать из списка", "Ввести свою функцию"))

        if function_type == "Выбрать из списка":
            selected_function = st.selectbox("Выберите функцию", list(functions.keys()), format_func=lambda func: func)
        else:
            custom_function = st.text_input("Введите свою функцию", value="x")
            selected_function = custom_function

            # Add custom function to the functions dictionary if it's not already there
            if selected_function not in functions:
                functions[selected_function] = sympify(selected_function)

        st.latex(f"f(x) = {latex(functions[selected_function])}")

    # Bounds selection
    with col2:
        left_bound = st.number_input("Левая граница", value=0.0)
    with col3:
        right_bound = st.number_input("Правая граница", value=1.0)

    # Calculate the integral
    if selected_function in functions:
        integral = integrate(functions[selected_function], (x, left_bound, right_bound))
    else:
        integral = integrate(selected_function, (x, left_bound, right_bound))

    # Display the LaTeX name of the function
    if selected_function in functions:
        st.latex(f"Выбрана: {latex(functions[selected_function])}")
    else:
        st.latex(f"Выбрана: {selected_function}")

    # Display the result
    st.write(f"Интеграл найден! Он равен {integral:.4f}")

    # Generate x values for plotting
    x_vals = np.linspace(left_bound, right_bound, 100)
    # Generate y values by evaluating the selected function at x values
    if selected_function in functions:
        y_vals = [functions[selected_function].subs(x, val) for val in x_vals]
    else:
        y_vals = [sympify(selected_function).subs(x, val) for val in x_vals]

    # Plot the function
    fig, ax = plt.subplots()
    ax.plot(x_vals, y_vals, label=f"f(x) = {latex(functions[selected_function])}")

    x_vals = np.linspace(left_bound, right_bound, 100)
    y_vals = [functions[selected_function].subs(x, val) for val in x_vals]

    # Handle non-finite values
    y_vals = np.array(y_vals)
    y_vals[~np.isfinite(y_vals)] = 0.0

    ax.fill_between(x_vals, y_vals, where=(x_vals >= left_bound) & (x_vals <= right_bound), alpha=0.3)
    ax.legend()
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.set_title("График функции и область под интегралом")
    st.pyplot(fig)

if __name__ == "__main__":
    main()
