import matplotlib.pyplot as plt
import panel as pn
import streamlit as st
import numpy as np

# Define the function to integrate
def f(x):
    return 2*x**3 - 7*x + 4

# Define the integral function
def integral(a, b, n):
    x = np.linspace(a, b, n)
    y = f(x)
    dx = (b - a) / n
    return np.sum(y) * dx

# Create the widgets
left_bound = pn.widgets.FloatSlider(value=-5, start=-10, end=10, step=0.1, name='Левая граница')
right_bound = pn.widgets.FloatSlider(value=5, start=-10, end=10, step=0.1, name='Правая граница')
steps = pn.widgets.IntSlider(value=100, start=1, end=1000, step=1, name='Шаги')

function_name = r'$2x^3 - 7x + 4$'

# Create the integral widget
integral_widget = pn.widgets.StaticText(name='Результат интеграла')

# Create the button to solve the integral
solve_button = pn.widgets.Button(name='Решить интеграл')

# Define the callback function for the button
def solve_integral(event):
    left = left_bound.value
    right = right_bound.value
    n_steps = steps.value
    result = integral(left, right, n_steps)
    integral_widget.value = f'{result}'
    
    # Update the plot with the integral area
    ax.fill_between(x, y, where=(x >= left) & (x <= right), alpha=0.3, color='orange')
    fig.canvas.draw()

# Add the callback to the button
solve_button.on_click(solve_integral)

# Create the figure and axis
fig, ax = plt.subplots()

# Set the visibility of the spines
ax.spines['left'].set_visible(True)
ax.spines['bottom'].set_visible(True)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

# Set the labels for the x and y axes
ax.set_xlabel('x')
ax.set_ylabel('y')

# Set the title of the plot
ax.set_title(f'График функции: {function_name}', fontsize=14)

# Generate x and y values for the plot
x = np.linspace(-10, 10, 100)
y = f(x)

# Plot the function
ax.plot(x, y, label=function_name)
ax.legend()

# Create the layout
app_layout = pn.Column(
    pn.layout.FlexBox(pn.Row(left_bound), align_items='center'),
    pn.layout.FlexBox(pn.Row(right_bound), align_items='center'),
    pn.layout.FlexBox(pn.Row(steps), align_items='center'),
    pn.layout.FlexBox(pn.Row(solve_button), align_items='center'),
    pn.layout.FlexBox(pn.Row(integral_widget), align_items='center'),
    pn.pane.Matplotlib(fig, tight=True)
)

# Serve the app
app_layout.servable(title='Простой расчет интеграла')
#pn.serve_as_panel_app(app)
