import re
import numpy as np
import matplotlib.pyplot as plt
from fourier import FourierInterp


def get_fourier(file, ratio, origin):
    with open(file, 'r') as fin:
        points = []

        s = fin.read()
        g = re.search(r'<polygon class="cls-1" points="([^/]*)"/>', s)
        path = g.group(1)
        data = path.split()

        N_point = len(data) // 2 - 1
        print(f'points: {N_point}')
        for i in range(N_point):
            v = float(data[2 * i]) - 1j * float(data[2 * i + 1])
            points.append(v)

        points = np.array(points, dtype=np.complex128)
        trans = origin - points[0]
        points += trans

        interp = FourierInterp(points, int(N_point*ratio))

    return interp, points


def plot_file(file, ratio, tmax, Nt, origin, show_points=True):
    interp, points = get_fourier(file, ratio, origin)
    t = np.arange(Nt) / Nt * tmax
    c = interp.eval(t)

    plt.plot(c.real, c.imag, '-b')
    if show_points:
        plt.scatter(points.real, points.imag)


show_points = False

# 头发外圈/呆毛
plot_file('../SVG/资源 7.svg', 0.3, 32/51, 500, 673.78-591.77j, show_points=show_points)
plot_file('../SVG/资源 8.svg', 0.3, 26/27, 500, 872.38-185.93j, show_points=show_points)

# 左耳
plot_file('../SVG/资源 11.svg', 0.3, 13/24, 500, 737.04-303.91j, show_points=show_points)
plot_file('../SVG/资源 12.svg', 0.3, 14/26, 500, 777.29-223.05j, show_points=show_points)

# 右耳
plot_file('../SVG/资源 13.svg', 0.3, 15/26, 500, 1058.73-301.82j, show_points=show_points)
plot_file('../SVG/资源 15.svg', 0.3, 12/22, 500, 1009.13-224.35j, show_points=show_points)

# 发饰
plot_file('../SVG/资源 16.svg', 0.3, 1/1, 500, 751.55-286.05j, show_points=show_points)

# 嘴
plot_file('../SVG/资源 17.svg', 0.4, 19/22, 500, 873.11-504.55j, show_points=show_points)

# 眼
plot_file('../SVG/资源 18.svg', 0.3, 8/20, 500, 793.39-416.73j, show_points=show_points)
plot_file('../SVG/资源 19.svg', 0.3, 8/20, 500, 927.25-418.49j, show_points=show_points)

# 头发
plot_file('../SVG/资源 20.svg', 0.4, 5/17, 500, 844.29-591.77j, show_points=show_points)
plot_file('../SVG/资源 21.svg', 0.3, 8/14, 500, 797.95-511.07j, show_points=show_points)

# 下巴
plot_file('../SVG/资源 22.svg', 0.4, 12/24, 500, 787.68-455.19j, show_points=show_points)

# 头发
plot_file('../SVG/资源 23.svg', 0.6, 6/10, 500, 775.47-440.32j, show_points=show_points)
plot_file('../SVG/资源 25.svg', 0.4, 14/23, 500, 779.6-427.11j, show_points=show_points)
plot_file('../SVG/资源 27.svg', 0.5, 10/16, 500, 818.9-341.77j, show_points=show_points)
plot_file('../SVG/资源 28.svg', 0.5, 14/21, 500, 839.53-320.86j, show_points=show_points)
plot_file('../SVG/资源 29.svg', 0.5, 8/15, 500, 884.98-390.8j, show_points=show_points)
plot_file('../SVG/资源 31.svg', 0.3, 11/18, 500, 907.93-387.89j, show_points=show_points)
plot_file('../SVG/资源 30.svg', 0.4, 18/24, 500, 958.85-368.18j, show_points=show_points)
plot_file('../SVG/资源 33.svg', 0.4, 11/18, 500, 997.91-455.58j, show_points=show_points)

plot_file('../SVG/资源 34.svg', 0.3, 13/20, 500, 962.71-500.57j, show_points=show_points)
plot_file('../SVG/资源 35.svg', 0.2, 7/23, 500, 973.23-512.54j, show_points=show_points)

# 脖子、肩
plot_file('../SVG/资源 36.svg', 0.3, 22/31, 500, 867.23-517.53j, show_points=show_points)
plot_file('../SVG/资源 37.svg', 0.2, 5/17, 500, 866.47-524.94j, show_points=show_points)
plot_file('../SVG/资源 38.svg', 0.2, 6/19, 500, 916.6-525.07j, show_points=show_points)

# 左手
plot_file('../SVG/资源 39.svg', 0.3, 11/19, 500, 713.25-591.77j, show_points=show_points)
plot_file('../SVG/资源 40.svg', 0.3, 7/17, 500, 735.43-558.66j, show_points=show_points)
plot_file('../SVG/资源 41.svg', 0.3, 9/17, 500, 741.89-578.78j, show_points=show_points)
plot_file('../SVG/资源 42.svg', 0.3, 7/16, 500, 762.3-591.77j, show_points=show_points)
plot_file('../SVG/资源 43.svg', 0.3, 14/21, 500, 778.52-515.38j, show_points=show_points)

# 右手
plot_file('../SVG/资源 44.svg', 0.3, 14/21, 500, 1079.57-591.77j, show_points=show_points)
plot_file('../SVG/资源 45.svg', 0.3, 9/15, 500, 1069.37-556.5j, show_points=show_points)
plot_file('../SVG/资源 46.svg', 0.3, 9/18, 500, 1069.23-578.12j, show_points=show_points)
plot_file('../SVG/资源 47.svg', 0.3, 5/12, 500, 1050.57-591.77j, show_points=show_points)
plot_file('../SVG/资源 48.svg', 0.3, 17/23, 500, 1007.64-529.32j, show_points=show_points)

# 眉毛
plot_file('../SVG/资源 49.svg', 0.2, 8/21, 500, 785.6-322.06j, show_points=show_points)
plot_file('../SVG/资源 50.svg', 0.2, 7/20, 500, 997.18-322.39j, show_points=show_points)

plt.show()
