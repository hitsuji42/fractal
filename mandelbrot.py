# coding: utf-8


import matplotlib.pyplot as plt
import matplotlib.cm as cm


def initialize_image(x_p, y_p):
    image = []
    for i in range(y_p):
        x_colors = []
        for j in range(x_p):
            x_colors.append(0)
        image.append(x_colors)
    return image


def man():
    x_p = 400
    y_p = 400
    image = initialize_image(x_p+1, y_p+1)
    max_iteration = 16
    for i in range(x_p+1):
        print(i)
        for k in range(y_p+1):
            x = 3.5*i/x_p - 2.0
            y = 2.0*k/y_p - 1.0
            z1 = 0 + 0j
            c = x + y * 1j
            iteration = 0
            while (abs(z1) < 2) and (iteration < max_iteration):
                z1 = z1*z1 + c
                iteration += 1
            else:
                image[k][i] = iteration

    plt.imshow(image, origin='lower', extent=(-2.5, 1.0, -1.0, 1.0),
               cmap=cm.Greys_r, interpolation='nearest')
    plt.colorbar()
    plt.show()

if __name__ == '__main__':
    man()
