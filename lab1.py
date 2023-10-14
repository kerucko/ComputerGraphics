import numpy as np
import matplotlib.pyplot as plt
import matplotlib.widgets as plt_widgets

def update_graph(event):
    a = float(a_textbox.text)
    A = float(A_textbox.text)
    B = float(B_textbox.text)

    ax.clear()
    ax.set_title('ρ = a/ф')

    phi = np.arange(A+0.05, B, 0.05)
    rho = a / phi

    ax.plot(phi, rho, lw=2)
    plt.draw()

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, polar=True)
ax.set_title('ρ = a/ф')

phi = np.arange(3, 10, 0.05)
rho = 1 / phi

ax.plot(phi, rho, lw=2)

a_textbox = plt_widgets.TextBox(plt.axes([0.1, 0.9, 0.1, 0.05]), 'a', initial='1')
A_textbox = plt_widgets.TextBox(plt.axes([0.3, 0.9, 0.1, 0.05]), 'A', initial='3')
B_textbox = plt_widgets.TextBox(plt.axes([0.5, 0.9, 0.1, 0.05]), 'B', initial='10')

update_button = plt_widgets.Button(plt.axes([0.7, 0.9, 0.1, 0.05]), 'Update')
update_button.on_clicked(update_graph)

plt.show()