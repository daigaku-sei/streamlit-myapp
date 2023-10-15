import streamlit as st
from sympy import symbols, integrate, latex

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

            # Add custom function to the functions dictionary
            functions[selected_function] = selected_function

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

if __name__ == "__main__":
    main()
