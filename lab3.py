import numpy as np
from scipy.linalg import norm
import matplotlib.pyplot as plt
import matplotlib.widgets as plt_widgets
from matplotlib.colors import LightSource


def truncated_cone(event):
    p0 = np.array([5, 5, 2])
    p1 = np.array([5, 5, 9])
    R0, R1 = 6, 2
    accuracy = int(textbox.text)
    deg = int(deg_textbox.text)

    v = p1 - p0
    mag = norm(v)
    v = v / mag
    not_v = np.array([1, 1, 0])
    if (v == not_v).all():
        not_v = np.array([0, 1, 0])
    n1 = np.cross(v, not_v)
    n1 /= norm(n1)
    n2 = np.cross(v, n1)

    t = np.linspace(0, mag, accuracy)
    theta = np.linspace(0, 2 * np.pi, accuracy)
    t, theta = np.meshgrid(t, theta)

    R = np.linspace(R0, R1, accuracy)
    X, Y, Z = [p0[i] + v[i] * t + R * np.sin(theta) * n1[i] + R * np.cos(theta) * n2[i] for i in [0, 1, 2]]

    ax.clear()
    light = LightSource(azdeg=deg, altdeg=15)
    ax.plot_surface(X, Y, Z, shade=True, lightsource=light)
    plt.draw()


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d')

ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_zlim(0, 10)

textbox = plt_widgets.TextBox(plt.axes([0.15, 0.05, 0.3, 0.075]), "Accuracy", initial=20)
deg_textbox = plt_widgets.TextBox(plt.axes([0.15, 0.15, 0.3, 0.075]), "Light", initial=15)
update_button = plt_widgets.Button(plt.axes([0.6, 0.05, 0.1, 0.075]), "Update")
update_button.on_clicked(truncated_cone)

plt.show()