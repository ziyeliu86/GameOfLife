import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as a3
import matplotlib.colors as colors


def icoshpere(n):
    v, f = icosahedron()
    for i in range(n):
        f_new = np.zeros((f.shape[0]*4, 3)).astype(int)
        for j in range(f.shape[0]):
            tri = f[j, :]
            a, v = split_line(tri[0], tri[1], v)
            b, v = split_line(tri[1], tri[2], v)
            c, v = split_line(tri[2], tri[0], v)

            f_new[4*j, :] = [tri[0], a, c]
            f_new[4*j+1, :] = [tri[1], b, a]
            f_new[4*j+2, :] = [tri[2], c, b]
            f_new[4*j+3, :] = [a, b, c]
        f = f_new
    v, _, ids = np.unique(
        v, return_index=True, return_inverse=True,
        axis=0)
    f = np.unique(ids[f], axis=0)
    return v, f


def split_line(t1, t2, v):
    v1 = v[t1, :]
    v2 = v[t2, :]
    vm = (v1 + v2) / 2
    vm = vm / np.linalg.norm(vm)
    t = v.shape[0]
    v = np.vstack((v, vm[np.newaxis, :]))
    return t, v


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
    v, f = icoshpere(3)
    plot_polyhedron(v, f)
