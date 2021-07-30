import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as a3
import matplotlib.colors as colors


def icosahedron():
    """ICOSAHEDRON creates unit regular icosahedron
    Returns 12 vertex and 20 face values"""
    t = (1 + np.sqrt(5)) / 2
    # create vertices
    v = np.array([
        [-1, t, 0],
        [1, t, 0],
        [-1, -t, 0],
        [1, -t, 0],
        [0, -1, t],
        [0, 1, t],
        [0, -1, -t],
        [0, 1, -t],
        [t, 0, -1],
        [t, 0, 1],
        [-t, 0, -1],
        [-t, 0, 1]])
    # normalise vertices to unit size
    v = v / np.linalg.norm(v[0, :])
    # create f
    f = np.array([
        [0, 11, 5],
        [0, 5, 1],
        [0, 1, 7],
        [0, 7, 10],
        [0, 10, 11],
        [1, 5, 9],
        [5, 11, 4],
        [11, 10, 2],
        [10, 7, 6],
        [7, 1, 8],
        [3, 9, 4],
        [3, 4, 2],
        [3, 2, 6],
        [3, 6, 8],
        [3, 8, 9],
        [4, 9, 5],
        [2, 4, 11],
        [6, 2, 10],
        [8, 6, 7],
        [9, 8, 1]])
    return v, f


def plot_polyhedron(v, f):
    ax = a3.Axes3D(plt.figure())
    # ax.dist=10
    # ax.azim=30
    # ax.elev=10
    ax.set_xlim([-1.5, 1.5])
    ax.set_ylim([-1.5, 1.5])
    ax.set_zlim([-1.5, 1.5])

    triangles = v[f[:, :]]

    for sq in triangles:
        f = a3.art3d.Poly3DCollection(sq)
        f.set_color(colors.rgb2hex(np.random.random(3)))
        f.set_edgecolor('k')
        # f.set_alpha(1.0)
        ax.add_collection3d(f)

    plt.show()


if __name__ == "__main__":
    v, f = icosahedron()
    plot_polyhedron(v, f)
